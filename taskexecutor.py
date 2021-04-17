
tasks = ("Procurement", "Quality Checking" , "Preperation", "Production","Packaging","Marketing","Dispatching")

#Generally library creator will create a function with callback
def process(task,taskname):
    if(taskname=="Procurement"):
        print("Alloting budget")
        task("Products list", "Procuring....")
    elif(taskname=="Quality Checking"):
        print("Initiating Quality assesment")
        task("Quality Metrics","Analysing....")
    else:
        print("Task Initiated")
        task(taskname, "Performing ....")
    print("task completed")

#application programmer will come up with his business logic while passing the callback
def dotask(task, action):
    print(action, task)

for x in tasks:
    process(dotask,x)