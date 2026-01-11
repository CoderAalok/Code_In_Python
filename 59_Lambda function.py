
# # Level 1:
# # Question:1
# li = [2, 4, 6, 8]
# square = list(map(lambda x: x**2,li))
# print(square)
# # ("OR")
# square = list(map(lambda x: x*x , li))
# print(square)
# # OR 
# square = (lambda x: x**2)
# for i in li:
#     print(square(i),end=',')

# print("_"*50)

# # Question:2  (Also can solve using filter)
# n = list(range(1,11))
# even = lambda x: x%2 == 0
# for e in n:
#     print(f"Even: {even(e)}")
# # Or
# even = list(filter(lambda e: e%2 == 0,n))
# print(even)

# print("_"*50)

# # Question:3  (Also can solve using map)
# li_str = ["Python", "Lambda", "Function"]
# result = lambda c: c[-1]
# for c in li_str:
#     print(result(c))

# # Or
# char = map(lambda c: c[-1], li_str)
# print(list(char))

# # Level: 2
# # Question:4

# li = ["12", "45", "100", "8"]
# integer = map(lambda i: int(i), li)
# print(list(integer))

# print("_"*50)

# # Question:5

# nums_li = [10, 20, 30, 40]
# add = list(map(lambda a: a+5, nums_li))
# print(add)

# print("_"*50)
# # Question:6

# strr = ["alex", "bob", "charlie"]
# upper = list(map(lambda u: u.upper(), strr))
# print(upper)

# Level: 3
# Question: 7

# li_num = [3, 10, 15, 22, 31, 40, 45]
# odd = list(filter(lambda x: x%2 != 0 , li_num))
# print(odd)

# print("_"*50)

# # Question: 8
# words = ["hi", "hello", "code", "python", "AI"]

# len_word = list(filter(lambda w: len(w)>4, words))
# print(len_word)

# Level: 4
# Question: 9

# li_tup = [(3, 9), (1, 2), (5, 1), (2, 5)]
# sort_ = sorted(li_tup, key=lambda s: s[1]) #In my according it behaves like: Initially, hold every second value (9,2,1,5)->sorted them and match to re-arrange
# print(sort_)
# # Without lambda
# dic = {k[1]:k for k in li_tup }
# dic_s = sorted(dic.items())
# new_dic = dict(dic_s)
# print(list(new_dic.values()))

# print("_"*50)
# # Question: 10

# names = ["ram", "sudeep", "alok", "neeraj"]
# len_name = sorted(names, key=lambda x: len(x))
# # In my according Python interpeter execute this program like
# # first see-> 'sorted' function -> names -> see 'key' parameter (Python do compare, make desion -> see 'len'-> according to len 
# print(len_name)


# Level 5: Real-world Style
#Question: 11

# students = [
#     {"name": "Aalok", "marks": 92},
#     {"name": "Hari", "marks": 75},
#     {"name": "Sita", "marks": 88}
# ]

# mark = sorted(students, key=lambda m: m["marks"])
# print(mark)

# print("_"*50)
# # Question: 11

# gmail = ["user1@gmail.com", "test@yahoo.com", "dev@outlook.com"]

# domain = list(map(lambda x: x.split('@')[1], gmail))

# print(domain)

# print("_"*50)
# # Question: 12

# products = [
#     {
#     "item": "Keyboard",
#     "price": 300
#     },
#     {
#     "item": "Mouse",
#     "price": 150
#     },
#     {
#     "item": "Monitor",
#     "price": 700
#     },
#     {
#     "item": "SSD",
#     "price": 1200
#     }
# ]

# items = [tuple(key.values()) for key in (products)  ]
# value = [k for k,v in items]
# print(value)

# value = list(filter(lambda k: k['price']>200,products))

# product = [list(k.values())[0] for k in value]

# print(product)




# price = list(filter(lambda p: p['price']>500 , products))

# product = [list(p.values())[0] for p in price]
# print(product)

# print("_"*50)
# # Question: 13

# emp = [
#     {"name": "A", "salary": 50000},
#     {"name": "B", "salary": 75000},
#     {"name": "C", "salary": 60000},
# ]

# salary = sorted(emp, key=lambda x: x['salary'],reverse=True )
# print(salary)



# Level 6: Challenging
# Question: 15

# numbers = [2,3,4,5]
# # lambda to double
# op = list(map(lambda n: n*2,numbers))
# print(op)

# # lambda to square
# op = list(map(lambda n: n*n,numbers))
# print(op)

