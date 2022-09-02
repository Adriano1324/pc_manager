from cgitb import reset

import strawberry


@strawberry.input
class RGBInput:
    red: int
    green: int
    blue: int
