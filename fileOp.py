with open("file.txt","w") as f:
    f.write("It's Done Bro!")
with open("file.txt","r") as f:
    print(f.readline().strip())
    f.seek(5)
    print(f.read(5))