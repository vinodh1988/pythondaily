
def fun():
    print("this function is working")

#callback functions
#a function which is passed as parameter to another function is what we call callback function
def funny(callme):
    print('job has been started')
    callme("Rahul")
    print('job proceeding')
    callme("Jonathan")
    print("Job Ends")


def process(n):
    print('processing ',n)

funny(process)


