import os

folders = os.listdir("data")
print("Before changing directory:", os.getcwd())
os.chdir("data")
print("After changing directory:", os.getcwd())

for folder in folders:
    print(os.listdir(folder))
