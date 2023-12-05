import os
import json
cwd = os.getcwd()

def save_dict(data, path, filename):
  if data:
    with open(path + filename, "w") as file:
      json.dump(data, file, indent=4)
  else:
    print("Dictionary is empty!")

def open_dict(path, filname):
  with open(path + filname, "r") as file:
    data = file.read()
    
    return data

if __name__ == "__main__":
  path = cwd + "/src/06 Save a Dictionary/"
  data = {
    "fname": "Shaun",
    "lname": "Cummins",
    "birthplace": "Preston"
    }
  # save_dict(data=data, path=path, filename="my_dict.json")
  print(open_dict(path=path, filname="my_dict.json"))


