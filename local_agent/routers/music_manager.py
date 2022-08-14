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


@router.post("/next")
def play_next_song(player: str = None):
    return base_playerctl_operation("next", player)


@router.post("/previous")
def play_previous_song(player: str = None):
    return base_playerctl_operation("previous", player)


@router.post("/play")
def play_song(player: str = None):
    return base_playerctl_operation("play", player)


@router.post("/pause")
def pause_song(player: str = None):
    return base_playerctl_operation("pause", player)


@router.post("/play_pause")
def play_pause_song(player: str = None):
    return base_playerctl_operation("play-pause", player)


@router.post("/stop")
def stop_song(player: str = None):
    return base_playerctl_operation("stop", player)


@router.post("/position")
def ser_song_position(operation: str, player: str = None):
    return base_playerctl_operation("position", player, operation)


@router.post("/volume")
def set_song_volume(operation: str, player: str = None):
    return base_playerctl_operation("volume", player, operation)


@router.post("/open")
def open_song(uri: str, player: str = None):
    return base_playerctl_operation("open", player, uri)


@router.post("/loop")
def loop_song(status: str, player: str = None):
    """
    Can be "None", "Track", or "Playlist".
    """
    return base_playerctl_operation("loop", player, status)


@router.post("/shuffle")
def set_shuffle(status: str, player: str = None):
    """
    Can be "On", "Off", or "Toggle".
    """
    return base_playerctl_operation("shuffle", status, player)
