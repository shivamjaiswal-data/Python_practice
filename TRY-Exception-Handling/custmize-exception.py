class ValueError(Exception):
    pass



age = int(input("Enter a Number"))

try:
    if age < 18:
        raise ValueError("You must be more older")

except ValueError as e:
    print("Output failed:", e)

else:
    print("Access Granted")



