import re
import time
import pyttsx3

def day_status(days):
    remainder_days = {
        "Low": "Too near",
        "Medium": "Not so far",
        "High": "So far"
    }
    
    if days <= 15:
        message_days = "Low"
    elif days <= 45:
        message_days = "Medium"
    else:
        message_days = "High"
        
    return (remainder_days[message_days], message_days)
    
def hour_status(hour):
    schedule_study = {
        "Low": "Very bad ✔️",
        "Medium": "Slightly good ☑️",
        "High": "Totally fine ✅"
    }
    
    if hour < 5:
        message_hour = "Low"
    elif hour < 10:
        message_hour = "Medium"
    else:
        message_hour = "High"
    
    return (schedule_study[message_hour], message_hour)

def percentage_status(percentage):
    previous_prof = {
        "Low": "Poor ✔️",
        "Medium": "Good ☑️",
        "High": "Excellent ✅"
    }
    
    if percentage <= 50:
        message_prof = "Low"
    elif percentage <= 70:
        message_prof = "Medium"
    else:
        message_prof = "High"
    
    return (previous_prof[message_prof], message_prof)

def get_proformance(msg_day, msg_hour, msg_per):
    # Determine proformance days and hours
    
    if msg_day in ["Low", "Medium", "High"] and msg_hour in ["High"]:
        proformance = "High"
    elif msg_day in ["Low", "Medium", "High"] and msg_hour in ["Medium"]:
        proformance = "Medium"
    elif msg_day in ["Low", "Medium"] and msg_hour in ["Low"]:
        proformance = "Low"
    else:
        proformance = None
    
    # After that determine proformance (days, hours) and percentage
    category = None
    if msg_per and proformance:
        if msg_per in ["Low", "Medium", "High"] and proformance in ["Low"]:
            category = "Below"
        elif msg_per in ["Low", "Medium", "High"] and proformance in ["Medium"]:
            category = "Average"
        elif msg_per in ["High"] and proformance in ["Low", "Medium", "High"]:
            category = "Topper"
            
    return category


if __name__ == '__main__':
    
    try:
        speak = pyttsx3.init()
        
         # Bot asked these questions
        text = "What's your name?"
        text1 = "How many of days left your final board examination?"
        text2 = "How many hours you will study in a day?"
        text3 = "Is your pre-board finished (yes/no)?"
        text4 = "So, what percentage you scored?"
        text5 = "Anyway what percentage in mid-term you scored?"
        text6 = "Answer is not defined."
        text7 = "If you say I'll generate good strategy for scored better result. Just tell me yes!"
        text9 = "Best wish you follow these strategies you'll definatly do better than other."
        
        print("Bot: What's your name?")
        speak.say(text)
        speak.runAndWait()
        
        std = None
        while std is None:
            
            student = input("You: ").strip().title()
            pattern = re.compile(r'^[a-zA-Z]+$')
            
            if not student:
                print("Bot: Please enter your name?")
            
            elif not pattern.match(student):
                print("Bot: Please enter correct name?")
                
            else:
                std = student
                
       
        print(f"Hi! {std}")
        speak.say(f"Hi! {std}")
        
        print("Bot: How many of days left your final board examination?")
        speak.say(text1)
        speak.runAndWait()
        
        days = int(input("\nYou: ").strip())
        
        print("Bot: How many hours you will study in a day?")
        speak.say(text2)
        
        hours = int(input("\nYou: ").strip())
        
        print("Bot: Is your pre-board finished (yes/no)?")
        speak.say(text3)
        speak.runAndWait()
        
        confirm_board = (input("\nYou: ").strip().lower())
        
        percentage = None
        if confirm_board == 'yes':
            print("Bot: So, what percentage you scored?")
            speak.say(text4)
            speak.runAndWait()
            percentage_board = int(input("\nYou: ").strip())
            percentage = percentage_board
            
        elif confirm_board == 'no':
            print("Bot: Anyway what percentage in mid-term you scored?")
            speak.say(text5)
            speak.runAndWait()
            percentage_mid = int(input("\nYou: ").strip())
            percentage = percentage_mid
            
        else:
            print("Bot: Answer is not defined.")
            speak.say(text6)
            speak.runAndWait()
        
        
        day_prof, msg_day = day_status(days) #1
        hour_prof, msg_hour = hour_status(hours) #2
        per_prof, msg_per = percentage_status(percentage) #3
        
        categoies = {
            "Below": """A student in this category may struggle with concepts or consistency,
                    but they have strong potential for improvement. With guidance, practice, and confidence, steady progress is always possible.""",
            
            "Average": """A student in this category maintains a balanced performance and understands most concepts with regular effort.
                    With focus and discipline, they can easily move to a higher level of achievement.""",
                        
            "Topper": """A student in this category demonstrates excellent understanding, consistency, and dedication.
                    Their hard work, curiosity, and discipline set an example for others."""
        }
        
        if msg_day and  msg_hour and  msg_per:
            category = get_proformance(msg_day, msg_hour, msg_per) #4
            
            print("\nBottom line your schedule and proformance:")
            speak.say("Bottom line your schedule and proformance")
            speak.runAndWait()
            
            print("_"*50)
            print(f"➱ Your exam {days} days left: {day_prof}")
            print(f"➱ Your study time period: {hour_prof}")
            print(f"➱ Previous %: {per_prof}")
            print("-"*50)
            
            if category:
                summary = categoies.get(category)
                print(f"Bot: Your proformance fallen into {category}")
                speak.say(f"Your proformance fallen into {category}")
                speak.runAndWait()
                
                print(f"● Summary: {summary}")
                speak.say(summary)
                speak.runAndWait()
        
            # After that
            time.sleep(0.02)
            print("Bot: If you say I'll generate good strategy for scored better result. Just tell me yes!")
            speak.say(text7)
            speak.runAndWait()
            stdin = input("You: ").strip().lower()
            
            strategies = [
                "Build strong fundamentals by understanding concepts instead of memorizing",
                "Follow a consistent daily study routine",
                "Set clear, realistic, and achievable goals",
                "Practice actively through problems, writing, and self-explanation",
                "Review performance regularly and learn from mistakes",
                "Manage time effectively and minimize distractions",
                "Ask for help whenever concepts are unclear",
                "Maintain physical and mental well-being with proper rest and activity",
                "Stay positive, patient, and focused on continuous improvement"
            ]
            
            if stdin == "yes":
                
                for strategy in (strategies):
                    print(f"● {strategy}")
                
                print("\nBest wish you follow these strategies you'll definatly do better than other.")
                speak.say(text9)
                speak.runAndWait()
            
            else:
                print("\nBot: Good Luck!")
                speak.say("Good Luck!")
                speak.runAndWait()
                
    except (ValueError, TypeError, AttributeError):
        print("Bot: Input type is not valid as required!")
        

