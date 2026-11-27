# def outer(func):
#     def inner(*args):
#         print("Code has started")
#         res =func(*args)
#         print("Code has Succesfully Ended")
#         return res 
#     return inner 
# @outer

# def fact(n):
#     if n <= 1:
#          return 1
#     return n*fact(n-1)


# print(fact(5))



def outer(func):
    def inner(*args):
        print("Code has started")

        res = func(*args)

        print(res)

        print("Code has successfully ended")

        return res

    return inner


@outer
def fact(n):

    def calculate(n):
        if n <= 1:
            return 1

        return n * calculate(n - 1)

    return calculate(n)


fact(5)




