from typing import Optional

import strawberry


@strawberry.type
class MusicMetadata:
    trackid: Optional[str]
    length: Optional[float]
    artUrl: Optional[str]
    album: Optional[str]
    albumArtist: Optional[str]
    artists: Optional[str]
    autoRating: Optional[str]
    discNumber: Optional[int]
    title: Optional[str]
    trackNumber: Optional[float]
    url: Optional[str]


@strawberry.type
class MusicInformationResponse:
    metadata: Optional[MusicMetadata]
    status: str
    position: Optional[str]
    volume: Optional[str]
    player: str
    loop: str
    shuffle: str
