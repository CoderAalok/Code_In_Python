#Maximum frequency character (maximum times appears no.)
#method=I
from collections import Counter  # count no. of characters appears in string
strr ='Greekforgreeks'
count = Counter(strr)
#method-1
max_count = max(count, key = count.get)  #maximum value of key count
print(max_count)
#method-2
size = max(count.values())
re = [k for k, v in count.items() if size == v]
print(f"Here the maximum frequency character -> {re}")


#method=II
strr = "The most expensive in this world is our skill with knowledge".lower()
least = {}  #stored each character with it's appearing time

print(least)

# for ch in strr:
#     if ch == ' ':  #skip spaces
#         continue
#     val_ch = strr.count(ch)   
#     if ch not in least :   
#         least[ch] = val_ch
# size = max(least.values())  #Maximum frequency length of character
# result = [k for k ,v in least.items() if v == size ]
# print(f"Here the maximum frequency characters -> {result}")


# least = ''.join(dict.fromkeys(strr)) :Makes a dictionary and pick unique character,
# on it iterable fromat cause join method used 

