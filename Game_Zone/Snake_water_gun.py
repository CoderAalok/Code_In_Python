#Snake Water Gun Game..
import random

print("Welcome to Snake🐍 Water🌊 Gun🔫 Game\n ")

def Snake_Water_Gun_Game():
    while True:
        user_name = input("Enter your name🧍: ")
        if user_name == '' or not user_name.isalpha():
            print("Name is required!")
            continue
        
        content = {
            1:"Snake🐍", 
            2:"Water🌊", 
            3:"Gun🔫",
        }
        
        score_user = 0 
        score_bot = 0 
        i = 0
        max_attempt = 5
    
        while i < max_attempt:
            try:
                user = int(input(f"Select anyone number [1-3] -> {list(content.items())} : "))
                i += 1 
                
                if not 1<= user <= 3:
                    print("The value must be under range.")
                    i -= 1
                    continue
                
                bot = random.randint(1,3)
                print(f"[Canva🤖] : {content[bot]}\n[{user_name}]🧍: {content[user]}")
                
                if user == bot:
                    print("It's a Draw!, So no one get point.")
                    
                elif (bot == 1 and user == 2) or ( bot == 2 and user == 3) or ( bot == 3 and user == 1 ):
                    print("[Canva🤖]: +1 point.") 
                    score_bot += 1
                    
                else:
                    print(f"[{user_name}]: +1 point.") 
                    score_user += 1
            
            except ValueError:
                print("Enter only number [1], [2] or [3].") 
                continue
        
        print(f"Final scores:\n[{user_name}]: {score_user}\n[Canva]: {score_bot}")
        
        if score_user > score_bot:
            print(f"🎉 winner 🧍[{user_name}] ")
            
        elif score_bot == score_user:
            print(f"🤝 It's a tie. ")
                      
        else:
            print("🎉 winner [Canva🤖]")
            
        with open("game.txt",'w')as fg:
            fg.write(f"Score : [{user_name}]: {score_user}\n [Canva]: {score_bot}" )   
        
        while True:    
            again = input("Do you like to play once more [y / n] : ").lower().strip()
            if again == '' or not again.isalpha():
                print("Input type is Empty .")
                continue
            
            if again == 'y':
               break #Snake_Water_Gun_Game()
            
            elif again == 'n':
                exit()
                
            else:
                print("What do you meant to say? Just input [y] OR [n].")
       
       
Snake_Water_Gun_Game()
