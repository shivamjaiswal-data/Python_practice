def sumeven(numbers):
    total = 0 
    for i in numbers :
        if i%2 == 0 :
            total += i
    return total
print(sumeven([2,4,3,6,8,19]))