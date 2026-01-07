"""The Minion Game: In this game there are two players and they are used same string 
and find the all possible substring but the condition is player_1: Find all possible substring/words 
which begins (character) with  consonantes.
player_2: Find all possible words which begins with vowels.

-->> Our main task is find the winner of the game with higher scores.
Scores: Get +1 according to occurances of substring( No. of occurance = scores) 
NOTE: **All possible chance of apparing words not to generates it**  and string must uppercase.
"""
# Implementation:
def minion_game(string):
    string = string.upper()
    vowel = 'AEIOU'
    score_1 = 0
    score_2 = 0
    
    lenStrr = len(string)
    for i in range(lenStrr):
        # All Possible of substring 
        if string[i] not in vowel: # For consonante
            score_1 += lenStrr - i
            
        else:
            score_2 += lenStrr - i  # For Vowel
        
    if score_1 > score_2:
        print(f"Player_1 win with score: {score_1}")
        
    elif score_1 < score_2:
        print(f"Player_2 win with score: {score_2}")
    
    else:
        print("It's a tie!")
   
strr = input()
minion_game(strr)