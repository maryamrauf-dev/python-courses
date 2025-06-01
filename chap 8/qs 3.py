def sum(n):
    if (n==1):#base condition to prevent infinite recurssion
    
        return 1
    

    return n+sum(n-1)

a=int(input("enter number:"))
print(f"SUM of first {a} natural number is:")
print(sum(a))