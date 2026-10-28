def countfreque(text):
    freque = {}
    for char in text.lower() :
        if char in freque:
            freque[char]+=1
        else :
            freque[char]=1
    for key ,val in freque.items():
        print(key ,":", val)
print(countfreque("Bananab"))