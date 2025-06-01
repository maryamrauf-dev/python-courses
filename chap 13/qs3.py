l=[45,75,3,12,25,10,90,23]
def div(n):
    if (n%5==0):
        return True
    return False
result=filter(div,l)
print(list(result))