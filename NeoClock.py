from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
import atexit
from Pixel import Pixel

app = Flask(__name__)

framebuffer = [[Pixel(64, 128, 196, 255) for y in range(8)] for x in range(32)]

print framebuffer[0][0].__str__()

@app.route('/')
def hello_world():
    return framebuffer.__str__()


def LED_refresh():
    print time.strftime("%A, %d. %B %Y %I:%M:%S %p")


scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=LED_refresh,
    trigger=IntervalTrigger(seconds=1./20),
    id='LED_refresh',
    name='Update the internal framebuffer to the LEDs',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    app.run()

