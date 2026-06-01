# 're' -> This Module is stands for Regural Expression and it use for search, matche and extact patterns from string 

# """
# | Task                      | Function       | Example                                                           |
# | ------------------------- | -------------- | ----------------------------------------------------------------- |
# | Check if a pattern exists | `re.search()`  | `re.search(r"cat", "A cat is here")`                              |
# | Find all matches          | `re.findall()` | `re.findall(r"\d+", "My age is 23 and his is 45") → ['23', '45']` |
# | Replace text              | `re.sub()`     | `re.sub(r"apple", "orange", "apple pie") → 'orange pie'`          |
# | Split by pattern          | `re.split()`   | `re.split(r"\s+", "Split by spaces") → ['Split', 'by', 'spaces']` |

# """

import re
a = 'Active log is 404//error'
print(re.search(r'Active',a))   #output: <re.Match object; span=(0, 6), match='Active'>

print(re.findall(r'4',a))  #Individually find at every index  output: 

print(re.sub(r'404','***',a))

print(re.split(r's+',a))
