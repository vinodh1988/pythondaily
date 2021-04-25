
def eligible(x):
    if x['age']>60:
        return True
    else:
        return False


data=[
    {"sno":1,"name":"Vivek","age":40},
    {"sno":2,"name":"Arman","age":70},
    {"sno":3,"name":"Nikhil","age":30},
    {"sno":4,"name":"Shaw","age":40},
    {"sno":5,"name":"Jagan","age":67},
    {"sno":6,"name":"Cary","age":80}
]

result=filter(eligible,data)
result2=filter( lambda x: True if x['age']<60 else False,data)

print(result)
for x in result:
    print(x)

print("------------------------------")
for x in result2:
    print(x)    