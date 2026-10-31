def largest_digit(num):
    num = abs(num)
    largest = 0

    while num > 0:
        digit = num % 10

        if digit > largest:
            largest = digit

        num = num // 10

    return largest


print(largest_digit(58329))

