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
