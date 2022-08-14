from app.queries import agent as AgentQueries
from fastapi import APIRouter

router = APIRouter()


@router.get("")
def get_agent_informations(key: str):
    return AgentQueries.get_agent(key)
