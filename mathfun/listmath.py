def sumn(n):
    if(n==0):
        return 0
    else:
        return n+sumn(n-1)
    
def muln(n):
    if(n==1):
        return 1
    else:
        return n*muln(n-1)
