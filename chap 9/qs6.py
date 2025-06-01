with open("log.txt","r") as f:
    m=f.read()
    if "python" in m:
        print("yes the word python is in your string")
    else:
        print("no python is not present")
