import re
import subprocess

from fastapi import HTTPException

from gql_types.music.music_information import (MusicInformationResponse,
                                               MusicMetadata)


def get_all_players():
    result = subprocess.getoutput("playerctl -l")
    if result == "No players found":
        raise HTTPException(400, "no available players")

    return result.split("\n")


def get_metadata_for_player(players=None):
    available_players = get_all_players()
    if players is None:
        players = available_players[0]
    if not isinstance(players, list):
        players = [players]
    for player in players:
        if player not in available_players:
            raise HTTPException(400, f"Player:{player} dosen't exist")
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
            shuffle=subprocess.getoutput(f"playerctl -p {player} shuffle"),
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
                response[attribute] = " ".join(re.sub(" +", " ", row).split(" ")[2::])
                attributes.remove(attribute)
                break

    length = int(response.get("length")) / 1000000
    return MusicMetadata(
        trackid=response.get("trackid"),
        length=length,
        artUrl=response.get("artUrl"),
        album=response.get("album"),
        albumArtist=response.get("albumArtist"),
        artists=response.get("artists"),
        autoRating=response.get("autoRating"),
        discNumber=response.get("discNumber"),
        title=response.get("title"),
        trackNumber=response.get("trackNumber"),
        url=response.get("url"),
    )
