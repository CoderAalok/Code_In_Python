# Libraries
import json
from pathlib import Path
import re, ui, locations


#  Config:
base = Path(__file__).parent
FILE = base/"player_record.json"
FILE_INV = base/"investigation.json"

class DetectiveSystem:

    # player details save
    def save_details(self, data, file):
        with open(file, 'w') as fw:
            json.dump(data, fw, indent=4) 
        return

    # load player details
    def load_details(self, file):
        try:
            with open(file) as fr:
                return json.load(fr)
        except (FileNotFoundError ,  json.decoder.JSONDecodeError):
            return {}

    # player ID generation
    def player_id(self, file):
        player_record = self.load_details(file)
        if not player_record:
            id = "P0001"
            return id

        # last player id extract
        id = list(player_record.keys())[-1]
        id_num = int(id[1:]) + 1 
        
        # new player id
        return  f"P{id_num:04d}" if id_num < 10000 else "Player full!"


    # new account details 
    def account_verify(self, name=None):
        # load data
        data = self.load_details(FILE)
        
        if not name:
            return None, "Requirement not full fill."

        name_pattern = re.compile(r"^[A-Za-z ]+$")
        if not name_pattern.fullmatch(name):
            return None, "Name should only contains character and space."

        # generate player ID
        id = self.player_id(FILE)
        if id == "Player full!":
            return None, "Player full!"

        # record save
        data[id] = {
            "Name": name,
            "Rank": 'Rookie',
            "Cases_Won": 0,
            "Cases_Lost": 0,
            "XP": 0,
            "Rating": 0,
            "Pending_Cases": [],
            "Active_Case": None,
            "Completed_Cases": [],
        }
        
        self.save_details(data, FILE)
        
        player_info = data.get(id)
        return [player_info, id], "Successfully your account has been created."


    @staticmethod
    def get_cases_library():
        cases = {
            1: {
                "title": "the missing diamond",
                "difficulty": "easy",
                "location": "Blackwood Mansion",
                "objective": "Identify the thief and recover the missing diamond.",
            },
            2: {
                "title": "the midnight server breach",
                "difficulty": "medium",
                "location": "Hunted area",
                "objective": "Trace the hacker, uncover the breach method, and secure the stolen data.",
            },
            3: {
                "title": "the poisoned professor",
                "difficulty": "hard",
                "location": "university",
                "objective": "Determine who administered the poison and uncover their motive.",
            },

        }

        return cases
        
    @staticmethod
    def case_briefing_screen():
        brief = {
            1: "A priceless diamond vanished during a charity gala with no signs of forced entry.",
            2: "Confidential company data was stolen after a suspicious midnight network intrusion.",
            3: "A renowned professor collapsed after a faculty dinner under mysterious circumstances.",
        }

        return brief
    
