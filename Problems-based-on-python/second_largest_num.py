num = [10,20,30,40,50]
largest = float('-inf')
second = float('-inf')
for i in num :
    if i > largest:
        second = largest
        largest = i 
    elif i > second and i != largest:
        second = i
print(second)