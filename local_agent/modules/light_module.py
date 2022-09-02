from typing import List, Optional

import strawberry
from fastapi import APIRouter
from yeelight import Bulb, discover_bulbs

from gql_types.light.light_information import (LightCapabilities,
                                               LightInformations)
from gql_types.light.rgb_input import RGBInput
from utils.y_to_rgb import yeeight_color_to_rgb

router = APIRouter()


def get_list_of_bulbs(ips):
    if ips is None or ips == []:
        bulbs = discover_bulbs(timeout=6)
        ips = [bulb["ip"] for bulb in bulbs]
    return [Bulb(ip) for ip in ips]


@strawberry.type
class Query:
    @strawberry.field
    def discover_all_bulbs() -> List[LightInformations]:
        bulbs = discover_bulbs(timeout=6)
        bulbs = sorted(bulbs, key=lambda d: d["ip"])
        return [
            LightInformations(
                ip=bulb.get("ip"),
                port=bulb.get("port"),
                capabilities=LightCapabilities(
                    id=bulb["capabilities"].get("id"),
                    model=bulb["capabilities"].get("model"),
                    fw_ver=bulb["capabilities"].get("fw_ver"),
                    support=bulb["capabilities"].get("support"),
                    power=True if bulb["capabilities"].get("power") == "on" else False,
                    bright=bulb["capabilities"].get("bright"),
                    color_mode=bulb["capabilities"].get("color_mode"),
                    ct=bulb["capabilities"].get("ct"),
                    rgb=yeeight_color_to_rgb(bulb["capabilities"]["rgb"]),
                    hue=bulb["capabilities"].get("hue"),
                    sat=bulb["capabilities"].get("sat"),
                    name=bulb["capabilities"].get("name"),
                ),
            )
            for bulb in bulbs
        ]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def bulb_turn_on(
        ips: Optional[List[str]],
        effect: Optional[str] = "sudden",
        duration: Optional[int] = 0,
    ) -> list[str]:
        bulbs = get_list_of_bulbs(ips)
        return [bulb.turn_on(effect=effect, duration=duration) for bulb in bulbs]

    @strawberry.mutation
    def bulb_turn_off(
        ips: Optional[List[str]],
        effect: Optional[str] = "sudden",
        duration: Optional[int] = 0,
    ) -> list[str]:
        bulbs = get_list_of_bulbs(ips)

        return [bulb.turn_off(effect=effect, duration=duration) for bulb in bulbs]

    @strawberry.mutation
    def bulb_set_brightness(level: int, ips: Optional[List[str]]) -> list[str]:
        bulbs = get_list_of_bulbs(ips)

        return [bulb.set_brightness(level) for bulb in bulbs]

    @strawberry.mutation
    def bulb_set_color(color: RGBInput, ips: Optional[List[str]]) -> list[str]:
        bulbs = get_list_of_bulbs(ips)

        return [bulb.set_rgb(color.red, color.green, color.blue) for bulb in bulbs]
