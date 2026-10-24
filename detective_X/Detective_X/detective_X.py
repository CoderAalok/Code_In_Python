# Libraries
from pathlib import Path
import re, ui, locations, evidence, notebook, timeline, compare, detective_system

# ------------  Config --------------:
base = Path(__file__).parent
FILE = base/"player_record.json"
FILE_INV = base/"investigation.json"

SYSTEM = detective_system.DetectiveSystem()
class GenerativeSystem:

    @staticmethod
    # player ID generation
    def player_id(file):
        player_record = SYSTEM.load_records(file)
        
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
        data = SYSTEM.load_records(FILE)
        
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
        
        SYSTEM.save_record(data, FILE)
        
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
        ui.ScreenUI.opening_screen()
        input("""\n               PRESS ENTER TO BEGIN       \n""")

        while True:
            width = 45
            
            print("╔" + "═" * (width) + "╗")
            print("║" + "Detective Start Menu".center(width) + "║") 
            print("╠" + "═" * (width) + "╣")
            print("║" + " " * (width) + "║")
            print(f"║ {'[1] Create New Detective':<{width-2}} ║")
            print(f"║ {'[2] Load Existing Detective':<{width-2}} ║")
            print(f"║ {'[0] Exit':<{width-3}}  ║")
            print("║" + " " * (width) + "║")
            print("╚" + "═" *(width) + "╝")
            
            try:
                player = int(input("Select option [0-2]: ").strip())
                
                if player not in [0, 1, 2]:
                    print("Invalid input! Only select [0], [1] or [2].")
                    
                elif player == 0:
                    print("\nThank you for play.")
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
                    player_id = SYSTEM.load_records(FILE)

                    # user id
                    id = input("Your ID (hint: Pxxxx):\n⮩ ").strip()
                    record = player_id.get(id)
                    self.id = id
                    
                    # check player exist
                    if not record:
                        print("Player not found!")
                        continue

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

        
    def select_case(self, id: str):  # -> call by main()
        player_data = SYSTEM.load_records(FILE)
        
        while True:
            # cases are show up
            ui.CaseUI.case_library()

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
                SYSTEM.save_record(player_data, FILE)
                
                # call case_briefing() -> investigation dashboard or back to case library
                case_briefing(id, case_id)
                return
                
                                
            except Exception as e:
                print(f"ERROR: {e}")
                return 

    def investigation_state(self, detective, detective_id, case_id, level):
        # fetch investigation record
        data_inv = SYSTEM.load_records(FILE_INV)

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
                    "Contradictions": [],
                    "Comparisons": [],
                    "Hints": {
                        "Available": ["hint_1", "hint_2", "hint_3"],  # By default
                        "Used": [],
                    },
                    "Scores": 0,
                    "Progress": 0,
                }
            )

        # save record
        SYSTEM.save_record(data_inv, FILE_INV)
        return 


DS = GenerativeSystem()
PG = PlayerGround()   


# --------------- MAIN --------------------
def main(player_id: str):

    while True:
        # show up main menu
        ui.ScreenUI.main_menu()

        # menu options
        menu_options = {
            1: 'Start New Case',
            2: 'Continue Investigation',
            3: 'Detective Profile',
            4: 'Case Records',
            5: 'Help',
            0: 'Exit'
        }

        # funtions
        call_func = {
            1: PG.select_case,
            2: continue_investigation,
            3: ui.ScreenUI.detective_profile,
        }

        try:
            select = int(input("Select option [0-5]: ").strip())
            if menu_options.get(select):
                
                # CALL -> select_case
                if select == 1:
                    call_func[select](player_id)

                # CALL -> continue investigation
                elif select == 2:
                    call_func[select](player_id)

                # Call -> load player's record
                elif select == 3:
                    # load player records
                    records = SYSTEM.load_records(FILE)[player_id]

                    if not records:
                        print("Record not found!")
                        return
                    
                    # show -> detective profile
                    call_func[select](records)

                # Call -> Case record
                elif select == 4:
                    case_records(player_id)

                # Call -> help to see how to play
                elif select == 5:
                    help()

                # Exit from game
                elif select == 0:
                    return
            
            else:
                print("Invalid option. select only [0-5].")
                continue
                
        except Exception as e:
            print(f"Error: {e}")
            continue



