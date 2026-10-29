def is_palindrome(n):

    original = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev* 10 + dig
        n = n //10
    return original == rev

print(is_palindrome(125))