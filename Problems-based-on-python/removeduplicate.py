def removedpct(number):
    result = []
    for num in number:
        if num not in result :
            result.append(num)
    return result
print(removedpct([1,1,2,2,3,3,44.5,6,7]))

