from app.db import get_db
def get_agent(key:str):
    db = get_db()
    agents_collection = db["agents"]
    return agents_collection.find_one({"key": key}, {"_id": 0})
