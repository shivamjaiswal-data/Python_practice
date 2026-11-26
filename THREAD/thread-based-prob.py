# Creating a Thrrad : Thread and Target 


import threading 

def greet():
    print("Hello from the Thread ")
t1  = threading.Thread(target = greet)

t1.start()
print("Main Program continues")
