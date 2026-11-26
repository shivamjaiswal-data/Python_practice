try:
    num = int(input("Enter Your number: "))
    res = 100 / num
    print("Result:", res)

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("You cannot divide a number by zero")

else:
    print("Program executed succesfully")

finally:
    print("Program Executed Successfully")

