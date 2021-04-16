#key no duplicates
#value can have duplicates

mydict={
  "sno": 1,
  "name":"Rahul",
  "city":"Chennai",
  "sno":3
}

mydict['skills']=['java','c++','SQL']
print(mydict)

print(mydict['skills'])
print(mydict['skills'][1])
print(mydict.keys())

for x in mydict.keys():
    print(x, mydict[x])