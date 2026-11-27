# Write a generator that yields all even numbers from 1 to a user-provided limit.

def evennum(num):
    for i in range(1,num):
       if i %2 == 0 :
           yield i 

even = evennum(10)
for even in even:
 print(even)