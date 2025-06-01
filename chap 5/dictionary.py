marks={
    "marry":90,
    "haya":54,
    "anaya":78,
    "average":[90,34,67]
}

print(marks)

print(type(marks))
print(marks["marry"])
#marry is key and 90 is value
print(marks["average"])

print(marks.items())#it will return all the items in the dictionary
print(marks.keys())#    it will return all the keys in the dictionary
print(marks.values())#it will return all the values in the dictionary
marks.update({"marry":98,"rohan":78})
#  it will update the value of key "marry" and add a new key "rohan"
print(marks)

print(marks.get("marry"))
#it will return value of key mmarry
#if key is not present it will return none
#print(marks["marry"]) is different from this in aspect that if key is not present we will get error

print(marks.pop("marry"))#will return value of key marry and remove it from dictionary
print(marks)#will return dictionary after removing key marry
print(marks.popitem())#will return value of last item and remove it from dictionary
print(marks)#will return dic after removing last key and value set