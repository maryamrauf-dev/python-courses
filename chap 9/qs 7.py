with open("log.txt","r") as f:
    m=f.readlines()
    line=1
    for i in m:
        if "python" in i:
            print(f"yes the word python is in your line {line}")
            break
        line+=1
        
    else:
        print("no python is not present")
    
