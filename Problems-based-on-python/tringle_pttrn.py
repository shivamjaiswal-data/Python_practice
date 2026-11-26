def stdpttrn (number):
    for i in range (1,number+1):
        for j in range (1, i+1):
            print(j , end="")
        print()
print(stdpttrn(5))
