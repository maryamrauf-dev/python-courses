#using walrus operator
if(n :=len([2,3,4,3,3]))>3:
    print(f"The length of list is {n} elements which is to long. \nExpected n<=3.")
