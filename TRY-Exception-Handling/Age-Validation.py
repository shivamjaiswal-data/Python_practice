# age = 15
# if age  < 15:
#     raise ValueError("You must be 18 18 or older") 

# print("Access Granted ")



age = int(input("Enter a Number"))

try:
    if age < 18:
        raise ValueError("You must be more older")

except ValueError as e:
    print(e)

else:
    print("Access Granted")