import random

greet = [
    "Hi there! What’s up?",
    "Good to see you, There!",
    "Hey! Hope you’re having a great day 🙂",
    "Yo! What’s good? 😄",
    "Heyyy, how you been?",
    "Sup! Hope life’s treating you right.",
    "Hello! Long time no see, hope you’re doing well.",
]

speeking_style = [
    "Formal / Professional (Corporate tone)",
    "Gen Z / Internet slang",
    "Casual / Friendly",
    "Motivational / Coach style",
    "Analytical / Logical thinker",
    "Storyteller / Poetic",
    "Traditional / Respectful elder tone", 
]

for _ in range(1):
    greet_mess = random.choice(greet)
    style_mess = random.choice(speeking_style)
    print(f"⥀ {greet_mess}")
    print(f"⥀ In general, In which style do you like to conversation with me?\n➥ {style_mess}")

