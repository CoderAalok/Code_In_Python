"""Boost your mentally number calculation ability"""

from decimal import DivisionByZero
import json
import random
from collections import Counter
from pathlib import Path

# Config
FILE = "card_game.json"
BASE_DIR = Path(__file__).parent
USER_RECORD = BASE_DIR / FILE

class Cards:
    def __init__(self):
        self.target = random.randint(0, 99)
    
    @property
    def get_operators(self):
        """
        (+) -> Addition
        (-) -> Subtraction
        (*) -> Multiplication
        (/) -> Division
        (^) -> Power
        
        """
        operators = (
            ['+'] * 4 +
            ['-'] * 4 +
            ['*'] * 4 +
            ['/'] * 4 +
            ['^'] * 4
        )
        return operators



def load_record():
    try:
        with open(FILE)as f:
            return json.load(f)
    except Exception:
        return []
    
def add_file(file):
    with open(FILE, 'w')as f:
        json.dump(file, f, indent=4)

def verify_answer(ans: int, target: int) -> bool:
    return ans == target

def check_player(player_name: str):
    # load records
    record = load_record()

    for rec in record:
        if rec.get('player_id') == player_name:
            return rec
    
    format = {
        "player_id": player_name,
        "ways": 0,
        "operator": [],
        "points": 0
    }

    # add in the record
    record.append(format)
    add_file(record)
    
        
def player_calculation(
        num1: int,
        num2: int,
        idx_op: int, 
        target: int, 
        freq_operators: dict
    ):

    if num1 > 99 or num2 > 99:
        return "Number range should be (0-99)."
    
    ans = 0
    operators = {
        1: "+",
        2: "-",
        3: "*",
        4: "/",
        5: "^",
    }
    
    if (freq_operators.get(operators.get(idx_op)) != 0):
        if operators[idx_op] == "+":
            ans = num1 + num2
        
        elif operators[idx_op] == "-":
            ans = num1 - num2
        
        elif operators[idx_op] == "*":
            ans = num1 * num2

        elif operators[idx_op] == "/":
            if num2 == 0:
                return DivisionByZero(f"Cannot divide by {num2}.")
            
            if num1 % num2 == 0:
                ans = num1 / num2
            else:
                return f"{num2} is not factor of {num1}."
        
        elif operators[idx_op] == "^":
            if num2 <= 5:
                ans = num1**num2
            else:
                return "Num2: Minimum less than equal to 5."
    
        freq_operators[operators[idx_op]] -= 1
        
        # call function -> verify answer
        result = verify_answer(int(ans), target)
        
        # later scale this part
        if result:
            return "Correct! You got +10 points." 
        else:
            return "Incorrect! You lost -5 points." 


    return f"Operator ({operators[idx_op]}) limit reached out. Use any differet operator." 


c = Cards()
freq_operators = Counter(c.get_operators)

"""
GAME LOGIC:
Player makes target possible ways using different operators.
"""
"""
# Game Rules:
unique player name or id -> mandatory
correct answer -> +10 points
Incorrect answer -> -5 points  
avoid to use limit reached out number

"""
try:
    
    # player_name = input("Player name: ").strip().lower()
    # is_unique = check_player(player_name)
    
    play = True
    while play:
        # Target number
        target = c.target

        print(f"Your target: {target}")
        
        # player choose
        num1, num2 = list(map(int, input("Pick any number (0-99):\n").split()))
        print("1. (+)")
        print("2. (-)")
        print("3. (*)")
        print("4. (/)")
        print("5. (^)")
        op = int(input(f"Select any one operator number:\n").strip())
        
        result = player_calculation(num1, num2, op, target, freq_operators)
        print(result)
        
        player = input("Play more (y/n): ").strip().lower()
        if player == 'y':
            play = True
        else:
            play = False

except ValueError:
    print("Invalid input.")

