from pydantic import BaseModel


class RGBColor(BaseModel):
    red: int
    green: int
    blue: int
