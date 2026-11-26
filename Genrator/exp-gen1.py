def square (num):
    for i in range (1, num+1 ):
        c = (f"Square of {i} is Equal to {i**2}")
        yield c 


gen = square(10)


print(next(gen))
print(next(gen))
print(next(gen))


for i in gen :
    print (i)

