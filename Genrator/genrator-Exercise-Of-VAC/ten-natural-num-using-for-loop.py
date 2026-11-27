def mera_range(*args ):
    for i in range (args[0],args[1],args[2]):
        yield i 

greet = mera_range(10, 0,-1)
for i in greet:
    print(i)