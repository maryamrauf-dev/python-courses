
n=int(input("enter a number:"))
table=[n*i for i in range(1,11)]
try:    
    with open ("tables.txt","w") as f:
        f.write(str (table) + "\n")
        print("table written in file successfully")
except Exception as e:
    print(e)
