#a=[1,3,6,7,8,9,2,0,5,-7,5,7,0,1,4,7]
#print(a[2::5])

#dict={1:"Python" ,2:"C++", 3:"DSA",4:"RAG"}
#print(dict.items())
#for i in dict.items():
#    print( i )


# s = 'amaama'
# l = len(s)//2

# first_half = s[:l]
# second_half = s[l:] if len(s) %2 == 0 else s[l+1:]

# is_Symmetrical = first_half in second_half
# is_palindrom = s[::-1] == s

# if is_Symmetrical and is_palindrom:
#     print("Given string both Symmetrical and Palindrom.")
# elif is_palindrom:
#     print("Given string is Palindrom.")
# elif is_Symmetrical:
#      print("Given string is Symmetrical.")
# else:
#     print("Neither Symmetrical nor Palindrom.")

s = 'Python'
length = len(s)
rev = []
for i in range(1,length+1):
    re = s[length-i]
    rev.append(re)
for j in rev:
    print(j,end='')

    