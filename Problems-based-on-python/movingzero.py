def moving_zero(numbers):
    result = []
    for num in numbers :
        if num != 0:
            result.append(num)
    
    zero_count = len(numbers) - len(result)

    result.extend([0] * zero_count)

    return result
print(moving_zero([1,0,5,6,7,0,7,0]))