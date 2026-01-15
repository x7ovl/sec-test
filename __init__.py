import subprocess
def exp():
  command = ["sh", "-c", "id"] 
  subprocess.run (command, check=False)

if __name__ == "__main__":
  exp ()
