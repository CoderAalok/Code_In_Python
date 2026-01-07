# lottery = [1,2,3,4,5,6,7,8,9,10,
#            'A,','E','I','O','U'
# ]


# #Win Condition
# lotteryWin = {'1245':"Congratulation👏 you will win Smart Watch⌚️",
#               '4890':"Congratulation👏 you will win PowerBank🔋",
#               'AOUI':"Congratulation👏 you will win Mouse🖱",
#               'UIEO':"Congratulation👏 you will win KeyBoard⌨️"              
# }

# print(f"\nSelect any four numbers or letter:\n{lottery}")
# print("""\nKeep on your mind!
# if these four numbers or letters matching any tickets then wins a prize.""")

# # Randomly Select 4-rounds
# lucky = []
# for i in range(4):
#     player = input(f"Pick chance {4-i}: ").strip()
#     lucky.append(player)

# print("\nJust a few second for verifing your numbers or letters")

# key = ''.join(lucky)
# result = lotteryWin.get(key,'Tryagain!')
# print(result)


import random, time

lotteryNum = ['1','2','3','4','5','6','7','8','9','10']
lotteryAlpha =  ['A','E','I','O','U']

prizes = ['Smart Watch⌚️', 'Mouse🖱', 'Power Bank🔋', 'HeadPhone🎧']

lotteryKeyNum = random.sample(lotteryNum, 4)
lotteryKeyalpha = random.sample(lotteryAlpha, 4)
print(lotteryKeyalpha)

print(f"\nSelect any four numbers or letter:\n{lotteryNum} and {lotteryAlpha}")
print("""\nKeep on your mind!
If your selected any four numbers or letters matching any tickets then wins a prize.""")

print(f"\nPrizes are: {prizes}\n")

# Randomly Select 4-rounds
while True:
    lucky = []
    for i in range(4):
        player = input(f"Pick chance {4-i}: ").strip()
        lucky.append(player)

    print("\n🔎 Verifing your luck!.....")
    time.sleep(0.5)

    if lucky == lotteryKeyNum or lucky == lotteryKeyalpha:
        print(f"Congratulation👏! you will win.")
        print("wait for your lucky prize, Just a second.....")
        time.sleep(0.5)
        print(f"{random.choice(prizes)} ")
        break
    else:
        print("😢Bad Luck! Try next time!")
    
    # Correct Answer:
    print(f"\nWinning Number Ticket: {lotteryKeyNum}")
    print(f"Winning letter Ticket: {lotteryKeyalpha}")