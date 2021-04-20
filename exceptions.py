
try:
    a=input("enter a number:: ")
    n=int(a)
    a=input("enter another number:: ")
    n1=int(a)
    print("number n is",n)
    print('division is',n/n1)
except ValueError as e:
    print(e)
    print('enter right integer')
except Exception as e:
    print(e)
    print('some problem occored')
else:
    print('will work only if no exception ')
finally:
    print('regardless of anything will always execute')

print('after statements to execute')
