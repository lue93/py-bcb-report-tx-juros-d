from fastapi import APIRouter

from exceptions_custom import CustomException
from file_handler import read
from json_formatter import to_json

router = APIRouter(prefix="/api/v1/historico-taxa-juros-diario", tags=["historico-taxa-juros-diario"])

@router.get("/atual")
async def read_actually():
    response = ""
    try:
        response = read()        
    except:
        raise CustomException("We can´t proccess it now, try later")
    finally:
        response = json.loads(to_json(response))
        return JSONResponse(
            content=response, 
            status_code=200,
            media_type="application/json")
         