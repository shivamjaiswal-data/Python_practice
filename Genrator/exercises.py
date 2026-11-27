sqr  =  (i**2 for i in range(1,100))

# for i in sqr:
#     print(i)

# print(next(sqr))



def mera_range (args,krgs):
    for i in range(args,krgs):
        yield (f" Squar of {i} is Equal to {i** 2}") 

mara = mera_range(10,20)
print(next(mara))