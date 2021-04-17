
def one(p=403):
    print(p)

def sum(a,b=0,c=0):
    return a+b+c

def mul(a,b=1):
    return a*b

one()
one(9054)
one("Gary")
one([343,534,3566])

print(sum(1))
print(sum(4356))
print(sum(1,2))
print(sum(1,23,54))
print(sum(23,c=90)) #keyword parameters
print(mul(35))