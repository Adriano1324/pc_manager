from typing import Optional, Union

from pydantic import BaseModel, validator


class MusicMetadata(BaseModel):
    trackid: Optional[str]
    length: Optional[float]
    artUrl: Optional[str]
    album: Optional[str]
    albumArtist: Optional[str]
    artists: Optional[str]
    autoRating: Optional[str]
    discNumber: Optional[float]
    title: Optional[str]
    trackNumber: Optional[float]
    url: Optional[str]

    @validator("length")
    def change_to_seconds(cls, v):
        return v / 1_000_000


class MusicInformationResponse(BaseModel):
    metadata: Optional[MusicMetadata]
    status: str
    position: Optional[Union[float, str]]
    volume: Optional[Union[float, str]]
    player: str
    loop: str
    shuffle: str
