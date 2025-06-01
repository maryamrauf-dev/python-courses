from functools import reduce
l=[6,5,4]
square=lambda x:x*x
#map(function,list)
sqlist=map(square,l)
print(list(sqlist))

#filter function example
def even(n):
    if(n%2==0):
        return True
    return False
#filter(function,list)
onlyeven=filter(even,l)
print(list(onlyeven))

sum=lambda a,b:a+b
#reduce(function,list)
#l=[6,5,4]
#so reduce will work like 6+5=11 and then 11+4=15 and return 15
print(reduce(sum,l))
