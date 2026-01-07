# for i in range(2 , 21):
#     with open(f"table.txt {i}", "w")as t:
#          for j in range(1, 11):
#             res = i * j
#             if j != 10:
#                 t.write(f"{i} x {j} = {res}\n")  
#             else:
#                 t.write(f"{i} x {j} ={res}")


# with open("table.txt", "r")as fault:
#     pick = fault.read()
# pick = pick.replace("lol useless" , "$$$#####")
# with open("table.txt", "w")as fault:
#     fault.write(pick)


# def game(s):
#     return s
# new_score = game(100000)
# with open('score.txt','r')as f:
#     old_score = f.readline()
# with open('score.txt','w')as f:
#     if old_score == 0 :
#         f.write(f'The new Hi-score is {new_score}')
#     elif old_score < str(new_score):
#         f.write(f'The new Hi-score is {new_score}')
        
#Repeat such a censored word
# li = ['hey','come on', 'lets play','call me']
# for i in range(1,len(li)+1):
#     with open(f"pop.txt", "+a")as q:
#         for j in li:
#             q.write(f'{j} \n')
    

# file = open("log.txt",'w')
# file.write("Python is most popular programming language.")
# file.close()
# with open("log.txt", 'r')as file:
#     re = file.read()
# if "Python" in re:
#     print("Yes! the word 'Python' present in log file.")
# else:
#     print("No! the word 'Python not present in log file.")

# i = 1
# with open("Detect.txt", 'r')as f:
#     while True:
#         caught = f.readline()
#         if caught == '':  # this handling empty string...
#             break   
#         elif 'python' in caught.lower():
#             print(f"The word 'Python' present on {i} line. ")
#         else:
#             print(f"The word 'Python' not present on {i} line.")  
        
#         i += 1

