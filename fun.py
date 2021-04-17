#function parts
# 1.name
# 2. parameters  , its optional ,parameters will not have type specification
# 3. Return type
# python we dont specify return type yet a function can return values
# python doesnot support function overloading

def funone():
    print('function running')

def funone():
    print('function running more')

def funone(a):
    print("running",a)

funone(5409)
funone("Ram")
print(funone(67))