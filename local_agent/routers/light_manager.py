from fastapi import APIRouter
from yeelight import discover_bulbs, Bulb
from typing import Optional

router = APIRouter()

@router.get("")
def discover_all_bulbs():
    return discover_bulbs()

@router.post("/turn_on")
def bulb_turn_on(ip:str = None):
    if not ip:
        bulbs = discover_bulbs()
        for bulb in bulbs:
            bulb = Bulb(bulb["ip"])
            bulb.turn_on()
        return "turning on all lights"
    bulb = Bulb(ip)
    return bulb.turn_on()

@router.post("/turn_off")
def bulb_turn_off(ip:str = None):
    if not ip:
        bulbs = discover_bulbs()
        for bulb in bulbs:
            bulb = Bulb(bulb["ip"])
            bulb.turn_off()
        return "turning off all lights"
    bulb = Bulb(ip)
    return bulb.turn_off()
    