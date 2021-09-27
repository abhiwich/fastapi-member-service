from fastapi import FastAPI

from app.server.routes.member import router as MemberRouter
app = FastAPI()

app.include_router(MemberRouter, tags=["Member"], prefix="/member")


# @app.get("/", tags=["Root"])
# async def read_root():
#     return {"message": "Welcome to this fantastic app!"}

 