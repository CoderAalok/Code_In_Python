#Snake Water Gun Game..

import random
print(" \t Welcome to Snake🐍 Water🌊 Gun🔫 Game \n ")
def Snake_Water_Gun_Game():
    while True:
        user_name = input("\t Enter your name 🧍:")
        if user_name == '' or not user_name.isalpha():
            print("\t Name is required  ") 
            continue
        content = {1:"Snake🐍", 2:"Water🌊", 3:"Gun🔫"}
        score_user = 0 
        score_bot = 0 
        i = 0
        max = 2
    
        while i < max:
            try:
                user = int(input(f"\t Select anyone number [1-3] >>> {list(content.items())} : "))
                i += 1 
                if not 1<= user <= 3:
                    print("\t The value must be under range.")
                    i -= 1
                    continue
                bot = random.randint(1,3)
                print(f"\t Canva🤖 : Siuuu!>>> {content[bot]} \n \t {user_name}🧍: Siuuuuuuu!>>> {content[user]}")
                if user == bot :
                    print("\t  It's a Draw!, So no one get point.")
                elif ( bot == 1 and user == 2) or ( bot == 2 and user == 3) or ( bot == 3 and user == 1 ):
                    print("\t Canva🤖 get +1 point. ") 
                    score_bot += 1
                else:
                    print("\t You🧍 get +1 point. ") 
                    score_user += 1
            
            except ValueError:
                print("\t Please input a correct number >[1,2,3].") 
                continue
        
        print(f"\t Final scores are 🧍: {score_user} and 🤖 : {score_bot}.")
        if score_user > score_bot:
            print(f"\t  🎉 winner 🧍{user_name}. ")
        elif score_bot == score_user:
            print(f"\t 🤝 It's a draw. ")               
        else:
            print("\t  🎉 winner Canva🤖.")
        with open("game.txt",'w')as g:
            add = g.write(f"Score : {user_name} = {score_user} \n\t  Canva = {score_bot}" )   
        
        while True:    
            again = input("\t Do you like to play once more [ YES OR NO ] : ").lower().strip()
            if again == '' or not again.isalpha():
                print("\t Input type is Empty .")
                continue
            
            if again == 'yes' :
               break #Snake_Water_Gun_Game()
            elif again == 'no':
                exit()
            else:
                print("\t  What do you meant to say ? Just input [YES OR NO].")
       
       
Snake_Water_Gun_Game()
