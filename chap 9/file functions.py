f=open("mary.txt")
# line=f.readlines()
# #return list of lines 
# print(line,type(line))

# line=f.readline()
# print(line,end="")
# l=f.readline()
# print(l,end="")
# l=f.readline()
# print(l,end="")

line=f.readline
while(line!=""):
    print(line,end="")
    line=f.readline()

# for line in f:
#     print(line,end="")

f.close()