class PlayerGround:
    def __init__(self):
        self.id = None
        
    def get_start(self):
        ui.UI.opening_screen()
        input("""\n               PRESS ENTER TO BEGIN       \n""")

        while True:
            width = 45
            
            print("╔" + "═" * (width) + "╗")
            print("║" + "Detective Start Menu".center(width) + "║") 
            print("╠" + "═" * (width) + "╣")
            print("║" + " " * (width) + "║")
            print(f"║ {'[1] Create New Detective':<{width-2}} ║")
            print(f"║ {'[2] Load Existing Detective':<{width-2}} ║")
            print(f"║ {'[3] Exit':<{width-3}}  ║")
            print("║" + " " * (width) + "║")
            print("╚" + "═" *(width) + "╝")
            
            try:
                player = int(input("Select option [1-3]: ").strip())
                
                if not player in {1, 2, 3}:
                    print("Invalid input! Only select [1], [2] or [3].")
                    
                elif player == 3:
                    print("\nPlay next time.")
                    return # exit from game
                
                # create new detective identity
                elif player == 1:
                    player_name = input("\nYour name: ").strip().lower().title()
                    
                    data, message = (DS.account_verify(player_name))                    
                    if not data:
                        print("Data is not found!")
                        return

                    details, self.id = data
                    
                    key_width = 18
                    value_width = 28
                    box_width = key_width + value_width + 5

                    print(message)
                    print(f"\n[✓] Detective Profile created for {player_name}!")

                    print("╔" + "═" * box_width + "╗")

                    print(f"║{str(self.id).center(box_width)}║")

                    print("╠" + "═" * box_width + "╣")

                    for key, value in details.items():
                        print(f"║ {key:<{key_width}} :  {str(value):<{value_width}}║")

                    print("╚" + "═" * box_width + "╝")

                
                elif player == 2:
                    player_id = DS.load_details(FILE)

                    # user id
                    id = input("Your ID (hint: Pxxxx):\n⮩ ").strip()
                    record = player_id.get(id)
                    self.id = id
                    
                    # check player exist
                    if not record:
                        print("Player not found!")
                        return

                    # loaded greet
                    print(f"\n[✓] Loaded Detective Profile successfully for {record['Name']} [{record['Rank']}]!")
                  
                # Check: Whether ID exist  
                if not self.id:
                    print("Required ID but None is found!")
                    return
                
                # call main() -> main_menu
                main(self.id)

            except Exception as e:
                print(f"Error: {e}")
                continue

        
    @staticmethod
    def select_case(id: str):  # -> call by main()
        player_data = DS.load_details(FILE)
        
        while True:
            # cases are show up
            ui.UI.case_library()

            try:
                case = int(input("Select case [0-3]: ").strip())
                
                # return back to -> main()
                if case == 0:
                    return 
                
                # create: case number convert into case id
                case_id = f"case_{case:03d}"
                
                # check case validity
                cases = DS.get_cases_library()
                brief = DS.case_briefing_screen()
            
                # check whether selected case exist
                if case not in cases:
                    print("Selected case is not available.")
                    continue

                # read briefing
                width = 85
                print("╔" + "═" * width + "╗")
                print(f"║{'CASE-ID: ' f'[{case_id}]'.center(width-2)}  ║")
                print("╠" + "═" * width + "╣")

                print(f"║ {'• Case       : ' + cases[case]['title'].title():<{width-2}} ║")
                print(f"║ {'• Difficulty : ' + cases[case]['difficulty'].title():<{width-2}} ║")
                print(f"║ {'• Location   : ' + cases[case]['location'].title():<{width-2}} ║")

                width1 = 85
                print("╠" + "═" * width1 + "╣")
                print(f"║{'READ BRIEF'.center(width1)}║")
                print("╠" + "═" * width1 + "╣")

                print(f"║{'• Briefing:':<{width1}}║")
                print(f"║{brief[case]:<{width1}}║")

                print("╠" + "═" * width1 + "╣")

                print(f"║{'• Objective:':<{width1}}║")
                print(f"║{cases[case]['objective']:<{width1}}║")

                print("╚" + "═" * width1 + "╝")


                # check case is pending
                if case_id not in player_data[id]["Pending_Cases"]:
                    player_data[id]["Pending_Cases"].append(case_id)
                    
                # case activate
                player_data[id]["Active_Case"] = case_id
                
                # create new investigation
                player_name = player_data[id]["Name"]
                level = DS.get_cases_library()[case]["difficulty"]

                # pass argument into investigation
                PG.investigation_state(player_name, id, case_id, level)

                # save updated record
                DS.save_details(player_data, FILE)
                
                # call case_briefing() -> investigation dashboard or back to case library
                case_briefing(id, case_id)
                return
                
                                
            except Exception as e:
                print(f"ERROR: {e}")
                return 


    @staticmethod
    def investigation_state(detective, detective_id, case_id, level):
        # fetch investigation record
        data_inv = DS.load_details(FILE_INV)

        # add/append records -> data_inv 
        existing_data = data_inv.setdefault(detective_id, [])
        if not any(data["Case"] == case_id for data in existing_data):
            existing_data.append(
                {
                    "Detective": detective,
                    "Case": case_id,
                    "Difficulty": level,
                    "Evidence": [],
                    "Suspects": [],
                    "Hints": {
                        "Available": [],
                        "Used": [],
                    },
                    "Scores": 0,
                    "Progress": 0,
                }
            )

        # save record
        DS.save_details(data_inv, FILE_INV)
        return 


DS = DetectiveSystem()
PG = PlayerGround()   


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


def main(player_id: str):

    while True:
        # show up main menu
        ui.UI.main_menu()

        # menu options
        menu_options = {
            1: 'Start New Case',
            2: 'Continue Investigation',
            3: 'Detective Profile',
            4: 'Case Records',
            5: 'Help',
            6: 'Exit'
        }

        # funtions
        call_func = {
            1: PG.select_case,
            3: detective_profile,
        }

        try:
            select = int(input("Select option [1-6]: ").strip())
            if menu_options.get(select):
                # call -> select_case()
                if select == 1:
                    call_func[select](player_id)
                    
                elif select == 2:
                    #later: add continuous  investigation  
                    print("This features not added yet.")

                elif select == 3:
                    # load player records
                    records = DS.load_details(FILE)[player_id]
                    
                    # detective profile
                    detective_profile(records)
                
                elif select == 4:
                    # later : case record  add
                    print("Case record not found.")

                elif select == 5:
                    # Help
                    print("This feature not added yet.")
                    
                elif select == 6:
                    print("Play next time.")
                    return
            
            else:
                print("Invalid option. select only [1-6].")
                continue
                
        except Exception as e:
            print(f"Error: {e}")
            continue


# curr_progress in %
def progress_bar(curr_progress, width=10):
    # curr_progress between 0 and 100
    progress = max(0.0, min(100.0, float(curr_progress)))
    
    # filled bar
    filled = int((progress / 100 ) * width)
    # empty bar
    empty = width - filled
    
    prog_bar = "█" * filled  + "░" * empty
    return f"{prog_bar} {progress:.1f}%"


