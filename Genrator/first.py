
# In this it will Only take few amount of memory not much 

x  =  range (100000)
# for i in x :
#     print (i**2)



#  in List what we are going to do it will take more memory 
l = [x for x in range(10000)]
for i in l :
    print(i**2)
import sys
print(sys.getsizeof(l))