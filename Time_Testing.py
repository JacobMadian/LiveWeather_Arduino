import datetime
import time

current = 0

while True:
    time.sleep(5)
    if datetime.datetime.now().hour != current:
        print('new minute')
        current = datetime.datetime.now().hour