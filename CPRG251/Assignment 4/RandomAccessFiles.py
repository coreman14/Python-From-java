with open("bonnie.txt","wb+") as f:
    f.write(b"My Bonnie lies over the ocean.")

with open("bonnie.txt","rb+") as f:
    print(f.read(9))
    print(f.read())