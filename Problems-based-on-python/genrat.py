def numbers():
    yield 1
    yield 2
result = numbers()
print(next(result))
print(next(result))
