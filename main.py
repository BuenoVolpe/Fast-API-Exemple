from fastapi import FastAPI
#======================================================================#
app:FastAPI = FastAPI()
#----------------------------------------------------------------------#
from routes.auth import auth_router
from routes.orders import orders_router
#======================================================================#
app.include_router(auth_router)
app.include_router(orders_router)
#======================================================================#
#RUN: uvicorn main:app --reload
#======================================================================#
