from fastapi import FastAPI
#======================================================================#
app:FastAPI = FastAPI() #create FastAPI instance
#======================================================================#
#import routes
from project.routes.auth import auth_router
from project.routes.orders import orders_router
#----------------------------------------------------------------------#
#creates routes
app.include_router(auth_router)
app.include_router(orders_router)
#======================================================================#
#how to run
#IMPORT LIBRARIES: python -m pip install fastapi uvicorn sqlalchemy sqlalchemy_utils alembic passlib[bcrypt] python_jose[cryptography] python-dotenv python_multipart
#RUN ON TERMINAL: uvicorn main:app --reload
#RUN ON TERMINAL TO START MIGRATION: alembic revision --autogenerate -m "Initial Migration" 
#RUN ON TERMINAL TO FINISH MIGRATION: alembic upgrad head
#======================================================================#

