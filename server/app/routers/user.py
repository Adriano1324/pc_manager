from app.auth.utils import get_current_active_user, get_password_hash
from app.db import get_db
from app.models import user as UserModels
from fastapi import APIRouter, Depends

router = APIRouter()


@router.post("")
def create_user(user: UserModels.CreateUser):
    db = get_db()
    users_collection = db["users"]
    user.password = get_password_hash(user.password)
    users_collection.insert_one(UserModels.User(**user.dict()).dict())
    return user.username


@router.get("/me")
async def read_users_me(
    current_user: UserModels.User = Depends(get_current_active_user),
):
    return current_user
