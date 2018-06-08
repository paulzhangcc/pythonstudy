from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time
import os
def tick():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick,"interval", seconds=3)
    scheduler.start()
    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()