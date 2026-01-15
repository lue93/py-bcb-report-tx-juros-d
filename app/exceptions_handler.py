
from exception import CustomException

@app.exception_handler(CustomException) 
async def app_exception_handler(request: Request, exc: CustomException): 
    return JSONResponse( 
        status_code=400, 
        content={
            "message": exc.message, 
            "route": str(request.url)
            } 
    )