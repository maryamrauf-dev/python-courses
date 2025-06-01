def maryam(i):
    #match is same as switch in c 
    match i:
        case 1:
            print("hi")
        case 2:
            print("hello")
        case 3:
            print("greeting")
        case _: #this is same as default case
            print("enter right choice")

i=int(input("your number:"))

maryam(i)