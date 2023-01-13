from fastapi import FastAPI
from routes.games import router

app = FastAPI()
# Register routes
app.include_router(router, prefix="")