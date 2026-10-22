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


    #  ------------------- DETECTIVE PROFILE -------------------
    @staticmethod
    def detective_profile(records: dict):
        if not records:
            return

        key_width, value_width = 20, 30
        box_width = key_width + value_width + 5

        print("╔" + "═" * box_width + "╗")
        print(f"║{'DETECTIVE PROFILE'.center(box_width)}║")
        print("╠" + "═" * box_width + "╣")

        print(f"║ {'Name':<{key_width}}: {records['Name']:<{value_width}}  ║")
        print(f"║ {'Rank':<{key_width}}: {records['Rank']:<{value_width}}  ║")
        print(f"║ {'Cases Won':<{key_width}}: {str(records['Cases_Won']):<{value_width}}  ║")
        print(f"║ {'Cases Lost':<{key_width}}: {str(records['Cases_Lost']):<{value_width}}  ║")
        print(f"║ {'XP':<{key_width}}: {str(records['XP']):<{value_width}}  ║")
        print(f"║ {'Rating':<{key_width}}: {str(records['Rating']):<{value_width}}  ║")

        print(f"║{'':<{box_width}}║")
        print("╚" + "═" * box_width + "╝")
        
        return 


    @staticmethod
    def case_selection():
        print("╔" + "═" * 50 + "╗")
        print("║" + "DIFFICULTY LEVELS".center(50) + "║")
        print("╠" + "═" * 50 + "╣")
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
            ("[1]", "The Missing Diamond",       "🟢  EASY "),
            ("[2]", "The Midnight Server Breach", "🟡 MEDIUM",),
            ("[3]", "The Poisoned Professor",     "🔴 HARD  ",),
            ("[0]", "Return Back to Main Menu",   "🔙 Back  ", ),
        ]

        for num, title, difficulty in cases:
            print(f"║ {num:<4} {title:<36} {difficulty:>5}  {'║':>5}")

        print("║" + " " * 58 + "║")
        print("╚" + "═" * 58 + "╝")

    @staticmethod
    def case_briefing_ui():
        width = 40
        print("╔" + "═" * (width + 2) + "╗")
        print(f"║{'CASE BRIEFING'.center(width + 2)}║")
        print("║" + " " * (width + 2) + "║")
        print("╠" + "═" * (width + 2) + "╣")
        print(f"║ [1] Begin Investigation {'':<16} ║")
        print(f"║ [2] Back to Case Library {'':<15} ║")
        print(f"║ [0] Save and exit {'':<22} ║")
        print("║" + " " * (width + 2) + "║")
        print("╚" + "═" * (width + 2) + "╝")


    @staticmethod
    def help_ui():
        width = 50
        print("╔" + "═" * (width) + "╗")
        print(f"║{'DETECTIVE X — HELP'.center(width)}║")
        print("║" + " " * (width) + "║")
        print("╠" + "═" * (width) + "╣")
        
        print(f"║ [1] Game Rules & Objectives {'':<20} ║")
        print(f"║ [2] Commands & Controls  {'':<23} ║")
        print(f"║ [3] Investigation Guide {'':<24} ║")
        print(f"║ [4] Scoring & Detective Ranks {'':<18} ║")
        print(f"║ [5] Investigation Progress  {'':<20} ║")
        print(f"║ [6] Hints & Assistance {'':<25} ║")
        print(f"║ [0] Return to Main Menu {'':<24} ║")
        
        
        print("║" + " " * (width) + "║")
        print("╚" + "═" * (width) + "╝")


    @staticmethod
    def investigation_dashboard(name, case, level, evd, sus, hint, pro, score=1000, total_evidence=12):
        width = 55
        ev_str = f"{evd} / {total_evidence}"
        
        print("╔" + "═" * (width + 2) + "╗")
        print(f"║{'INVESTIGATION DASHBOARD'.center(width + 2)}║")
        print("╠" + "═" * (width + 2) + "╣")
        print(f"║ {'':<{width}} ║")
        
        print(f"║ Detective  :  {str(name):<{width-14}} ║")
        print(f"║ Case       :  {str(case):<{width-14}} ║")
        print(f"║ Difficulty :  {str(level):<{width-13}}║")
        print(f"║ Evidence   :  {ev_str:<{width-14}} ║")
        print(f"║ Suspects   :  {str(sus):<{width-15}}  ║")
        print(f"║ Hints Used :  {str(hint):<{width-14}} ║")
        print(f"║ Score      :  {str(score):<{width-14}} ║")
        print(f"║ Progress   :  {str(pro):<{width-14}} ║")
        
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


    @staticmethod
    def suspect_selection_ui(suspects: dict, title="SELECT SUSPECT"):
        width = 55
        print("╔" + "═" * (width + 2) + "╗")
        print(f"║{title.center(width + 2)}║")
        print("╠" + "═" * (width + 2) + "╣")
        print(f"║{'':<{width + 2}}║")
        for num, data in suspects.items():
            name_str = f"[{num}] {data['name']}"
            role_str = f"[{data['role']}]"
            print(f"║ {name_str:<28} {role_str:<26} ║")
        print(f"║ {'[0] Return to Dashboard':<{width}} ║")
        print(f"║{'':<{width + 2}}║")
        print("╚" + "═" * (width + 2) + "╝")


    @staticmethod
    def suspect_profile_ui(suspect: dict):
        width = 55
        print("╔" + "═" * (width + 2) + "╗")
        print(f"║{'SUSPECT PROFILE'.center(width + 2)}║")
        print("╠" + "═" * (width + 2) + "╣")
        print(f"║{'':<{width + 2}}║")
        print(f"║ Name         : {suspect['name']:<{width-15}} ║")
        print(f"║ Role         : {suspect['role']:<{width-15}} ║")
        print(f"║ Stated Alibi : {suspect['alibi']:<{width-14}}║")
        print(f"║ Motive       : {suspect['motive']:<{width-14}}║")
        print(f"║ Status       : {suspect['status']:<{width-14}}║")
        print(f"║{'':<{width + 2}}║")
        print("╚" + "═" * (width + 2) + "╝")

    @staticmethod
    def interrogation_ui(name: str, questions: dict):
        width = 55
        
        title = f"INTERROGATING: {name.upper()}"
        print("╔" + "═" * (width + 2) + "╗")
        print(f"║{title.center(width + 2)}║")
        print("╠" + "═" * (width + 2) + "╣")
        print(f"║{'':<{width + 2}}║")
        
        for num, q_data in questions.items():
            q_label = f"[{num}]  {q_data[0]}"
            print(f"║ {q_label:<{width}} ║")
            
        print(f"║ {'[0] Back to Suspects':<{width}} ║")
        print(f"║{'':<{width + 2}}║")
        print("╚" + "═" * (width + 2) + "╝")


