from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
import atexit

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

def LED_refresh():
    print time.strftime("%A, %d. %B %Y %I:%M:%S %p")


scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=LED_refresh,
    trigger=IntervalTrigger(seconds=1./5),
    id='LED_refresh',
    name='Update the internal framebuffer to the LEDs',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run()

