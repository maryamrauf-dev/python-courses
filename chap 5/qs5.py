# s={}
# language=input("whats your favorite language:")
# names=input("what is your name:")
# s.update({names:language})
# language=input("whats your favorite language:")
# names=input("what is your name:")
# s.update({names:language})
# language=input("whats your favorite language:")
# names=input("what is your name:")
# s.update({names:language})
# language=input("whats your favorite language:")
# names=input("what is your name:")
# s.update({names:language})
# print(s)
s={}
for i in range(4):
    names=input("whats your name:")
    lang=input("whats your fav language:")
    s.update({names:lang})

print(s)