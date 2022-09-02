from typing import Optional

import strawberry


@strawberry.type
class LightCapabilities:
    id: Optional[str]
    model: Optional[str]
    fw_ver: Optional[str]
    support: Optional[str]
    power: Optional[bool]
    bright: Optional[int]
    color_mode: Optional[str]
    ct: Optional[int]
    rgb: Optional[str]
    hue: Optional[int]
    sat: Optional[int]
    name: Optional[str]


@strawberry.type
class LightInformations:
    ip: Optional[str]
    port: Optional[float]
    capabilities: Optional[LightCapabilities]
