def table(a):
    for i in range(11):
        c = (f"{a}* {i}={a*i}")
        yield c 

greet = table(15)

for i in greet:
    print(i)



