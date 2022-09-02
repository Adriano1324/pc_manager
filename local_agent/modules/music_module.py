import subprocess
from typing import List, Optional

import strawberry

from gql_types.music.music_information import MusicInformationResponse
from gql_types.music.player_type import Player
from utils.format import get_metadata_for_player
from utils.playerctl import base_playerctl_operation


@strawberry.type
class Query:
    @strawberry.field
    def list_actual_players(self) -> List[Player]:
        players = subprocess.getoutput("playerctl -l").split("\n")
        return [Player(player) for player in players]

    @strawberry.field
    def get_metadata(self, player: str = None) -> List[MusicInformationResponse]:
        if not player:
            player = subprocess.getoutput("playerctl -l").split("\n")
        return get_metadata_for_player(player)

    @strawberry.field
    def get_position(player: str) -> float:
        return float(subprocess.getoutput(f"playerctl -p {player} position"))


@strawberry.type
class Mutation:
    @strawberry.mutation
    def music_update(
        operation: str, value: Optional[str] = None, player: Optional[str] = None
    ) -> List[MusicInformationResponse]:
        """
        Shuffle can be "On", "Off", or "Toggle".
        Can be "None", "Track", or "Playlist".
        """
        return base_playerctl_operation(operation.replace("_", "-"), player, value)
