
# in filter if x is the size of the input and result size would <=x

#in map if x is the size of the input the result size would alse be a result#
# takes each element as input and produce output for each element

def eligible(x):
    if x['age']>50:
        return {**x, "eligibility":"eligible"}
      #  x['eligibility']='Eligible to be vaccinated'
      
    else:
        return {**x, "eligibility":"not eligible"}
    

data=[
    {"sno":1,"name":"Vivek","age":40},
    {"sno":2,"name":"Arman","age":70},
    {"sno":3,"name":"Nikhil","age":30},
    {"sno":4,"name":"Shaw","age":40},
    {"sno":5,"name":"Jagan","age":67},
    {"sno":6,"name":"Cary","age":80}
]

result =map(eligible,data)
result2 = map(lambda x: {**x,"eligibiliy":"Eligible"} if x['age']>50 else {**x,"eligibility":"Not eligible"},data)

for x in result:
    print(x)

print("-----------------------------")
for x in result2:
    print(x)