a="""this is wonderful.
let us explore
"""

print(a)
print(a.capitalize())
print(a.upper())
print(a.find("wonderful"))
print(a.find("adverb"))
print(a[1].isalpha())
print(a[4].isspace())

mylist=a.split()
mylist2=a.split(".")

print(mylist)
print(mylist2)
