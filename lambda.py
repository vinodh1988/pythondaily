
def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def status(age):
    if(age>=21):
        return "Approved"
    else:
        return "Rejected"

print(add(354,345))
print(mul(34,356))
print(status(42))

sum=lambda x,y:x+y

product=lambda x,y:x*y

status2=lambda age:"Approved" if age>=21 else "Rejected" 

print(sum(354,345))
print(product(34,356))
print(status2(42))