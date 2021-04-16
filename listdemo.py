mylist=[123,1234,23,45,35,56,467,7546,"Parry","Larry"]

print(mylist)
print(mylist[3])
print(mylist[3:7]) #slicing element 4 to 7
print(mylist[3:]) # element four to last
print(mylist[:5]) # until 5th element
print(mylist[::2]) #first to last in step of 2
print(mylist[1:8:2]) # second to eight in step of 2
print(mylist[::-1]) # from last to first
print(mylist[9:2:-2]) # from 10th to 3rd in reverse

for x in reversed(mylist):
    print(x,"length->",len(str(x)),end=", ")
    

print("\n",len(mylist))
mylist.insert(3,"Gary")
mylist.remove(467)

print(mylist)
del mylist[4:8]
print(mylist)
mylist.extend([34,534,"Jerry"])
print(mylist)
mylist.append([34,34,364])
print(mylist)
print(mylist[9])
print(mylist[9][2])