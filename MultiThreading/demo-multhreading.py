# def task1 ():
#     for i in range(1,6):
#         print("task 1 : ", i)

# def task2 ():
#     for i in range(1,6):
#         print("task 2 : ", i)

# task1()
# task2()


# import threading 
# import time
# def task1 ():
#     for i in range(1,6):
#         print(f"Attempt {i}  : ", i)
#     time.sleep(4)
#     print("Task 1 is completed   ")

# def task2 ():
#     for i in range(1,6):
#         print("task 2 : ", i)

# t1 = threading.Thread(target = task1)
# # t2 = threading.Thread(target = task2)
# t1.start()
# t1.join()
# t2.start()



"""
1) : - What is the Main Thread?
Whenever you run a Python program, Python automatically creates a thread called the Main Thread.
you dont need to Create it manually : 

"""
# import threading

# print("Hello")

# print(threading.current_thread().name)

# print("Welcome")


import threading 
def name ():
    print("Current thread:" ,threading.current_thread().name)
t1 =threading.Thread(target = name, name = "Student is bring Threaded")

t1.start()
t1.join()
print("main Thread" , threading.current_thread().name)

