def square(a):
    return a*a

def cube(a):
    return a*a*a

def factorial(a):
    if(n==0):
        return 1
    return a*factorial(a-1)

def power(a,b):
    result=1
    times=1
    while(times<=b):
        result*=a
        times+=1
    return result