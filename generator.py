def even_num():
    n = 1
    while True:
        if n%2==0:
            yield n
        n +=1

n = even_num()
for _ in range(1, 21):
    print(next(n))