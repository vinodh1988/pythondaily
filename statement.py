
myscore=int(input("enter your score ->"))
print(type(myscore))

if (myscore>90 and myscore<=100) :
    print("Excellent")
    print('The scored you entered is', myscore)
elif (myscore>75 and myscore<=90):
    print("Very Good")
    print('The scored you Given is', myscore)
elif (myscore>50 and myscore<=75):
    print("Average")
    print('The scored you Given is', myscore)
elif(myscore<=50):
    print("Failed")
    print("Score doesnt matter you failed")
else:
    print("Score should be less than 100")

#to comment we need to use Hash

#Python does not support switch statement