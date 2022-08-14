from typing import List

from fastapi import APIRouter, Query
from models import bulb as BulbModels
from yeelight import Bulb, discover_bulbs

router = APIRouter()


def get_list_of_bulbs(ips):
    if ips is None:
        bulbs = discover_bulbs()
        ips = [bulb["ip"] for bulb in bulbs]
    return [Bulb(ip) for ip in ips]


@router.get("")
def discover_all_bulbs():
    return discover_bulbs()


@router.post("/turn_on")
def bulb_turn_on(
    ips: List[int] = Query(None), effect: str = "sudden", duration: int = 0
):
    bulbs = get_list_of_bulbs(ips)
    return [bulb.turn_on(effect=effect, duration=duration) for bulb in bulbs]


@router.post("/turn_off")
def bulb_turn_off(
    ips: List[int] = Query(None), effect: str = "sudden", duration: int = 0
):
    bulbs = get_list_of_bulbs(ips)

    return [bulb.turn_off(effect=effect, duration=duration) for bulb in bulbs]


@router.post("/set_brigthenes")
def bulb_set_brightness(level: int, ips: List[int] = Query(None)):
    bulbs = get_list_of_bulbs(ips)

    return [bulb.set_brightness(level) for bulb in bulbs]


@router.post("/set_color")
def bulb_set_color(color: BulbModels.RGBColor, ips: List[int] = Query(None)):
    bulbs = get_list_of_bulbs(ips)

    return [bulb.set_rgb(**color.dict()) for bulb in bulbs]


@router.post("/test")
def test(temp: int, ips: List[int] = Query(None)):
    """
    1700-6500
    """
    bulbs = get_list_of_bulbs(ips)

    return [bulb.get_capabilities() for bulb in bulbs]
