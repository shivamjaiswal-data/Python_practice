def countvowel(text):
    total = 0 
    for char in text:
        if char in "AEIOUaeiou":
            total = total + 1 
    return total

print(countvowel("Elephant"))