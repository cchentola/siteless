from fastapi import FastAPI

from routes.content_routes import content_router
from routes.customer_routes import customer_router
from routes.owner_routes import (
    owner_router,
)
from routes.predict_routes import predict_router

app = FastAPI()

app.include_router(owner_router, prefix="/owner", tags=["owner"])
app.include_router(customer_router, prefix="/customer", tags=["customer"])
app.include_router(content_router, prefix="/content", tags=["content"])
app.include_router(predict_router, prefix="/predict", tags=["predict"])
