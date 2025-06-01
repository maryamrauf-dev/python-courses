try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print(a/b)
except ZeroDivisionError as e:
    print("infinite")