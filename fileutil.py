# importing os module  
import os 
  
# importing shutil module  
import shutil 
  
  
# Source path 
source = "e:/jsonfile.json"
  
# Destination path 
destination = "f:/"

  
# Copy the content of 
# source to destination 
dest = shutil.copy(source, destination) 

  
# List files and directories 
# in "/home / User / Desktop" 
print("After copying file:") 
print(os.listdir("f:/Exceptions")) 


  
# Print path of newly  
# created file 
print("Destination path:", dest) 