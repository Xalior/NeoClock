from flask import Flask
import time
import thread

from neopixel import *

# LED strip configuration:
LED_COUNT      = 256     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 25     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

app = Flask(__name__)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions with automatic shifting for Out of Band inputs."""
    while pos > 255:
        pos = pos - 255
    while pos < 0:
        pos = pos + 255
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def blank(colour):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, colour)


def refresh():
    print time.strftime("%A, %d. %B %Y %I:%M:%S %p")


def main():
    while True:
        refresh()
        time.sleep(0.1)
        strip.show()


@app.route('/')
def hello_world():
    global x

    x = x * 2
    return x.__str__()

thread.start_new_thread(main, ());

thread_id = thread.start_new_thread(main, ());

if __name__ == '__main__':
    app.run(host='0.0.0.0')
