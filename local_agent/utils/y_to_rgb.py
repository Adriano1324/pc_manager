def yeeight_color_to_rgb(color: str):
    color = int(color)
    red = int(color / 65536)
    green = int((color-red*65536)/256)
    blue = int(color-(red*65536+green*256))
    return '#%02x%02x%02x' % (red, green, blue)
