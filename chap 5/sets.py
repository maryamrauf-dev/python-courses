s={6,8,1,2,3,3,4}
#set conatin only values
e=set()
#empty set is created is s{} use it is empty dictionary

print(s)#only take 3 one time we can't repeat elements in set
#oder change in sets

s.add(90)
print(s)#90 is added to the set

s.discard(53)#will give no error if element is not present
#if present it is removed from set
print(s)

# s.remove(53)#will give error if element is not present
# #if present it is removed from set
# print(s)

# s.clear()#clear all elements from set
# print(s)

print(len(s))#will return set lenght here it will return 0 bcz set is clear

n={5,7,87,4,6}
print(s.union(n))
print(s.intersection(n))
print(s.difference(n))
print(n.difference(s))
e={1,2}
print(e.issubset(s))
print(s.issuperset({1,2}))
print({1,2}.issubset(s))