class LocationCase1:
    """UI display for Case_1: The Missing Diamond locations."""
    
    def __init__(self):
        self.status = {
            # Exhibition Room
            'case':    'Unsearched',
            'floor':   'Unsearched',
            'panel':   'Unsearched',
            'exit':    'Unsearched',
            
            # Security Room
            'cctv':    'Unsearched',
            'log':     'Unsearched',
            'desk':    'Unsearched',
            'rack':    'Unsearched',
            
            # Dining Hall
            'table':   'Unsearched',
            'kitchen': 'Unsearched',
            'trash':   'Unsearched',
            'window':  'Unsearched',
        }

    @staticmethod
    def visit_location_ui():
        width = 50
        print("╔" + "═" * width + "╗")
        print(f"║{'SELECT LOCATION TO VISIT'.center(width)}║")
        print("╠" + "═" * width + "╣")
        print(f"║ {'':<{width-2}} ║")
        print(f"║ {'[1] Exhibition Room':<{width-2}} ║")
        print(f"║ {'[2] Security Room':<{width-2}} ║")
        print(f"║ {'[3] Dining Hall':<{width-2}} ║")
        print(f"║ {'[0] Return to Dashboard':<{width-2}} ║")
        print(f"║ {'':<{width-2}} ║")
        print("╚" + "═" * width + "╝")


    # Exhibition Room
    def exhibition_room_ui(self):
        width = 55
        l_width, r_width = 22, 23

        # room scene
        print("╔" + "═" * width + "╗")
        print(f"║{'LOCATION: EXHIBITION ROOM'.center(width)}║")
        print("╠" + "═" * width + "╣")
        print(f"║{'':<{width}}║")
        print(f"║{'______________________'.center(width)}║")
        print(f"║{'|                      |'.center(width)}║")
        print(f"║{'|     DIAMOND CASE     |'.center(width)}║")
        print(f"║{'|        (empty)       |'.center(width)}║")
        print(f"║{'|______________________|'.center(width)}║")
        print(f"║{'':<{width}}║")
        print(f"║ {'• The protected gallery where the Blackwood Diamond':<{width-2}} ║")
        print(f"║ {'  was displayed. Glass case stands open.':<{width-2}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

        # search spots
        print("╔" + "═" * width + "╗")
        print(f"║ {'SEARCH LOCATION: EXHIBITION ROOM'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║ {'[1] Display Case':<{l_width}}        {f'[{self.status['case']}]':<{r_width}} ║")
        print(f"║ {'[2] Exhibition Floor':<{l_width}}        {f'[{self.status['floor']}]':<{r_width}} ║")
        print(f"║ {'[3] Access Panel':<{l_width}}        {f'[{self.status['panel']}]':<{r_width}} ║")
        print(f"║ {'[4] Emergency Fire Exit':<{l_width}}        {f'[{self.status['exit']}]':<{r_width}} ║")
        print(f"║ {'[0] Return':<{l_width + r_width + 8}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")


    # Security Room
    def security_room_ui(self):
        width = 55
        l_width, r_width = 22, 23

        # room scene
        print("╔" + "═" * width + "╗")
        print(f"║{'LOCATION: SECURITY ROOM'.center(width)}║")
        print("╠" + "═" * width + "╣")
        print(f"║{'':<{width}}║")
        print(f"║{'  [======]    [======]    [======]  '.center(width)}║")
        print(f"║{'  | CCTV |    | CCTV |    | CCTV |  '.center(width)}║")
        print(f"║{'  [======]    [======]    [======]  '.center(width)}║")
        print(f"║{'        ___________________         '.center(width)}║")
        print(f"║{'       | ACCESS LOG        |        '.center(width)}║")
        print(f"║{'       |___________________|        '.center(width)}║")
        print(f"║{'':<{width}}║")
        print(f"║ {'• The security hub. Monitors flicker with':<{width-2}} ║")
        print(f"║ {'  last night footage. Keycard rack on wall.':<{width-2}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

        # search spots
        print("╔" + "═" * width + "╗")
        print(f"║ {'SEARCH LOCATION: SECURITY ROOM'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║ {'[1] CCTV Monitor':<{l_width}}        {f'[{self.status['cctv']}]':<{r_width}} ║")
        print(f"║ {'[2] Access Log Terminal':<{l_width}}       {f'[{self.status['log']}]':<{r_width}} ║")
        print(f"║ {'[3] Guard Desk':<{l_width}}        {f'[{self.status['desk']}]':<{r_width}} ║")
        print(f"║ {'[4] Keycard Rack':<{l_width}}        {f'[{self.status['rack']}]':<{r_width}} ║")
        print(f"║ {'[0] Return':<{l_width + r_width + 8}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")


    # Dining Room
    def dining_room_ui(self):
        width = 55
        l_width, r_width = 22, 23

        # room scene
        print("╔" + "═" * width + "╗")
        print(f"║{'LOCATION: DINING HALL'.center(width)}║")
        print("╠" + "═" * width + "╣")
        print(f"║{'':<{width}}║")
        print(f"║{'  [-]  [-]  [-]  [-]  [-]  [-]  '.center(width)}║")
        print(f"║{'  |===========================|  '.center(width)}║")
        print(f"║{'  |      DINING  TABLE        |  '.center(width)}║")
        print(f"║{'  |===========================|  '.center(width)}║")
        print(f"║{'  [-]  [-]  [-]  [-]  [-]  [-]  '.center(width)}║")
        print(f"║{'':<{width}}║")
        print(f"║ {'• The grand hall where guests dined that night.':<{width-2}} ║")
        print(f"║ {'  Something was left behind in the chaos.':<{width-2}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

        # search spots
        print("╔" + "═" * width + "╗")
        print(f"║ {'SEARCH LOCATION: DINING HALL'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║ {'[1] Dinner Table':<{l_width}}        {f'[{self.status['table']}]':<{r_width}} ║")
        print(f"║ {'[2] Kitchen Counter':<{l_width}}        {f'[{self.status['kitchen']}]':<{r_width}} ║")
        print(f"║ {'[3] Trash Bin':<{l_width}}        {f'[{self.status['trash']}]':<{r_width}} ║")
        print(f"║ {'[4] Window Sill':<{l_width}}        {f'[{self.status['window']}]':<{r_width}} ║")
        print(f"║ {'[0] Return':<{l_width + r_width + 8}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")



class LocationCase2:
    """UI for Case 2: The Midnight Server Breach"""

    def __init__(self):
        self.status = {
            # Server Room Vault
            "rack": "Unsearched",
            "vent": "Unsearched",
            "terminal": "Unsearched",
            "power": "Unsearched",
            
            # Network Operations Center (NOC)
            "monitor": "Unsearched",
            "operator": "Unsearched",
            "firewall": "Unsearched",
            "trash": "Unsearched",
            
            # Chief Security Officer (CSO) Office
            "desk": "Unsearched",
            "safe": "Unsearched",
            "shredder": "Unsearched",
            "balcony": "Unsearched",
        }

    @staticmethod
    def visit_location_ui():
        width = 50
        print("╔" + "═" * width + "╗")
        print(f"║{'SELECT LOCATION TO VISIT'.center(width)}║")
        print("╠" + "═" * width + "╣")
        print(f"║ {'':<{width-2}} ║")
        print(f"║ {'[1] Server Room Vault':<{width-2}} ║")
        print(f"║ {'[2] Network Operations Center':<{width-2}} ║")
        print(f"║ {'[3] Chief Security Officer Office':<{width-2}} ║")
        print(f"║ {'[0] Return to Dashboard':<{width-2}} ║")
        print(f"║ {'':<{width-2}} ║")
        print("╚" + "═" * width + "╝")

    # ── 1. Server Room Vault ──────────────────────────────────────
    def server_room_vault(self):
        width = 55
        l_width, r_width = 22, 23
        dash = "-" * 5

        # Room Scene
        print("╔" + "═" * width + "╗")
        print(f"║ {'LOCATION: SERVER ROOM VAULT'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║     [{dash}]     [{dash}]     [{dash}]" + " " * 19 + "║")
        print(f"║     [RACK-A]    [RACK-B]    [RACK-C]" + " " * 18 + "║")
        print(f"║     [{dash}]     [{dash}]     [{dash}]" + " " * 19 + "║")
        print("║" + " " * width + "║")
        print(f"║ {'  • Cold air hums through the silent server aisle.':<{width-2}} ║")
        print(f"║ {'    Rack C access panel has been left unlatched.':<{width-2}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

        # Search Spots
        stat_rack = f"[{self.status['rack']}]"
        stat_vent = f"[{self.status['vent']}]"
        stat_term = f"[{self.status['terminal']}]"
        stat_powr = f"[{self.status['power']}]"

        print("╔" + "═" * width + "╗")
        print(f"║ {'SEARCH LOCATION: SERVER ROOM VAULT'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║ {'[1] Server Rack C':<{l_width}}         {stat_rack:<{r_width}}║")
        print(f"║ {'[2] Cooling Floor Vents':<{l_width}}        {stat_vent:<{r_width}}║")
        print(f"║ {'[3] Maintenance Terminal':<{l_width}}       {stat_term:<{r_width}}║")
        print(f"║ {'[4] Emergency Power Backup':<{l_width}}     {stat_powr:<{r_width}}║")
        print(f"║ {'[0] Return':<{l_width + r_width + 8}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")


    # ── 2. Network Operations Center (NOC) ────────────────────────
    def network_operations_center(self):
        width = 55
        l_width, r_width = 22, 23

        # Room Scene
        print("╔" + "═" * width + "╗")
        print(f"║ {'LOCATION: NETWORK OPERATIONS CENTER'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║     [---------------------------------]       {'║':>9}")
        print(f"║     |   NETWORK TRAFFIC: HIGH SPIKE   |       {'║':>9}")
        print(f"║     [---------------------------------]       {'║':>9}")
        print(f"║          [DESK-1]   [DESK-2]   [DESK-3]       {'║':>9}")
        print("║" + " " * width + "║")
        print(f"║ {'  • The monitoring wall shows massive data transfer.':<{width-2}} ║")
        print(f"║ {'    Desk 2 terminal was abandoned in a hurry.':<{width-2}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

        # Search Spots
        stat_mon  = f"[{self.status['monitor']}]"
        stat_oper = f"[{self.status['operator']}]"
        stat_fire = f"[{self.status['firewall']}]"
        stat_trsh = f"[{self.status['trash']}]"

        print("╔" + "═" * width + "╗")
        print(f"║ {'SEARCH LOCATION: NETWORK CENTER'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║ {'[1] Central Wall Monitor':<{l_width}}      {stat_mon:<{r_width}} ║")
        print(f"║ {'[2] Operator Desk':<{l_width}}        {stat_oper:<{r_width}} ║")
        print(f"║ {'[3] Firewall Log Printer':<{l_width}}     {stat_fire:<{r_width}} ║")
        print(f"║ {'[4] Paper Waste Bin':<{l_width}}        {stat_trsh:<{r_width}} ║")
        print(f"║ {'[0] Return':<{l_width + r_width + 8}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")


    # ── 3. Chief Security Officer (CSO) Office ────────────────────
    def cso_office(self):
        width = 55
        l_width, r_width = 22, 23

        # Room Scene
        print("╔" + "═" * width + "╗")
        print(f"║ {'LOCATION: CSO EXECUTIVE OFFICE'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║         ___________________________            {'║':>8}")
        print(f"║        |  EXECUTIVE GLASS DESK     |           {'║':>8}")
        print(f"║        |  [LAPTOP]     [WALL SAFE] |          {'║':>9}")
        print(f"║        |___________________________|           {'║':>8}")
        print("║" + " " * width + "║")
        print(f"║ {'  • Quiet luxury corner office. The wall safe':<{width-2}} ║")
        print(f"║ {'    behind the painting stands slightly unlocked.':<{width-2}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

        # Search Spots
        stat_desk = f"[{self.status['desk']}]"
        stat_safe = f"[{self.status['safe']}]"
        stat_shrd = f"[{self.status['shredder']}]"
        stat_balc = f"[{self.status['balcony']}]"

        print("╔" + "═" * width + "╗")
        print(f"║ {'SEARCH LOCATION: CSO OFFICE'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║ {'[1] Executive Desk':<{l_width}}        {stat_desk:<{r_width}} ║")
        print(f"║ {'[2] Open Wall Safe':<{l_width}}        {stat_safe:<{r_width}} ║")
        print(f"║ {'[3] Document Shredder':<{l_width}}        {stat_shrd:<{r_width}} ║")
        print(f"║ {'[4] Balcony Glass Door':<{l_width}}        {stat_balc:<{r_width}} ║")
        print(f"║ {'[0] Return':<{l_width + r_width + 8}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")


class LocationCase3:
    """UI for Case 3: The Poisoned Professor"""

    def __init__(self):
        self.status = {
            # Chemistry Lab
            "reagent": "Unsearched",
            "hood": "Unsearched",
            "logbook": "Unsearched",
            "sink": "Unsearched",
            
            # Professor's Study
            "tea": "Unsearched",
            "letter": "Unsearched",
            "drawer": "Unsearched",
            "basket": "Unsearched",
            
            # Faculty Lounge
            "coffee": "Unsearched",
            "fridge": "Unsearched",
            "board": "Unsearched",
            "gloves": "Unsearched",
        }

    @staticmethod
    def visit_location_case3():
        width = 50
        print("╔" + "═" * width + "╗")
        print(f"║{'SELECT LOCATION TO VISIT'.center(width)}║")
        print("╠" + "═" * width + "╣")
        print(f"║ {'':<{width-2}} ║")
        print(f"║ {'[1] Chemistry Research Lab':<{width-2}} ║")
        print(f"║ {'[2] Professor Personal Study':<{width-2}} ║")
        print(f"║ {'[3] Faculty Dining Lounge':<{width-2}} ║")
        print(f"║ {'[0] Return to Dashboard':<{width-2}} ║")
        print(f"║ {'':<{width-2}} ║")
        print("╚" + "═" * width + "╝")


    # ────────── Chemistry Research Lab ────────────
    def chemistry_lab(self):
        width = 55
        l_width, r_width = 22, 23

        # Room Scene
        print("╔" + "═" * width + "╗")
        print(f"║ {'LOCATION: CHEMISTRY RESEARCH LAB'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║         ___________________________            {'║':>8}")
        print(f"║        | [BEAKERS]    [ FUME HOOD] |           {'║':>8}")
        print(f"║        | [========]   [POISON CAB] |          {'║':>9}")
        print(f"║        |___________________________|           {'║':>8}")
        print("║" + " " * width + "║")
        print(f"║ {'  • Pungent chemical fumes hang in the air.':<{width-2}} ║")
        print(f"║ {'    A reagent bottle stands unsealed on the bench.':<{width-2}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

        # Search Spots
        stat_reag = f"[{self.status['reagent']}]"
        stat_hood = f"[{self.status['hood']}]"
        stat_logb = f"[{self.status['logbook']}]"
        stat_sink = f"[{self.status['sink']}]"

        print("╔" + "═" * width + "╗")
        print(f"║ {'SEARCH LOCATION: CHEMISTRY LAB'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║ {'[1] Poison Reagent Cabinet':<{l_width}}    {stat_reag:<{r_width}} ║")
        print(f"║ {'[2] Ventilation Fume Hood':<{l_width}}     {stat_hood:<{r_width}} ║")
        print(f"║ {'[3] Lab Research Logbook':<{l_width}}      {stat_logb:<{r_width}} ║")
        print(f"║ {'[4] Chemical Drain Sink':<{l_width}}       {stat_sink:<{r_width}} ║")
        print(f"║ {'[0] Return':<{l_width + r_width + 8}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

    # ──────── Professor Personal Study ───────────────────────────────
    def professor_study(self):
        width = 55
        l_width, r_width = 22, 23

        # Room Scene
        print("╔" + "═" * width + "╗")
        print(f"║ {'LOCATION: PROFESSOR STUDY'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║         ___________________________            {'║':>8}")
        print(f"║        |  MAHOGANY FACULTY DESK    |           {'║':>8}")
        print(f"║        |  [TEA MUG]   [EXAM STACK] |          {'║':>9}")
        print(f"║        |___________________________|           {'║':>8}")
        print("║" + " " * width + "║")
        print(f"║ {'  • Heavy shelves of antique volumes line the room.':<{width-2}} ║")
        print(f"║ {'    A half-finished mug of Earl Grey sits cold.':<{width-2}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

        # ────  Search Spots ──────
        stat_tea  = f"[{self.status['tea']}]"
        stat_lett = f"[{self.status['letter']}]"
        stat_draw = f"[{self.status['drawer']}]"
        stat_bask = f"[{self.status['basket']}]"

        print("╔" + "═" * width + "╗")
        print(f"║ {'SEARCH LOCATION: PROFESSOR STUDY'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║ {'[1] Cold Tea Mug & Saucer':<{l_width}}     {stat_tea:<{r_width}} ║")
        print(f"║ {'[2] Tenure Dispute Letter':<{l_width}}     {stat_lett:<{r_width}} ║")
        print(f"║ {'[3] Unlocked Desk Drawer':<{l_width}}      {stat_draw:<{r_width}} ║")
        print(f"║ {'[4] Waste Paper Basket':<{l_width}}        {stat_bask:<{r_width}} ║")
        print(f"║ {'[0] Return':<{l_width + r_width + 8}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

    # ──────── Faculty Dining Lounge ────────
    def faculty_lounge(self):
        width = 55
        l_width, r_width = 22, 23

        # Room Scene
        print("╔" + "═" * width + "╗")
        print(f"║ {'LOCATION: FACULTY DINING LOUNGE'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║         ___________________________            {'║':>8}")
        print(f"║        | COFFEE BAR & VEND MACHINE |           {'║':>8}")
        print(f"║        |  [KETTLE]     [TRASH CAN] |          {'║':>9}")
        print(f"║        |___________________________|           {'║':>8}")
        print("║" + " " * width + "║")
        print(f"║ {'  • Faculty gathered here before the seminar.':<{width-2}} ║")
        print(f"║ {'    Fine white powder dusts the sugar dispenser.':<{width-2}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")

        # Search Spots
        stat_coff = f"[{self.status['coffee']}]"
        stat_frid = f"[{self.status['fridge']}]"
        stat_boar = f"[{self.status['board']}]"
        stat_glov = f"[{self.status['gloves']}]"

        print("╔" + "═" * width + "╗")
        print(f"║ {'SEARCH LOCATION: FACULTY LOUNGE'.center(width-2)} ║")
        print("╠" + "═" * width + "╣")
        print("║" + " " * width + "║")
        print(f"║ {'[1] Coffee Machine Counter':<{l_width}}    {stat_coff:<{r_width}} ║")
        print(f"║ {'[2] Staff Refrigerator':<{l_width}}        {stat_frid:<{r_width}} ║")
        print(f"║ {'[3] Department Notice Board':<{l_width}}   {stat_boar:<{r_width}} ║")
        print(f"║ {'[4] Trash Under Sink':<{l_width}}        {stat_glov:<{r_width}} ║")
        print(f"║ {'[0] Return':<{l_width + r_width + 8}} ║")
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")


# if __name__ == "__main__":
    # loc3 = LocationCase3()
    # loc3.chemistry_lab()
    # loc3.professor_study()
    # loc3.faculty_lounge()
    # name, case, level, evd, sus, hint, pro, total_evidence=12, score=0):
    # UI.investigation_dashboard('bob', 'case001', 'hard', 5, 'alie', "hint1", 90)
    # UI.help_ui()
    # UI.interrogation_ui('alice', {'name':'alice', 'role':'listout', 'alibi':'unknow', 'motive':'unknow', 'status':"None"})