
def nsum(*params):
    sum=0
    for x in params:
        sum+=x
    return sum


print(nsum(43,564,234,3,534,34,34,23,23,2534,123))
print(nsum(12,234))
print(nsum())
print(nsum(34,35,365))

take= lambda *x:print(x)

take(23,2345423,23232,54234,324)