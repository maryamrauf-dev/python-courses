# f=open("mary.txt")
# print(f.read())
# f.close()

#same can be written using with statement
with open("mary.txt") as f:
    print(f.read())

#you dont need to explicitly close the file