from app.db import get_db


def get_user(username: str):
    db = get_db()
    users_collection = db["users"]
    return users_collection.find_one({"username": username}, {"_id": 0})
