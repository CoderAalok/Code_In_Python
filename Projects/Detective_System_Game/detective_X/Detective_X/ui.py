class UI:

    @staticmethod
    def opening_screen():
        print("╔" + "═" * 52 + "╗")
        print("║" + " " * 52 + "║")
        print("║" + "DETECTIVE X".center(52) + "║")
        print("║" + " " * 52 + "║")
        print("║" + "PYTHON INVESTIGATION GAME".center(52) + "║")
        print("║" + " " * 52 + "║")
        print("╚" + "═" * 52 + "╝")

    @staticmethod
    def main_menu():
        print("╔" + "═" * 58 + "╗")
        print("║" + "MAIN MENU".center(58) + "║")
        print("╠" + "═" * 58 + "╣")
        print("║" + " " * 58 + "║")

        menu_options = [
            ("[1]", "Start New Case"),
            ("[2]", "Continue Investigation"),
            ("[3]", "Detective Profile"),
            ("[4]", "Case Records"),
            ("[5]", "Help"),
            ("[6]", "Exit")
        ]

        for num, option in menu_options:
            print(f"║ {num:<4} {option:<51} ║")

        print("║" + " " * 58 + "║")
        print("╚" + "═" * 58 + "╝")

    @staticmethod
    def case_selection():
        print("╔" + "═" * 50 + "╗")
        print("║" + "DIFFICULTY LEVELS".center(50) + "║")
        print("╠" + "═"*50 + "╣")
        print("║" + " " * 50 + "║")

        levels = [
            ("[1]", "Easy"),
            ("[2]", "Medium"),
            ("[3]", "Hard"),
            ("[4]", "Exit"),
        ]

        for num, level in levels:
            print(f"║ {num:<4} {level:<43} ║")
    
        print("║" + " " * 50 + "║")
        print("╚" + "═" * 50 + "╝")
        
    @staticmethod
    def case_library():
        print("╔" + "═" * 58 + "╗")
        print("║" + "CASE LIBRARY".center(58) + "║")
        print("╠" + "═" * 58 + "╣")
        print("║" + " " * 58 + "║")

        
        cases = [
            ("[1]", "The Missing Diamond", "MEDIUM"),
            ("[2]", "The Midnight Server Breach", "HARD"),
            ("[3]", "The Poisoned Professor", "HARD"),
            ("[4]", "Murder at Blackwood Hotel", "HARD"),
            ("[5]", "The Vanishing Programmer", "HARD"),
            ("[6]", "The Museum Switch", "MEDIUM"),
            ("[7]", "The Anonymous Letter", "EASY"),
            ("[8]", "The Midnight Train", "HARD")
        ]

        for num, title, difficulty in cases:
            print(f"║ {num:<4} {title:<36} {difficulty:>10}     ║")

        print("║" + " " * 58 + "║")
        print("╚" + "═" * 58 + "╝")
               
    @staticmethod
    def investigation_dashboard():
        width = 58

        print("╔" + "═" * width + "╗")
        print(f"║{'INVESTIGATION DASHBOARD'.center(width)}║")
        print("╠" + "═" * width + "╣")

        print(f"║ {'':<{width-2}} ║")
        print(f"║ {'[1] Investigate Locations':<{width-2}} ║")
        print(f"║ {'[2] Examine Evidence':<{width-2}} ║")
        print(f"║ {'[3] Interview Suspects':<{width-2}} ║")
        print(f"║ {'[4] View Timeline':<{width-2}} ║")
        print(f"║ {'[5] Evidence Board':<{width-2}} ║")
        print(f"║ {'[6] View Suspicion':<{width-2}} ║")
        print(f"║ {'[7] Use Hint':<{width-2}} ║")
        print(f"║ {'[8] Make Final Accusation':<{width-2}} ║")
        print(f"║ {'[9] Save Investigation':<{width-2}} ║")
        print(f"║ {'[0] Exit Investigation':<{width-2}} ║")
        print(f"║ {'':<{width-2}} ║")

        print("╚" + "═" * width + "╝")


    @staticmethod
    def location_screen():
        width = 58

        locations = [
            "[1] Main Hall",
            "[2] Study Room",
            "[3] Security Room",
            "[4] Garden",
            "[5] Exit"
        ]

        print("╔" + "═" * width + "╗")
        print(f"║{'INVESTIGATION LOCATIONS'.center(width)}║")
        print("╠" + "═" * width + "╣")

        print(f"║ {'':<{width-2}} ║")
        for location in locations:
            print(f"║ {location:<{width-2}} ║")
        print(f"║ {'':<{width-2}} ║")

        print("╚" + "═" * width + "╝")

UI.location_screen()