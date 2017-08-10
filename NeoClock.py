from flask import Flask
import time
import thread

x = 1

def LED_loop():
    global x

    while True:
        LED_refresh(x)

app = Flask(__name__)

@app.route('/')
def hello_world():
    global x

    x = x * 2
    return x.__str__()


def LED_refresh(dt):
    print time.strftime("%A, %d. %B %Y %I:%M:%S %p")
    time.sleep(0.1)

thread_id = thread.start_new_thread(LED_loop, ());

if __name__ == '__main__':
    app.run(host='0.0.0.0')
