def spelling(word , defined_word):
   
    for i in defined_word:
        count = []
        if len(i) == len(word):
            pick = i     
            for j in range(len(word)):
                    if word[j] != pick[j]:
                        count.append(word[j])
            return count 
    return 0
    
word = input("Enter your favourit mammal name : ").strip().lower()
defined_word = ['monkey', 'leopard', 'tiger','dog','elephant',
                'yak','camel','lion','horse','rhinoceros','sheep',
                'panda','cheetah','deer']
result = spelling(word , defined_word)
print(f'There is {result} spelling you mistake.')