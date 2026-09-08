from fastapi import APIRouter
#======================================================================#
auth_router:APIRouter = APIRouter(prefix="/auth", tags=["auth"])
#======================================================================#
@auth_router.get("/test1")
async def test1(text:str, integer:int=0, float_num:float=0.0, boolean:bool=False) -> dict:
    #----------------------------------------------------------------------#
    return {
        "text":text,
        "integer":integer,
        "float_num":float_num,
        "boolean":boolean,
            }
#----------------------------------------------------------------------#