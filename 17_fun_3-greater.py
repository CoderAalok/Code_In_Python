# def revome_word(string , word):
#     q = string.strip()
#     return q.replace(word , 'master_mind')
    
# string = "The most valuable things which has our skill and knowledge"
# word = 'knowledge'
# print(revome_word(string, word))

def table(n):
    for i in range(1,11):
        result = n * i
        print(f'The multiple of {n} * {i} = {result} ')
table(10)


#Celsius to Fahrenheit
# def fah(Cel):
#     q = Cel * (9/5) +32
#     return q
# print(fah(45))

#Fahrenheit to Celsius 

def cel(fah):
    z = (fah-32) * 5/9
    return z
print(cel(212))


# def greater(a,b,c):
#     result = max(a,b,c)
#     return result
#     # if a > b and a > c:
#     #     return a
#     # elif b > a and b > c:
#     #     return b
#     # else:
#     #     return c
# q = greater(5000,100,21)
# print(f'The greater number is {q}.')
