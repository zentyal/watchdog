import sys
import time
import watchdog
import watchdog.events

import logging
logging.basicConfig(level=logging.DEBUG)

class MyEventHandler(watchdog.events.PatternMatchingEventHandler):
    def on_any_event(self, event):
        logging.debug(event)

event_handler = MyEventHandler(patterns=['*.py', '*.pyc'],
                                ignore_patterns=['version.py'],
                                ignore_directories=True)
observer = watchdog.Observer()
observer.schedule('a-unique-name', event_handler, recursive=True, sys.argv[1:])
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.unschedule('a-unique-name')
    observer.stop()
observer.join()

