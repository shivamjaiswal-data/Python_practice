def execute(args):
    for i in range (args,1,-1):
        yield i 

gren = execute(15)

for i in gren:
    print(i)