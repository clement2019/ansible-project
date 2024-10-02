import os
if os.path.exists("emptyfolder.txt"):
    print("file exist")
    #os.rmdir("emptyfolder1")   
if os.remove("emptyfolder.txt"):
    
    print("file removed")
else:
    print("file not removed")
    
