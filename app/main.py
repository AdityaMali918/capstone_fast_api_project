from fastapi import FastAPI
from app.api import routes_auth, routes_predict
from app.core.exceptions import register_expcetion_handler
from app.middleware.logging_middleware import LoggingMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title='Car Price Prediction API')


app.add_middleware(LoggingMiddleware)


app.include_router(routes_auth.router, tags=['Auth'])
app.include_router(routes_predict.router, tags=['Prediction'])


# monitoring using Prometheus
Instrumentator().instrument(app).expose(app)


# add exception handler
register_expcetion_handler(app)