fruits=["banana","mango",1,2.34,None,"maryam"]
print(fruits[1])

print(fruits[2:6])
print(fruits[1:6:2])
x=[1,34,65,75,3,2,5,32,55,224,5234]
x.sort()#sort the list and will return none because it will change the original list 
#aghar ham yahan print lagain to yeh none return kary gha q k orognal list change hoghi na k yeh 
print(x)#list are mutable so it will change the original list

x.reverse()
print(x)#sort the list in reverse order

x.append(9000)
print(x)#add the element at the end of the list

x.count(225)
print(x.count(2))#count the number of times the element is present in the list

x.insert(2,"maryam")
print(x)#insert the element at the given index

x.remove("maryam")
print(x)#remove the element from the list

x.pop(0)
print(x)#remove the element from the given index

x.clear()
print(x)#remove all the elements from the list

x=[1,34,65,75,3,2,5,32,55,224,5234]
y=x.copy()
print(y)#copy the list to y 

z=x
print(z)#copy the list to z

x[0]=100
print(x)#change the element of the list at index 0
print(y)#it will not change because it is the copy of x

x.extend([3,10])
print(x)#add the element at the end of the list

x.index(10)
print(x.index(10))#return the index of the element

print(max(x))
#return the maximum element of the list

print(min(x))
#return the minimum element of the list

print(sum(x))
#return the sum of the list
