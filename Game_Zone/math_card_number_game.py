"""Boost your mentally number calculation ability"""
"""
GAME LOGIC:
A Player makes a target using given card numbers and arithmetic operators.
"""

"""
# Game Rules:
Player name -> mandatory
Use only given card numbers and arithmetic operators to make target. Also writting an expression must use parentheses.
Avoid writting wrong expression.

for Easy Level:
correct answer -> +5 points
Incorrect answer -> -5 points  

for Medium Level:
correct answer -> +10 points
Incorrect answer -> -10 points  

for Hard Level:
correct answer -> +15 points
Incorrect answer -> -15 points  
"""

"""
Level -> Easy-> Medium-> Hard
"""

import json
import random
from pathlib import Path
import re
from typing import List
from itertools import permutations, product
from collections import Counter

# Config
FILE = "card_game.json"
BASE_DIR = Path(__file__).parent
USER_RECORD = BASE_DIR / FILE

class Cards:
    def __init__(self):
        self.operators = ['+', '-', '*', '/']
        
    def easy_level(self):
        self.possible_targets = [] # collect all possible values(targets)
        
        # generate cards
        cards = random.choices(list(range(1, 20)), k=2)

        for nums in permutations(cards):
            for ops in product(self.operators, repeat=1):
                expre = (
                    f"{nums[0]}{ops[0]}"
                    f"{nums[1]}"
                )

                try:
                    result = eval(expre)
                    if result == int(result):
                        self.possible_targets.append(int(result))

                except Exception:
                    continue

        # generate target
        target = random.choice(self.possible_targets)
        return (cards, target)


    def medium_level(self):
        self.possible_targets = [] # collect all possible values(targets)
        
        # generate cards
        cards = random.choices(list(range(1, 20)), k=3)
        
        for nums in permutations(cards):
            for op in product(self.operators, repeat=2):
                expre = (
                    f"{nums[0]}{op[0]}"
                    f"{nums[1]}{op[1]}"
                    f"{nums[2]}"
                )

                try:
                    # evalulate the expression
                    result = eval(expre)
                    if result == int(result):
                        self.possible_targets.append(int(result))
                    
                except Exception as e:
                    continue
        
        # generate target value
        target = random.choice(self.possible_targets)
        return (cards, target)

    def hard_level(self):
        self.possible_targets = [] # collect all possible values(targets)
        
        # generate cards
        cards = random.choices(list(range(1, 20)), k=4)
        
        for nums in permutations(cards):
            for op in product(self.operators, repeat=3):
                expre = (
                    f"{nums[0]}{op[0]}"
                    f"{nums[1]}{op[1]}"
                    f"{nums[2]}{op[2]}"
                    f"{nums[3]}"
                )

                try:
                    # evalulate the expression
                    result = eval(expre)
                    if result == int(result):
                        self.possible_targets.append(int(result))
                    
                except Exception:
                    continue
        
        # generate target value
        target = random.choice(self.possible_targets)
        return (cards, target)

    
def load_record():
    try:
        with open(FILE)as f:
            return json.load(f)
    except Exception:
        return []

    
def update_file(file):
    with open(FILE, 'w')as f:
        json.dump(file, f, indent=4)


def verify_answer(ans, target, tol=1e-6) -> bool:
    return abs(ans - target) < tol


def get_player_record(player_name: str):
    # load records
    record = load_record()

    # check player does exist
    for rec in record:
        if rec.get('player_id') == player_name:
            return rec

    # add new player
    format = {
        "player_id": player_name,
        "correct": 0,
        "incorrect": 0,
        "scores" : 0,
    }

    # update record
    record.append(format)
    update_file(record)
    

def player_calculation(expre: str, target: int, cards: List[int], player_name: str, level: str):
    """This function works for all number of cards"""

    #Level-wise points
    level_points = {
        '1': 5,  # easy level
        '2': 10, # medium level
        '3': 15, # hard level
    }
    
    # extract all numbers from player expression
    chosen_cards = list(map(int, re.findall(r'\d+', expre)))
    
    # check all card numbers frequency match
    if Counter(chosen_cards) != Counter(cards):
        return "You must use given card numbers."

    # calculate answer
    try:
        ans = eval(expre)
    except Exception:
        return "Invalid expression."
    
    # verify answer
    result = verify_answer(ans, target)

    # load record
    record = load_record()
    for rec in record:
        if rec.get("player_id") == player_name:
            if result:
                rec['correct'] += 1
                rec['scores'] += level_points[level]
                print(f"You got +{level_points[level]} points.")

            else:
                rec['incorrect'] += 1
                rec['scores'] -= level_points[level]
                print(f"You lost -{level_points[level]} points.")
                
            # update record
            update_file(record)
            return


c = Cards()

def main():
    try:
        """Player can explicitly play no need to create account."""
        is_player_name = False # initially no name
        while not is_player_name:
            player_name = input("Player name: ").strip().lower()
            if not player_name:
                print("Player name is mandatory.")
            else:
                is_player_name = player_name

        player_name = is_player_name
        get_player_record(player_name) # if player_name not found in record-file, automatically created.

        print("1) Easy Level")
        print("2) Medium Level")
        print("3) Hard Level")
        level = input("Select number of level [1-3]: ").strip()

        levels = {
            '1': c.easy_level,
            '2': c.medium_level,
            '3': c.hard_level,
        }

        # check None type
        if levels.get(level) is None:
            print("Choose level only [1-3].")
            return
    
        play = True
        while play:
            # load cards and target
            cards, target = levels[level]()
            
            print(f"\nCard Numbers: {cards}")
            print(f"Operators: {['+', '-', '*', '/']}")
            print(f"Your target: {target}\n")

            print("NOTE: Use given card nubmers and operators to make target. Also use parentheses.\n")
            
            # player
            expre = input("Let's play:\n").strip()
            
            # call function -> result
            is_error = player_calculation(expre, target, cards, player_name, level)
            # check error
            if is_error:
                print(is_error)
            
            # push player the (play more)
            player = input("Play more (y/n): ").strip().lower()
            if player == 'y':
                play = True 
            else:
                play = False

    except Exception as e:
        print(f"Invalid input.\n {e}")


if __name__ == "__main__":
    main()
