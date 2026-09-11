from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
#----------------------------------------------------------------------#
from project.bank.models import db, User
from project.bank.dependencies import get_session
from project.bank.schemas import UserSchema
#----------------------------------------------------------------------#
from main import bcrypt_context
#======================================================================#
auth_router:APIRouter = APIRouter(prefix="/auth", tags=["auth"])
#======================================================================#
@auth_router.get("/test1") #creates route with needed arguments
async def test1(text:str, integer:int=0, float_num:float=0.0, boolean:bool=False) -> dict:
    #----------------------------------------------------------------------#
    return { #returns JSON
        "text":text,
        "integer":integer,
        "float_num":float_num,
        "boolean":boolean,
            }
#----------------------------------------------------------------------#
@auth_router.post("/create_accont")
async def create_accont(user_schema:UserSchema, session:Session=Depends(get_session)) -> dict:
    #----------------------------------------------------------------------#
    email:str = user_schema.email
    name:str = user_schema.name
    password:str = user_schema.password
    #----------------------------------------------------------------------#
    #gets user
    user = session.query(User).filter(User.email==email).first()
    #----------------------------------------------------------------------#
    #if user exists
    if user:
        raise HTTPException(status_code=400, detail=f"user {name} with email {email} already exist")
    #----------------------------------------------------------------------#
    #cryptographs password
    crypt_password = bcrypt_context.hash(password)
    #----------------------------------------------------------------------#
    #if it doens't exist
    new_user = User(name, email, crypt_password) #creates new user
    session.add(new_user) #add new user
    session.commit() #commit changes
    #----------------------------------------------------------------------#
    return {
        "message": f"user {name} with email {email} created"
    }