def case_briefing(player_id, case_id):

    # load detective record
    player_data = DS.load_details(FILE)

    # load investigation record
    investigation_data = DS.load_details(FILE_INV)

    if not player_data or not investigation_data:
        print("Data is empty.")
        return 

    existing_investigation = investigation_data.get(player_id)  # list of dictonary 
    if not existing_investigation:
        print("Investigation is no found!")
        return
    
    active_record = next(
        (record for record in existing_investigation if record['Case'] == case_id), 
        None
    ) # -> dictionary
    
    if not active_record:
        print("Investigation record not found!")
        return

    RECORDS = ['Detective', 'Difficulty', 'Evidence', 'Suspects', 'Hints', 'Progress']
    name, level, evidence, suspects, hints, prog = [active_record[record] for record in RECORDS]
    evid = len(evidence)
    susp = len(suspects)
    hint = len(hints['Used'])
    
    while True:
        # call case briefing ui -> display case options
        ui.UI.case_briefing_ui()
        try:
            briefing_option = int(input("Select case briefing [0-2]: ").strip()) 
            cases = {
                1: ui.UI.investigation_dashboard,
                2: PG.select_case
            }
            
            if cases.get(briefing_option):
                if briefing_option == 1:

                    if case_id not in player_data[player_id]['Pending_Cases']:
                        # pending case
                        player_data[player_id]['Pending_Cases'].append(case_id)

                    # case active
                    player_data[player_id]["Active_Case"] = case_id
                    
                    # investigation dashboard
                    cases[briefing_option](name, case_id, level, evid, susp, hint, prog)

                    # save updated record
                    DS.save_details(player_data, FILE)
                    DS.save_details(investigation_data, FILE_INV)
                    
                    # call -> investigation action
                    investigation_action(player_id, case_id)
                    return
                    
                else:
                    cases[briefing_option](player_id)
                    
            elif briefing_option == 0:
                # save updated record
                DS.save_details(player_data, FILE)
                DS.save_details(investigation_data, FILE_INV)
                return
            
            else:
                print("Invalid option.")
                continue
            
        except Exception as e:
            print(f"Error: {e}")
            continue 



# ------------------- INVESTIGATION ACTION -------------------
def investigation_action(player_id, case_id):
    actionable_func = {
        1: locations.main
    }

    # ------- INVESTIGATION LOOP -------
    while True:
        # fetch existing data
        investigation_data = DS.load_details(FILE_INV)
        player_data = DS.load_details(FILE)

        # get the active case record
        active_record = next(
            (record for record in investigation_data.get(player_id, []) if record["Case"] == case_id),
            None
        )

        if not active_record:
            print("Investigation record not found!")
            return

        # extract fresh stats
        RECORDS = ['Detective', 'Difficulty', 'Evidence', 'Suspects', 'Hints', 'Scores', 'Progress']
        name, level, evidence, suspects, hints, score, progress = [active_record[record] for record in RECORDS]
        evid = len(evidence)
        susp = len(suspects)
        hint = len(hints["Used"])
        prog = progress_bar(progress)

        # show dashboard
        ui.UI.investigation_dashboard(name, case_id, level, evid, susp, hint, prog, score)
        
        # UI -> Investigation action
        ui.UI.investigation_action_ui()

        try:
            action = int(input("Select action [0-9]: ").strip())

            if action == 0:
                # save and exit to main menu
                DS.save_details(investigation_data, FILE_INV)
                DS.save_details(player_data, FILE)
                print("[✓] Progress saved.")
                return

            # visit location
            elif action == 1:
                actionable_func[action](player_id, case_id)

            # Question Suspects
            elif action == 2:
                print("[!] Question Suspects Coming soon.")

            # Examine Evidence
            elif action == 3:
                # examine collected evidence
                if evidence:
                    print("\nEvidence Collected")
                    for i, ev in enumerate(evidence, 1):
                        print(f"  {i}. {ev}")
                else:
                    print("[!] No evidence collected yet.")

            # View Suspect Profiles
            elif action == 4:
                # view suspect list
                if suspects:
                    print("\nSuspects Identified")
                    for i, sus in enumerate(suspects, 1):
                        print(f"  {i}. {sus}")
                else:
                    print("[!] No suspects identified yet.")

            # Investigation Notebook
            elif action == 5:
                print("[!] Investigation Notebook Coming soon.")

            # Crime timeline
            elif action == 6:
                print("[!] Crime Timeline Coming soon.")

            # Compare evidence
            elif action == 7:
                print("[!] Compare Evidence Coming soon.")

            # Hint system
            elif action == 8:
                print("[!] Hint System Coming soon.")

            # Final Accusation
            elif action == 9:
                print("[!] Final Accusation Coming soon.")

            else:
                print("[!] Invalid option. Select [0-9].")

        except ValueError:
            print("[!] Please enter a number.")
    
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    PlayerGround().get_start()