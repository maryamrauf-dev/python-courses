n=int(input("enter n:"))
for i in range(1,2*n,2):
    print(" "*((2*n-i)//2),end="")
    print("*"*i,end="")
    print("")

    '''
      *
     ***
    *****
=
    '''