def gen():
    x= "python"
    for i in x:
        yield i 
greet = gen()
print(next(greet))
print(next(greet))
print(next(greet))
print(next(greet))


# greet = greet()
for i in greet:
    print(i)