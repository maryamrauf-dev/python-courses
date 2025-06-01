def pattern(n):
    if(n==0):
        return #means if function is going and return come then it stop function there
    print("*"*n)
    pattern(n-1)

n=3
pattern(n)
