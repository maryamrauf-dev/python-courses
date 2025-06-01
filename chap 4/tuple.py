z=(2,2,2,2,2,3,6)
print(z)
print(z[0])#access the element of the tuple

print(z.count(2))#count the number of times the element is present in the tuple

print(z.index(2))#return the index of the element
#as it found the first element it will return the index of the first element and will not search for the next element

#z[0]=100
#tuple is immutable so we can not change the element of the tuple
#it will give error

print(len(z))
#return the length of the tuple

print(max(z))
#return the maximum element of the tuple

print(min(z))
#return the minimum element of the tuple

print(sum(z))
#return the sum of the tuple

x=[2,4,5]
y=print(tuple(x))
#convert the list to tuple

