#Find pair no. of characters from strings 
#Method_1
# s1 = 'encapsulation'
# s2 = 'abstraction'
# count = 0
# ch = []
# for i in s1:
#     if i in  s2 and i not in ch:
#         count += 1
#         ch.append(i)
# print(f"Here the pair no. of strings -> {count} and {ch}")

#Method_2
s1 = 'encapsulation'
s2 = 'abstraction'
count = set(s1)
count_ = 0
li = []
for ch in count:
    if ch in s2:
        count_ += 1
        li.append(ch)
print(count_, li)
         