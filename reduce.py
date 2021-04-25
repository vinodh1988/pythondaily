

#reduce takes n input and produce one output

from functools import reduce;

def fun(x,y):
    print(x,y)
    if(x>y):
        return x
    else:
        return y

data=[3435,34,3,3566,4,234224,232,23,5432,23,2345,23,254]

result = reduce(fun,data)
result1= reduce( lambda x,y: x if x>y else y,data)
print('result is',result)
print('result is',result1)
