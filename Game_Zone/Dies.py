import random,time

# Game Setup
agent_name = random.choice(["Sora", "ChatGPT", "Grok", "Fido", "Canva"])
player_name = input("Enter your 👤 nickname: ").strip().title()
if not player_name:
    player_name = "Unknown"

# Start positions (Rule: Start: 1)

player_p = 1
agent_p = 1
win_position = 12
    
# Rules
step_jump = {3: 5, 8: 10}
snake_position = {6: 2, 11: 7, 9: 6}

# Dice
dice = { 1:'⚀', 2:'⚁', 3:'⚂', 4:'⚃', 5:'⚄', 6:'⚅'}

# Winner
winner = ""

print("Let's Play...")
time.sleep(1.5)
print(f"\n🎮 ​Game Start! 👤 {player_name} vs 🤖 {agent_name}") 
print(f"🎯 Goal: Reach position {win_position}")

while True:
    try:
        time.sleep(0.2)
        player_input = input("\nPress Enter to 🎲 roll dice... ").strip()
        if player_input != "":
            print("Just press Enter↩ to roll!🎲")
            continue

        # Player Turn
        player_roll = random.randint(1, 6)
        print(f"👤 {player_name} rolled a {dice[player_roll]}")
        
        if (player_p + player_roll) <= win_position:
            player_p += player_roll
            print(f"👤 {player_name} moved to {player_p}")
            
            # Check for Snakes/Ladders
            if player_p in step_jump:
                old_p = player_p
                player_p = step_jump[player_p]
                print(f"👤 {player_name} -> Jump from {old_p} to {player_p}\n")
            elif player_p in snake_position:
                old_p = player_p
                player_p = snake_position[player_p]
                print(f"👤 {player_name} -> Fall from {old_p} to {player_p}\n")
        else:
            print(f"👤 {player_name} needs exact {win_position - player_p} to win.")

        # Win Check Player
        if player_p == win_position:
            winner = player_name
            print(f"\n🥇 {winner} Wins! 🎉")
            break

        # Agent Turn
        time.sleep(0.5)
        agent_roll = random.randint(1, 6)
        print(f"🤖 {agent_name} rolled a {dice[agent_roll]}")
        
        if (agent_p + agent_roll) <= win_position:
            agent_p += agent_roll
            print(f"🤖 {agent_name} moved to {agent_p}")
            
            # Check for Snakes/Ladders
            if agent_p in step_jump:
                old_p = agent_p
                agent_p = step_jump[agent_p]
                print(f"🤖 {agent_name} -> Jump from {old_p} to {agent_p}\n")
            elif agent_p in snake_position:
                old_p = agent_p
                agent_p = snake_position[agent_p]
                print(f"🤖 {agent_name} -> Fall from {old_p} to {agent_p}\n")
        else:
            print(f"🤖 {agent_name} needs exact {win_position - agent_p} to win.")

        # Win Check Agent
        if agent_p == win_position:
            winner = agent_name
            print(f"\n🥇 {winner} Wins! 🤖")
            break
            

    except ValueError:
        print("Invalid input!")
    except KeyboardInterrupt:
        print("\nGame exited.")
        break

# Loser found
loser = agent_name if agent_p != win_position else player_name

# Record existing format  create
record = f"{winner} beats {loser}"

try:
    with open("snake.txt","r")as r:
        lines = [line.strip('\n') for line in r.readlines()]
except FileNotFoundError:
    lines = []

if record not in lines:

    with open("snake.txt",'a+')as w:
        w.write(f"{winner} beats {loser} "+ '\n')
    print("Recods has been saved.")

else:
    print(f"This {winner} and {loser} already exists in file.")