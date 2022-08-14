import re
import subprocess

from core.models.music import MusicInformationResponse, MusicMetadata


def get_first_player():
    result = subprocess.getoutput("playerctl -l")
    return result.split("\n")[0]


def get_metadata_for_player(players=None):
    if players is None:
        players = get_first_player()
    if not isinstance(players, list):
        players = [players]
    return [
        MusicInformationResponse(
            metadata=format_music_metadata(
                subprocess.getoutput(f"playerctl -p {player} metadata")
            ),
            status=subprocess.getoutput(f"playerctl -p {player} status"),
            position=subprocess.getoutput(f"playerctl -p {player} position"),
            volume=subprocess.getoutput(f"playerctl -p {player} volume"),
            player=player,
            loop=subprocess.getoutput(f"playerctl -p {player} loop"),
            shuffle=subprocess.getoutput(f"playerctl -p {player} shuffle")
        )
        for player in players
    ]


def format_music_metadata(data: str):
    addons = ["chromium", "spotify", "mpris", "xesam"]
    attributes = [
        "trackid",
        "length",
        "artUrl",
        "album",
        "albumArtist",
        "artists",
        "autoRating",
        "discNumber",
        "title",
        "trackNumber",
        "url",
    ]
    response = {}
    rows = data.split("\n")
    for row in rows:
        for addon in addons:
            row = row.replace(addon, "", 1)
        for attribute in attributes:
            if attribute in row:
                response[attribute] = " ".join(re.sub(' +', ' ',row).split(" ")[2::])

                
    return MusicMetadata(**response)
