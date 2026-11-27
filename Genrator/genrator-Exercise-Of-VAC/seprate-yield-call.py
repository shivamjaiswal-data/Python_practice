# Create a generator that yields the numbers 10, 20, 30, 40, and 50 using separate yield statements.
#  Retrieve the values using next()
def gen():
    yield 40
    yield 50
    yield 60
    yield 70

# greet = gen()
# for i in greet:
#     print(i)

# print(next(gen()))
print(gen())