def greet_per(name):
    print("Hello",name + "!")

def change_case(text):
    result =""
    for ch in text :
        if ch.isupper():
            result += ch.lower()
        elif ch.islower():
            result += ch.upper()
        else:
            result+= ch
    return result


'''
Locating Modules 
-- when importing a module ,python 


math module :- min(),max(),abs(),pow(x,y) 
'''



from mymodule import greet_person 
greet_person("Jayshree")



'''
Random Module  -- generate random num and selection 
randint(a,b)
random()
choice(seq)
shuffle(list)

'''


import random 
x = random.randint(1,20)
sun = ("pyhton","ADBMS","DSA")
mychoice = random.choice(sun)
print(mychoice)
print(x)


'''
Date time Module : - date.today()
datetime.now() 
timedelta() :- date arithmatic
'''



'''
Application of timedelta ():
in pyhton timedelta is class within a the datetime module used to represent date and time 

'''

import datetime 
print(datetime.date.today())



from datetime import datetime ,timedelta
now = datetime.noe()
fut_date = now + timedelta(days =10)
pst_date = now - timedelta(hours =5)




'''
Function programming tools 
map() transform each module 1(iterable of modified val) ,
 filter()select elements meeting a condition (iterable for filtered val),
 Rduce() combined elements in  a value 
'''

num =[1,2,3,4]
res = list(map(lambda x : x*2 ,num))
print(res)


#change to upper case 

name =["shivam" ,"priyam"]



#use of filter   
num =[1,2,3,4]
rs =list(filter(lambda x:x%2 ==0 ,num))
print(rs)


#reduce function 

from functools import reduce 

num = [1,2,3,4,5,-7]
res = reduce(lambda x ,y : x+ y ,num)

print(res)