# ----------- CASE BRIEFING ---------------
def case_briefing(player_id: str, case_id: str):
    # load detective record
    player_data = SYSTEM.load_records(FILE)

    # load investigation record
    investigation_data = SYSTEM.load_records(FILE_INV)

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
    
    if active_record is None:
        print("Investigation record not found!")
        return

    KEYS = ['Detective', 'Difficulty', 'Evidence', 'Suspects', 'Hints', 'Scores', 'Progress']
    name, level, evidence, suspects, hints, score,  prog = [active_record[record] for record in KEYS]
    evid = len(evidence)
    susp = len(suspects)
    hint = len(hints['Used'])

    # BY DEFAULT: Available Hints = 3
    
    while True:
        # call case briefing ui -> display case options
        ui.CaseUI.case_briefing_ui()
        try:
            briefing_option = int(input("Select case briefing [0-2]: ").strip()) 
            cases = {
                1: ui.InvestigationUI.investigation_dashboard,
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
                    cases[briefing_option](name, case_id, level, evid, susp, hint, prog, score)

                    # save updated record
                    SYSTEM.save_record(player_data, FILE)
                    SYSTEM.save_record(investigation_data, FILE_INV)
                    
                    # call -> investigation action
                    investigation_action(player_id, case_id)
                    return
                    
                else:
                    cases[briefing_option](player_id)
                    
            elif briefing_option == 0:
                # save updated record
                SYSTEM.save_record(player_data, FILE)
                SYSTEM.save_record(investigation_data, FILE_INV)
                return
            
            else:
                print("Invalid option.")
                continue
            
        except Exception as e:
            print(f"Error: {e}")
            continue 


# ----------- CONTINUE INVESTIGATION ---------------
def continue_investigation(player_id: str):
    # load player's record
    record = SYSTEM.load_records(FILE_INV)

    # fetch player record
    player_inv = record.get(player_id)
    
    if not player_inv:
        print("Record is empty!")
        return

    while True:
        try:
            # fetch case id
            case_id = input("Enter your Case ID (e.g. case_001): ").strip().lower()

            norm_case_id = case_id.split("_")
            
            # verify case id
            if (
                norm_case_id[0].isalpha() and
                norm_case_id[-1].isdigit() and
                1 <= int(norm_case_id[-1]) <= 3
            ):
                is_exist = next(
                    (True for rec in player_inv if rec['Case'] == case_id),
                    False
                )

                if not is_exist:
                    print("[!] Case ID not found")
                    continue 
                
                # call -> case briefing
                case_briefing(player_id, case_id)
                return

            else:
                print("[!] Case ID does not match.")
                continue 
             
        except Exception as e:
            print(f"Error: {e}")
        

# ----------- CASE RECORDS ---------------
def case_records(player_id: str):
    # load cases from investigation.json
    inv = SYSTEM.load_records(FILE_INV)
    
    records = inv.get(player_id, [])

    if not records:
        print("[!] No records found.")
        return

    width = 57
    # print simple box
    print("╔" + "═" * (width) + "╗")
    print(f"║{'CASE RECORDS'.center(width)}║")

    # case record show in formate
    for record in records:
        print("╠" + "═" * width + "╣")
        print(f"║ Case     : {record['Case']:<{width-13}} ║")
        print(f"║ Clues    : {len(record['Evidence'])}/12{'':<{width-16}}║")
        print(f"║ Progress : {SYSTEM.progress_bar(record['Progress']):<{width-12}}║")
        print(f"║ Score    : {record['Scores']:<{width-12}}║")
    print("╚" + "═" * width + "╝")

    return

# ----------- HELP/SUPPORT ---------------
def help():
    """This function job is to guide the new player HOW TO PLAY?"""
    GUIDE = {
        1: "Search locations, find 12 clues, question suspects, and accuse the true culprit.",
        2: "Enter numbers at each menu to inspect rooms, talk to suspects, or view records.",
        3: "Visit all 3 crime scenes per case. Each room contains 4 distinct spots to search.",
        4: "Start at 1000 pts. Clues give +30, contradictions +50. Hints cost -50. Climb from Rookie to Master Detective!",
        5: "Track your clue discovery '%' in the dashboard. Each found clue adds ~8% progress.",
        6: "Use hints if you get stuck finding evidence, but remember they deduct 50 points!",
    }

    while True:
        # display Guide Lines/ Help UI
        ui.CaseUI.help_ui()
        try:
            guide_option = int(input("Select guide [0-6]: ").strip())
            if guide_option == 0:
                return # exit
            
            if guide_option not in GUIDE:
                print("[!] Invalid option.")
                continue

            # show guide
            print(f"\n➥  {GUIDE[guide_option]}\n")
                
        except ValueError as e:
            print(f"Error: {e}")
            continue


# ------------------- INVESTIGATION ACTION -------------------
def investigation_action(player_id, case_id):
    import suspects
    
    actionable_func = {
        1: locations.main,
        2: suspects.Dispatch.question_suspects,
        4: suspects.Dispatch.view_suspect_profiles,
        
    }

    # ------- INVESTIGATION LOOP -------
    while True:
        # fetch existing data
        investigation_data = SYSTEM.load_records(FILE_INV)
        player_data = SYSTEM.load_records(FILE)

        # get the active case record
        active_record = next(
            (record for record in investigation_data.get(player_id, []) if record["Case"] == case_id),
            None
        )

        if not active_record:
            print("Investigation record not found!")
            return

        # extract saved record
        KEYS = ['Detective', 'Difficulty', 'Evidence', 'Suspects', 'Hints', 'Scores', 'Progress']
        name, level, _evidence, _suspects, hints, score, progress = [active_record[record] for record in KEYS]
        evid = len(_evidence)
        susp = len(_suspects)
        hint = len(hints["Used"])
        prog = SYSTEM.progress_bar(progress)

        # show dashboard
        ui.InvestigationUI.investigation_dashboard(name, case_id, level, evid, susp, hint, prog, score)
        
        # UI -> Investigation action
        ui.InvestigationUI.investigation_action_ui()

        try:
            action = int(input("Select action [0-9]: ").strip())

            if action == 0:
                # save and exit to main menu
                SYSTEM.save_record(investigation_data, FILE_INV)
                SYSTEM.save_record(player_data, FILE)
                print("[✓] Progress saved.")
                return

            # visit location
            elif action == 1:
                actionable_func[action](player_id, case_id)

            # Question Suspects
            elif action == 2:
                actionable_func[action](player_id, case_id)

            # Examine Evidence
            elif action == 3:
                # examine collected evidence
                print("\nEvidence Collected")
                evidence.ExamineEvidence().examine_evidence(player_id, case_id)

            # View Suspect Profiles
            elif action == 4:
                actionable_func[action](player_id, case_id)

            # Investigation Notebook
            elif action == 5:
                notebook.InvestigationNotebook.display_notebook(player_id, case_id)
                
            # Crime timeline
            elif action == 6:
                timeline.TimeLine.time_line(player_id, case_id)

            # Compare evidence
            elif action == 7:
                compare.CompareEvidence.compare_evidence(player_id, case_id)

            # Hint system
            elif action == 8:
                import hints
                hints.HintSystem.request_hint(player_id, case_id)
            
            # Final Accusation
            elif action == 9:
                import accusation
                ended = accusation.FinalAccusation.final_accusation(player_id, case_id)
                if ended:
                    return

            else:
                print("[!] Invalid option. Select [0-9].")

        except ValueError:
            print("[!] Please enter a number.")
    
        except Exception as e:
            print(f"Error: {e}")

