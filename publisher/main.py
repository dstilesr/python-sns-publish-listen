from fastapi import FastAPI
from api.views import router


app = FastAPI(
    title="SNS Publisher service",
    description="Publishes received messages to SNS",
    redoc_url="/redoc"
)

app.include_router(router, prefix="/publish")
