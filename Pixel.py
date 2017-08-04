class Pixel():
    def __init__(self, red=0, green=0, blue=0, brightness=256):
        self.red = red
        self.green = green
        self.blue = blue
        self.brightness = brightness

    def __str__(self):
        return ",".join([self.red.__str__(), self.green.__str__(), self.blue.__str__(), self.brightness.__str__()])