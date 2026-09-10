from sqlalchemy import create_engine, Engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
# from sqlalchemy_utils.types import ChoiceType
#======================================================================#
sqlite:str = "sqlite:///"#sqlite format #*local
url:str = f"{sqlite}project/bank/bank.db" #data bank url #*local for now
#----------------------------------------------------------------------#
db:Engine = create_engine(url=url) #creates data bank
#======================================================================# 
Base = declarative_base() #data bank base
#======================================================================#
#data bank classes/tables
#----------------------------------------------------------------------#
#Users
class User(Base):
    #======================================================================#
    __tablename__:str = "users" #sets a expecified name
    #======================================================================#
    #Columns
    id:Column = Column("id", Integer, primary_key=True, autoincrement=True) 
    #----------------------------------------------------------------------#
    name:Column = Column("name", String) 
    email:Column = Column("email", String, nullable=False)
    password:Column = Column("password", String)
    #----------------------------------------------------------------------#
    active:Column = Column("active", Boolean)
    #----------------------------------------------------------------------#
    admin:Column = Column("admin", Boolean, default=False)
    #======================================================================#
    def __init__(self, name:str, email:str, password:str, active:bool=True, admin:bool=False) -> None: #what's gonna do after creating user
        #----------------------------------------------------------------------#
        self.name:str = name
        self.email:str = email
        self.password:str = password
        self.active:bool = active
        self.admin:bool = admin
        #----------------------------------------------------------------------#
        return
#----------------------------------------------------------------------#
#Orders
class Order(Base):
    #----------------------------------------------------------------------#
    __tablename__:str = "orders"
    #----------------------------------------------------------------------#
    # STATUS_TYPES:list = [
    #     ("PENDING", "pending"),
    #     ("COMPLETED", "completed"),
    #     ("CANCELLED", "cancelled"),
    # ]
    #----------------------------------------------------------------------#
    id:Column = Column("id", Integer, primary_key=True, autoincrement=True)
    status:Column = Column("status", String) #pending, completed, cancelled
    user:Column = Column("user", ForeignKey("users.id")) #uses the id value on the users table
    price:Column = Column("price", Float)
    #itens:Column = Column("itens", )
    #======================================================================#
    def __init__(self, user:int, status:str="PENDING", price:float= 0.0) -> None:
        #----------------------------------------------------------------------#
        self.user:int = user
        self.status:str = status
        self.price:float = price
#----------------------------------------------------------------------#
#OrderItens
class OrderItens(Base):
    #----------------------------------------------------------------------#
    __tablename__:str = "order_itens"
    #----------------------------------------------------------------------#
    id:Column = Column("id", Integer, primary_key=True, autoincrement=True)
    quantity:Column = Column("quantity", Integer)
    flavour:Column = Column("flavour", String)
    size:Column = Column("size", String)
    unitary_price:Column = Column("unitary_price", Float)
    order:Column = Column("order", ForeignKey("orders.id"))
    #======================================================================#
    def __init__(self, quantity:int, flavou:str, size:str, unitary_price:float=0.0, order:int=0) -> None:
        self.quantity:int = quantity
        self.flavou:str = flavou
        self.size:str = size
        self.unitary_price:float = unitary_price
        self.order:int = order
#======================================================================#
#execute the metadata creation (effectivally creates data bank)
#======================================================================#
