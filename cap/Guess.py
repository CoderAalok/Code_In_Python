import random
def twice(final):
    result = final
    while True:
        # Random choice
        val = random.randint(1,100)
        val_1 = val
        try:
            user = int(input(f" ->Take ({val}) and 1.Add or 2.Subtract or 3.Skip and Show Result -> "))
            if user == 1:
                result += val_1
                continue

            elif user == 2:
                result -= val_1
                continue

            elif user == 3:
                return result
            else:
                print("🆒: I say choose either 1, 2, or 3 only!")

        except ValueError:
            print("😶‍🌫️ Choose only 1, 2, or 3")

def Guess_Number(num):
    result = 0
    if not num.isdigit():
        print(">>❌ Invalid valid input!")

    # length measure of number
    digit_size = len(num)
    if not digit_size in (2,3):
        print("\n⚠️ Hey my fellow, Only 2-digits or 3-digits guess 🙂‍↕️.")
        return

    print("\nNow '⏪' reverse it's digits...")
    rev_num = num[::-1] #1
    input("\nIf you reversed '⏪'-> Say:'Done'✅ : ").capitalize().strip()

    print(">>\nNow '➖' subtract: (reversed_number) and (your guessed_number) number...")
    diff = abs(int(rev_num) - int(num)) #2
    input("\nIf you subtracted '➖'-> Say:'Done'✅: ").capitalize().strip()

    print(">>\nNow again '⏪' reverse subtracted' number...")
    rev_diff = int(str(diff)[::-1]) #3
    input("\nIf you reversed '⏪'-> Say:'Done'✅: ").capitalize().strip()
    

    print("\n>>Let's see the result...🤩")
    result = rev_diff + diff

    # when reversed of 3-digits becomes 2-digits only executes
    if digit_size == 3 and result != 1089 or digit_size == 2 and result != 99:
        new_result = '0'+str(rev_diff)
        rev_ = int(new_result[::-1])
        result = rev_ + int(new_result)

    print(">>....\nWait! Wait!! Wait!!!🤔 Before see the result")
    outcome = twice(result)
    return outcome

# Starting to guess
num = input("🧏 Guess a number in your mind (2-digits) or (3-digits):\n")

input("\nIf you guessed. -> Say: 👍'Done' :  ").capitalize().strip()
print(f"\n🥴 So, Is your calculated value is {Guess_Number(num)}?")

user_feedback = input("\nIf yes! 💬 Say:'Yes': ").capitalize().strip()
if user_feedback == 'Yes':
    print("\nThanks! For playing 😎.")
else:
    print("\n🤦: Make ensure your all steps calculation correctly.")
