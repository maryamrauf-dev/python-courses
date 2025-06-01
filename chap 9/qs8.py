with open("donkey.txt","r") as f:
    content=f.read()

with open("copydonkey.txt","w") as f:
    f.write(content)

