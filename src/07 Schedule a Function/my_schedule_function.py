from datetime import datetime, timedelta
import time


def schedule_function(wait, function, *args):
  now = datetime.now()
  schedule = now + timedelta(seconds=wait)
  print(f"*** {function.__name__}() scheduled for {schedule} ***")

  time.sleep(wait)
  print(*args)

if __name__ == "__main__":
  schedule_function(5, print, "Hello")
