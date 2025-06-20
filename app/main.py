from fastapi import FastAPI, HTTPException
from app.api.api import api_router
from app.core import exception_handlers
from sqlalchemy.exc import IntegrityError


app = FastAPI(
    title="Client Favorites API",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api")
app.add_exception_handler(HTTPException, exception_handlers.http_exception_handler)
app.add_exception_handler(Exception, exception_handlers.generic_exception_handler)
app.add_exception_handler(IntegrityError, exception_handlers.sqlalchemy_integrity_error_handler)
