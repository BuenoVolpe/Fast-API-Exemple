from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker, Session
#----------------------------------------------------------------------#
from project.bank.models import db, User
#======================================================================#
def get_session():
    #----------------------------------------------------------------------#
    try:
        #----------------------------------------------------------------------#
        #creates session for the databank
        NewSession:sessionmaker = sessionmaker(bind=db)
        session:Session = NewSession() 
        #----------------------------------------------------------------------#
        yield session # returns but doesn't end the function
        #----------------------------------------------------------------------#
    finally: #executes if error or if it works property
        session.close()

