f = open("text.txt")
data = f.read()
print(data)
f.close()
# try:
#     f = open("text.txt", "r")
#     print("file opened")
#     data = f.read()
#     print(data)
#     f.close()
# except FileNotFoundError:
#     print("The file 'text.txt' does not exist.")