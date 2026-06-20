#Maximum frequency character (maximum times appears no.)
#method=I
from collections import Counter  # count no. of characters appears in string
strr ='Greekforgreeks'
count = Counter(strr)
#method-1
max_count = max(count, key = count.get)  #maximum appearing character
print(max_count)


#method-2
max_freq = max(count.values())
re = [char for char, freq in count.items() if freq == max_freq]
print(f"Here the maximum frequency character -> {re}\n")


strr = "The most expensive in this world is our skill with knowledge".lower()
least = {}  #stored each character with it's appearing time
print(least)

for ch in strr:
    if ch == ' ':  #skip spaces
        continue
    val_ch = strr.count(ch)   
    if ch not in least :   
        least[ch] = val_ch
size = max(least.values())  #Maximum frequency length of character
result = [k for k ,v in least.items() if v == size ]
print(f"Here the maximum frequency characters -> {result}")


least = ''.join(dict.fromkeys(strr)) #:Makes a dictionary and pick unique character,
# on it iterable fromat cause join method used 

