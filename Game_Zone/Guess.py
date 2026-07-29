import random
import time

from regex import R
def twice(final):
    result = final
    while True:
        # Random choice
        val = random.randint(1,100)
        val_1 = val
        try:
            user = int(input(f"-> Can you ({val}):\n1. Add\n2. Subtract\n3. show result -> "))
            if user == 1:
                result += val_1

            elif user == 2:
                result -= val_1
                
            else:
                return result
                
        except ValueError:
            print("😶‍🌫️ Choose only 1, 2 & 3")

def Guess_Number(num):
    result = 0
    if not num.isdigit():
        print(">>❌ Invalid valid input!")

    # length measure of number
    digit_size = len(num)
    if not digit_size in [2,3]:
        print("⚠️ Hey my fellow, Only 2-digits or 3-digits guess 🙂‍↕️.\n")
        return

    print(">> Now '⏪' reverse it's digits...\n")
    rev_num = num[::-1] #1
    input("Enter to next step ->\n ")
    
    print(">> Now '➖' subtract: (reversed_number) and (your guessed_number) number...\n")
    diff = abs(int(rev_num) - int(num)) #2
    input("Enter to next step ->\n ")
    
    print(">> Now again '⏪' reverse subtracted' number...\n")
    rev_diff = int(str(diff)[::-1]) #3
    input("Enter to next step ->\n ")
    
    print(">> Now add current reversed number and its non-reversed\n")
    result = rev_diff + diff
    
    print(">> Checking....🤩\n")
    # when reversed of 3-digits becomes 2-digits only executes
    if digit_size == 3 and result != 1089 or digit_size == 2 and result != 99:
        new_result = '0'+str(rev_diff)
        rev_ = int(new_result[::-1])
        result = rev_ + int(new_result)

    time.sleep(2)
    
    print("Wait! Wait!! Wait!!!")
    outcome = twice(result)
    return outcome

# Starting to guess
num = input("🧏 Guess a number in your mind (2-digits) or (3-digits):\n")

print(f"\n🥴 So, Is your calculated value is {Guess_Number(num)}?")

user_feedback = input("\nIf yes! 💬 Say:'Yes': ").strip().lower()
if user_feedback == 'yes':
    print("\nThanks! For playing 😎.")
else:
    print("\n🤦: Make ensure your all steps calculation correctly.")
