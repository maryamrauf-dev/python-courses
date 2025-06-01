with open("donkey.txt","r") as f:
    content=f.read()

with open("copydonkey.txt","r") as f:
    copy=f.read()

if(content==copy):
    print("yes both files are identicle")
else:
    print("no files are different")