# # lambda to get even numbers
# op = list(filter(lambda n: n%2 == 0 ,numbers))
# print(op)

# Question: 16

# from functools import reduce
# li = [1,2,3,4,5]
# mul = reduce(lambda x,y : x*y,li)
# print(mul)

# # without lambda function
# def mul(x,y):
#     return x*y
# result = reduce(mul,li)
# print(result)


# # Question: 17
# courses = [
#     ("Python", 4),
#     ("JavaScript", 2),
#     ("C++", 3),
#     ("Go", 1)
# ]

# second_value = sorted(courses, key=lambda v: v[1])
# print(second_value)


# # Question: 18
# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Phone", "price": 800},
#     {"name": "Tablet", "price": 400},
#     {"name": "Monitor", "price": 300}
# ]
# items = list(map(lambda p: p['name'], filter(lambda p: p["price"]>500, products)))

# # product = [list(v.values())[0] for v in items]
# print(items)

# # Question: 19
# words = ["Python", "Lambda", "Function", "Code", "Developer"]

# word = sorted(filter(lambda w: len(w) >= 6, words),key=lambda w: len(w),reverse=True)[:2]
# print(word)

# # Question: 20
# students = [  
#     {"name": "Aalok", "marks": 92},
#     {"name": "Hari", "marks": 75},
#     {"name": "Sita", "marks": 88},
#     {"name": "Ramesh", "marks": 65}
# ]

# names = list(map(lambda n: n["name"], filter(lambda n: n["marks"] >= 80, students)))

# # names = [list(v.values())[0] for v in items]
# print(names)

# from functools import reduce
# products = [
#     {"name": "Laptop", "price": 1200, "rating": 4.5},
#     {"name": "Phone", "price": 800, "rating": 4.7},
#     {"name": "Tablet", "price": 400, "rating": 4.2},
#     {"name": "Monitor", "price": 300, "rating": 4.6}
# ]

# # total price
# result = reduce(lambda x,y: x+y,
#            map(lambda p: p["price"],
#                 filter(lambda p: p["price"]>= 500 and p["rating"] >= 4.5, products)
#             )
#     )

# # Sort price in decending order
# result = sorted(
#     map(lambda p: p['name'] + ":"+ str(p["price"]),
#                 filter(lambda p: p["price"]>= 500 and p["rating"] >= 4.5, products)
#     ),reverse=True
# )

# print(result)


# from functools import reduce
# products = [
#     {"name": "Laptop", "price": 700, "rating": 4.5},
#     {"name": "Phone", "price": 800, "rating": 4.7},
#     {"name": "Tablet", "price": 400, "rating": 4.2},
#     {"name": "Monitor", "price": 300, "rating": 4.6}
# ]



# # Sort by alphabetically
# price = sorted(
#     map(lambda p: f"{p['name']}: {p['price']}",   
#      filter(lambda p: p['price']>=500 and p['rating']>=4.5, products)
#     )
# )


# # Sort by numberically(price)
# price = list(
#     map(lambda p: f"{p['name']}: {p['price']}",   
#      sorted(filter(lambda p: p['price']>=500 and p['rating']>=4.5, products),
#             key=lambda p: p['price'],
#             reverse=True
#         )
#     )
# )

# total_price =  reduce(lambda x,y: x+y, 
#                 map(lambda p: p['price'], 
#                 filter(lambda p: p['price']>=500 and p['rating']>=4.5,products)
#     )
# )
# print(f"Price: {price}")
# print(f"Total Price: {total_price}")


from functools import reduce

products = [
    {"name": "Laptop", "price": 1200, "rating": 4.5, "stock": 15},
    {"name": "Phone", "price": 800, "rating": 4.7, "stock": 5},
    {"name": "Tablet", "price": 400, "rating": 4.2, "stock": 30},
    {"name": "Monitor", "price": 300, "rating": 4.6, "stock": 25},
    {"name": "Camera", "price": 90000, "rating": 4.8, "stock": 8}
]

filtered = list(filter(
    lambda p: p['price'] >= 500 and p['rating'] >= 4.5 and p['stock'] >= 8,products
    )
)

result = list(
    map(lambda p: f"{p['name']} | Price: {p['price']}| Rating: {p['rating']}",
        sorted(filtered,key=lambda x: (x['rating'] , x['price']), reverse=True 
        )
    
    )
)

total_price = reduce(lambda x,y: x+y,
    map(lambda p: p['price'],list(filtered)
    )
)



print("\n".join(result))

print(f"\nTotal Price: {total_price}")