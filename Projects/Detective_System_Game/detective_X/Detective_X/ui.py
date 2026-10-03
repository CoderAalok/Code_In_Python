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
        width = 55
        print("╔" + "═" * width + "╗")
        print("║" + "MAIN MENU".center(width) + "║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")

        menu_options = {
            1: 'Start New Case',
            2: 'Continue Investigation',
            3: 'Detective Profile',
            4: 'Case Records',
            5: 'Help',
            6: 'Exit'
        }

        for num, option in menu_options.items():
            print(f"║ [{num}] {option:<{width-6}} ║")

        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

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
            ("[1]", "The Missing Diamond", " 🟢 EASY", "✓ "),
            ("[2]", "The Midnight Server Breach", "🔴 HARD", "🔒"),
            ("[3]", "The Poisoned Professor", "🔴 HARD", "🔒"),
            ("[4]", "Murder at Blackwood Hotel", "🔴 HARD", "🔒"),
            ("[5]", "The Vanishing Programmer", "🔴 HARD", "🔒"),
            ("[6]", "The Museum Switch", "⚠️  MEDIUM", "🔒"),
            ("[7]", "The Anonymous Letter", " 🟢 EASY", "✓ "),
            ("[8]", "The Midnight Train", "🔴 HARD", "🔒"),
            ("[0]", "Return Back to Main Menu", "Back", "🔙 ")
        ]

        for num, title, difficulty, icon in cases:
            print(f"║ {num:<4} {title:<36} {difficulty:>8}  {icon}  ║")

        print("║" + " " * 58 + "║")
        print("╚" + "═" * 58 + "╝")


    @staticmethod
    def case_briefing_ui():
        width = 40
        print("╔" + "═" * (width + 2) + "╗")
        print(f"║{'CASE BRIEFING'.center(width + 2)}║")
        print("║" + " " * (width + 2) + "║")
        print("╠" + "═" * (width + 2) + "╣")

        print(f"║ [1] Begin Investigation {"":<16} ║")
        print(f"║ [2] Back to Case Library {"":<15} ║")
        
        print("║" + " " * (width + 2) + "║")
        print("╚" + "═" * (width + 2) + "╝")
        
        
        
               
    @staticmethod
    def investigation_dashboard(
        name,
        case, 
        level, 
        evd, 
        sus, 
        hint, 
        pro, 
        score=1000
    ):
        
        width = 55
        print("╔" + "═" * (width + 2) + "╗")
        print(f"║{'INVESTIGATION DASHBOARD'.center(width + 2)}║")
        print("╠" + "═" * (width + 2) + "╣")
        print(f"║ {'':<{width}} ║")

        print(f"║ Detective  :  {str(name):<{width-14}} ║")
        print(f"║ Case       :  {str(case):<{width-14}} ║")
        print(f"║ Difficulty : {str(level):<{width-13}} ║")
        print(f"║ Evidence   :  {str(evd):<{width-15}}  ║")
        print(f"║ Suspects   :  {str(sus):<{width-15}}  ║")
        print(f"║ Hints      :  {str(hint):<{width-14}} ║")
        print(f"║ Score      :  {str(score):<{width-14}} ║")
        print(f"║ Progress    :  {str(pro):<{width-14}} ║")
        print("║" + " " * (width + 2) + "║")
        
        print("╠" + "═" * (width + 2) + "╣")
        print("║" + " " * (width + 2) + "║")
        print("╚" + "═" * (width + 2) + "╝")


    @staticmethod
    def investigation_action_ui():
        width = 55
        
        print("╔" + "═" * (width + 2) + "╗")
        print(f"║{'INVESTIGATION ACTIONS'.center(width + 2)}║")
        print("╠" + "═" * (width + 2) + "╣")
        print(f"║ {'':<{width}} ║")
        print(f"║ {'[1] Visit Location':<{width}} ║")
        print(f"║ {'[2] Question Suspects':<{width}} ║")
        print(f"║ {'[3] Examine Evidence':<{width}} ║")
        print(f"║ {'[4] View Suspect Profiles':<{width}} ║")
        print(f"║ {'[5] Investigation Notebook':<{width}} ║")
        print(f"║ {'[6] Crime Timeline':<{width}} ║")
        print(f"║ {'[7] Compare Evidence':<{width}} ║")
        print(f"║ {'[8] Request Hint':<{width}} ║")
        print(f"║ {'[9] Make Final Accusation':<{width}} ║")
        print(f"║ {'[0] Save and Exit':<{width}} ║")
        print(f"║ {'':<{width}} ║")
        print("╚" + "═" * (width + 2) + "╝")


class LocationsUI:
    """Location: The Missing Diamond"""
    def __init__(self):
        self.status = {
            'case': 'Unsearched',
            'floor': 'Unsearched',
            'panel': 'Unsearched',
        }

    
    @staticmethod
    def visit_location_ui():
        width = 50
        print("╔" + "═" * (width) + "╗")
        print(f"║{'SELECT LOCATION TO VISIT'.center(width)}║")
        print("╠" + "═" * (width) + "╣")
        print(f"║ {'':<{width-2}} ║")
        print(f"║ {'[1] Exhibition Room':<{width-2}} ║")
        print(f"║ {'[2] Security Room':<{width-2}} ║")
        print(f"║ {'[3] Dining Hall':<{width-2}} ║")
        print(f"║ {'[0] Return to Dashboard':<{width-2}} ║")
        print(f"║ {'':<{width-2}} ║")
        print("╚" + "═" * (width) + "╝")


    def exhibition_room(self):
        print("""
    ╔═════════════════════════════════════════════════════════╗
    ║               LOCATION: EXHIBITION ROOM                 ║
    ╠═════════════════════════════════════════════════════════╣
    ║                ______________________                   ║
    ║               |                      |                  ║
    ║               |     DIAMOND CASE     |                  ║
    ║               |        (empty)       |                  ║
    ║               |______________________|                  ║
    ║                                                         ║
    ║ • The protected gallery where the Blackwood Diamond was ║
    ║ displayed. Glass case stands open.                      ║
    ╚═════════════════════════════════════════════════════════╝
    """)


        width = 50
        l_width, r_width = 22, 18
        
        print("╔" + "═" * width + "╗")
        print(f"║ {'SEARCH LOCATION: EXHIBITION ROOM'.center(width-2)} ║")
        print(f"╠" + "═"*(width) + "╣")
        print(f"║" + " "*(width) + "║")
        print(f"║ {'[1] Display Case':<{l_width}}        {f'[{self.status['case']}]':<{r_width}} ║")
        print(f"║ {'[2] Exhibition Floor':<{l_width}}        {f'[{self.status['floor']}]':<{r_width}} ║")
        print(f"║ {'[3] Access Panel':<{l_width}}        {f'[{self.status['panel']}]':<{r_width}} ║")
        print(f"║ [0] Exhibition Floor" + "║".rjust(width-20))
        
        print(f"║" + " "*(width) + "║")
        print("╚" + "═" * (width) + "╝")

    
    @staticmethod
    def security_room():
        print("This feature not added.")
        return 

    @staticmethod
    def dining_hall():
        print("This feature not added.")
        return

    
    
    


        
if __name__ == "__main__":
    # UI.investigation_dashboard('python', 1000,1000,10000,1110,10000,100000)
    # LocationUI.exhibition_room()
    # status = {
    # "case": "Found Key",
    # "floor": "Searched",
    # "panel": "Unsearched"
    # }
