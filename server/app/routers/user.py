from app.auth.utils import get_current_active_user, get_password_hash
from app.core.utils import get_random_string
from app.db import get_db
from app.models import local_agent as AgentModels
from app.models import user as UserModels
from fastapi import APIRouter, Depends

router = APIRouter()


@router.post("")
def create_user(user: UserModels.CreateUser):
    db = get_db()
    users_collection = db["users"]
    agent_collection = db["agents"]
    user.password = get_password_hash(user.password)
    users_collection.insert_one(UserModels.User(**user.dict()).dict())
    agent = AgentModels.LocalAgent(
        user_username=user.username, key=get_random_string(64)
    )
    agent_collection.insert_one(agent.dict())
    return {"username": user.username, "key": agent.key}


@router.get("/me")
async def read_users_me(
    current_user: UserModels.User = Depends(get_current_active_user),
):
    return current_user
