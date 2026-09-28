from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

def register_expcetion_handler(app: FastAPI):
    @app.exception_handler(Exception)
    async def unhandled_exception_handler(req: Request, exc : Exception):
        return JSONResponse(status_code=500, content={'detail': str(exc)})