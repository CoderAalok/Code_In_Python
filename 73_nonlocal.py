# # without nonlocal keyword
# def outer(y):
#     x = y
#     def inner():
#         x = 10
#         print(f"Inner: {x}")
#     inner()
#     print(f"Outer: {x}")

# outer(5)

# with nonlocal keyword 
def outer(y):
    x = y
    def inner():
        nonlocal x #Read and modify
        x *= 10
        print(f"Inner: {x}")
    inner()
    print(f"Outer: {x}")

outer(5)

