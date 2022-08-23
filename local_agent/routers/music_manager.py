import subprocess

from fastapi import APIRouter
from utils.format import get_metadata_for_player
from utils.playerctl import base_playerctl_operation

router = APIRouter()


@router.get("/players")
def list_actual_players():
    return subprocess.getoutput("playerctl -l").split("\n")


@router.get("/metadata")
def get_metadata(players: str = None):
    if not players:
        players = subprocess.getoutput("playerctl -l").split("\n")
    return get_metadata_for_player(players)


@router.get("/position")
def get_position(player: str = None):
    return float(subprocess.getoutput(f"playerctl -p {player} position"))


@router.post("/{operation}")
def music_change(operation:str, value:str=None, player: str = None):
    """
    Shuffle can be "On", "Off", or "Toggle".
    Can be "None", "Track", or "Playlist".
    """
    return base_playerctl_operation(operation.replace("_", "-"), player, value)
