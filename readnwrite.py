import os
os.getcwd()
os.makedirs("./data",exist_ok=True)
os.chdir("/content/data")

os.getcwd()
# create a new file inside data
with open("myfile.txt", "w") as f:
    f.write("Hello, this is a test file inside data directory!")

print("File created:", os.path.join(os.getcwd(), "myfile.txt"))
with open("myfile.txt", "r") as k:
  print(k.read())
  !ls /content/data
