def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)
n=int(input("enter a no:"))
print(f"fatorila of no is {factorial(n)}")