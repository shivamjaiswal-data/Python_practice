# def gem_demo():
#     yield "First Statement"
#     yield "Second Statement"
#     yield "Third Statement"

# gen  = gem_demo()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

def gem_demo():
    yield "First Statement"
    yield "Second Statement"
    yield "Third Statement"

gen  = gem_demo()
# print(gen)

for i in gen :
    print(i)

