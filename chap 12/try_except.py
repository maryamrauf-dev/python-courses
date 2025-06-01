try:
    n=int(input("enter number:"))
    print(n)
except Exception as e:
    print(e)
    #help in avoiding program crashing 
    #if there is any invalid input by user t will not give error instead pint messge
    #there are specific eeror also
    #e.g  
except ValueError as v:
    print(v)
except ZeroDivisionError as v:
    print(v)