from functools import reduce
l=[32,42,12,34,12,56,43,433]
def max(n,x):
    if (n>x):
        return n
    return x
result=reduce(max,l)
print(result)