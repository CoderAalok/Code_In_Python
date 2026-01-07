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
    if not num:
        print(">>❌ Invalid valid input!")
        return False
    
    if num not in [2,3]:
        print("\n⚠️ Hey my fellow, Only 2-digits or 3-digits guess 🙂‍↕️.")
        return False

    if num == 2:
        result = 99  #2-digits
    else:
        result = 1089  #3-digits

    print("\nNow '⏪' reverse it's digits...")
    
    input("\nIf you reversed '⏪'-> Say:'Done'✅ : ").capitalize().strip()

    print(">>\nNow '➖' subtract: (reversed_number) and (your guessed_number) number...")
 
    input("\nIf you subtracted '➖'-> Say:'Done'✅: ").capitalize().strip()

    print(">>\nNow again '⏪' reverse subtracted' number...")
   
    input("\nIf you reversed '⏪'-> Say:'Done'✅: ").capitalize().strip()
    
    print("\n>>Let's see the result...🤩")

    print(">>....\nWait! Wait!! Wait!!!🤔 Before see the result")
    outcome = twice(result)
    return outcome

# Starting to guess
num = int(input("🧏 Guess a number in your mind either (2-digits) or (3-digits):\n"))
input("\nIf you guessed. -> Say: 👍'Done' :  ").capitalize().strip()

result = Guess_Number(num)
print(f"\n🥴 So, your calculated value is {result}?")

if result:
    user_feedback = input("\nIf yes! 💬 Say:'Yes': ").capitalize().strip()
    if user_feedback == 'Yes':
        print("\nThanks! For playing 😎.")
    else:
        print("\n🤦: Make ensure your all steps calculation correctly.")
else:
    print("Because you thing wrong number!")
