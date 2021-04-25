
file = open("e:/fun.js", "r")  
print(file.read())
print("-----------------------------------------------")


"""
r- reading
w- writing
a- appending
"""

file = open("e:/textfile.txt","a+")
while True:
    sentence=input("enter the sentence \n")
    file.write(sentence)    
    if(sentence=="end"):
        break; 

file.close()
