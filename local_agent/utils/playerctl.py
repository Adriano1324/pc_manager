import subprocess
import time

from utils.format import get_metadata_for_player


def base_playerctl_operation(operation, player=None, value=""):
    if player:
        subprocess.run(f"playerctl -p {player} {operation} {value}".split(" "))
    else:
        subprocess.run(f"playerctl {operation} {value}".split(" "))
    time.sleep(1.5)
    return get_metadata_for_player(player)
