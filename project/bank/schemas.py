#forces datatypes
from pydantic import BaseModel
from typing import Optional
#======================================================================#
class UserSchema(BaseModel):
    #id #we dont use id since w dont pass ids to create a user 
    name:str
    email:str
    password:str
    admin:Optional[bool]
    active:Optional[bool]
    #======================================================================#
    class Config:
        #----------------------------------------------------------------------#
        from_attributes:bool=True #connects with model
#======================================================================#
#----------------------------------------------------------------------#

