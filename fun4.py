#closures
#function within a function

def outer(a):
    b=34
    def process(x): #inner function can access outer function content and vice versa is not true
        print('processing ',a,b)
        c=a+b+x
        return c
  
    return(process(100))

print(outer(90))
        
    
    #() - tuple
    #[] - list
    #{} - set
    #{}  - dictionary