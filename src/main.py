from fastapi import FastAPI, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from pydantic import BaseModel
from src.containers import Container
from src.core.services import UserService
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class UserRequest(BaseModel):
    email: str

@app.post("/users")
@inject
def create_user(
    request: UserRequest,
    service: UserService = Depends(Provide[Container.user_service])
):
    try:
        user = service.register_user(request.email)
        return {"id": user.id, "email": user.email, "status": "created"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Initialize Container
container = Container()