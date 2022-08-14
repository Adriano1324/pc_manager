from webbrowser import get
from pydantic import BaseModel

class LocalAgent(BaseModel):
    user_username: str
    key: str 
    name: str = "Kira"
    active: bool = True

class AgentRequest(BaseModel):
    key: str