import os
with open("log.txt","w") as f:
    f.write("hi")
os.rename("log.txt","rename by python.txt")
# import os

# # Create and write to the file
# with open("donkey.txt", "w") as f:
#     f.write("This is a test file.")

# # Rename the file
# os.rename("donkey.txt", "rename by python.txt")