from random import randint
import time

def waiting_game():
  seconds = randint(2, 4)
  print(f"Your taget time is {seconds} seconds.")
  start_input = input("---Press Enter to Begin---")

  if start_input == "":
    start_time = time.time()
    end_input = input("---Press Enter Again to Stop---")
  else:
    print("Press Enter to Start!")
    
  if end_input == "":
    end_time = time.time()
  else:
    print("Press Enter to Stop!")

  elapsed_time = end_time - start_time

  time_delta = seconds - elapsed_time


  print(f"Elapsed time: {elapsed_time}")
  match time_delta:
    case 0:
      print("Perfect timing!")
    case _ if time_delta < 0:
      print(f"({time_delta*(-1):.2f} seconds too slow)")
    case _ if time_delta > 0:
      print(f"({time_delta:.2f} seconds too fast)")
    case _:
      print("Something went wrong!")

waiting_game()
