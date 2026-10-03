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
            4: {
                "title": "murder at blackwood hotel",
                "difficulty": "hard",
                "location": "blackwood hotel",
                "objective": "Solve the locked-room murder and identify the killer.",
            },
            5: {
                "title": "the vanishing programmer",
                "difficulty": "medium",
                "location": "tech park",
                "objective": "Find the missing programmer and uncover the reason behind the disappearance.",
            },
            6: {
                "title": "the museum switch",
                "difficulty": "medium",
                "location": "city museum",
                "objective": "Discover how the switch occurred and recover the real artifact.",
            },
            7: {
                "title": "the anonymous letter",
                "difficulty": "easy",
                "location": "downtown post office",
                "objective": "Track down the sender and determine their intentions.",
            },
            8: {
                "title": "the midnight train",
                "difficulty": "hard",
                "location": "central station",
                "objective": "Reconstruct the events on board and solve the disappearance.",
            }
        }

        return cases
        
    @staticmethod
    def case_briefing_screen():
        brief = {
            1: "A priceless diamond vanished during a charity gala with no signs of forced entry.",
            2: "Confidential company data was stolen after a suspicious midnight network intrusion.",
            3: "A renowned professor collapsed after a faculty dinner under mysterious circumstances.",
            4: "A wealthy guest was found dead in a locked hotel suite late at night.",
            5: "A software developer disappeared days before releasing a revolutionary application.",
            6: "An ancient artifact was secretly replaced with an almost perfect replica.",
            7: "A series of threatening letters has caused panic throughout the city.",
            8: "A passenger disappeared from a moving train without leaving any evidence behind.",
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
                        return

                    details, id = data
                    
                    key_width = 18
                    value_width = 28
                    box_width = key_width + value_width + 5

                    print(message)
                    print(f"\n[✓] Detective Profile created for {player_name}!")

                    print("╔" + "═" * box_width + "╗")

                    print(f"║{str(id).center(box_width)}║")

                    print("╠" + "═" * box_width + "╣")

                    for key, value in details.items():
                        print(f"║ {key:<{key_width}} :  {str(value):<{value_width}}║")

                    print("╚" + "═" * box_width + "╝")

                
                elif player == 2:
                    player_id = DS.load_details(FILE)

                    # user id
                    self.id = input("Your ID (hint: Pxxxx):\n⮩ ").strip()
                    record = player_id.get(self.id)

                    # check player exist
                    if not record:
                        print("Player not found!")
                        return

                    # loaded greet
                    print(f"\n[✓] Loaded Detective Profile successfully for {record['Name']} [{record['Rank']}]!")
                    
                # call main() -> main_menu
                main(self.id)
                return

            except Exception as e:
                print(f"Error: {e}")

        
    @staticmethod
    def select_case(id):  # -> call by main()
        data = DS.load_details(FILE)
        
        while True:
            # cases are show up
            ui.UI.case_library()

            try:
                case = int(input("Select case [0-8]: ").strip())
                
                # create case id
                case_id = "case_{case:03d}"
                
                # check case validity
                cases = DS.get_cases_library()
                brief = DS.case_briefing_screen()
                
                # return back to main
                if case == 0:
                    return 

                # check existing case
                if case not in cases:
                    print("Case is not found.")
                    continue

                
                # read briefing
                width = 85
                print("╔" + "═" * width + "╗")
                print(f"║{'CASE-ID [{case_id}] '.center(width)}║")
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
                if case not in data[id]["Pending_Cases"]:
                    data[id]["Pending_Cases"].append(case)
                    
                # case activate
                data[id]["Active_Case"] = case
                
                # create new investigation
                name = data[id]["Name"]
                level = DS.get_cases_library()[case]["difficulty"]
                case_title = DS.get_cases_library()[case]["title"].title()
                PG.investigation_state(name, id, case_title, level)

                # save updated record
                DS.save_details(data, FILE)
                
                # call case_briefing() -> investigation dashboard or back to case library
                case_briefing(id, case_id)
                return
              
                                
            except Exception as e:
                print(f"ERROR: {e}")
                return 

    @staticmethod
    def investigation_state(detective, detective_id, case, level):

        data_inv = DS.load_details(FILE_INV)
        
        data_inv[detective_id] =  {
            "Detective": detective,
            "Case": case,
            "Difficulty": level,
            "Evidence": [],
            "Suspects": [],
            "Hints": {
                "Available": [],
                "Used": [],
            },
            "Scores": 1000,
            "Progress": 0,
        }

        # save record
        DS.save_details(data_inv, FILE_INV)
        return 


DS = DetectiveSystem()
PG = PlayerGround()   


def detective_profile(records):
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


def main(player_id):

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
                    print("Feature not added.")
                    
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
    data1 = DS.load_details(FILE)

    # load investigation record
    data2 = DS.load_details(FILE_INV)

    if not data1 or not data2:
        print("Data is empty.")
        return 

    name, _, level, evidence, suspects, hints, _, progress = list(data2[player_id].values()) 
    hint = len(hints['Used'])
    evid = len(evidence) 
    susp = len(suspects)
    prog = progress_bar(progress)
    
    while True:
        # call case briefing ui -> display case options
        ui.UI.case_briefing_ui()
        try:
            briefing_option = int(input("Select case briefing [1-2]: ").strip()) 
            cases = {
                1: ui.UI.investigation_dashboard,
                2: PG.select_case
            }
            
            if cases.get(briefing_option):
                if briefing_option == 1:

                    if case_id not in data1[player_id]['Pending_Cases']:
                        # pending case
                        data1[player_id]['Pending_Cases'].append(case_id)

                    # case active
                    data1[player_id]["Active_Case"] = case_id
                    
                    # investigation dashboard
                    cases[briefing_option](name, case_id, level, evid, susp, hint, prog)

                    # investigation action
                    

                else:
                    cases[briefing_option](player_id)
                    
            elif briefing_option == 0:
                # save updated record
                DS.save_details(data1, FILE)
                DS.save_details(data2, FILE_INV)
                return
            
            else:
                print("Invalid option.")
                continue
            
        except Exception as e:
            print(f"Error: {e}")
            continue 




def investigation_action():
    # display actionable options
    ui.UI.investigation_action_ui()

    try:
        action_option = int(input("Select action [0-9]").strip())
        actionable_func = {
            1: locations.Location.visit_location,
        }
    
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    PlayerGround().get_start()