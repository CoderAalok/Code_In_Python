# Libraries
import json
from pathlib import Path
import re, ui


#  Config:
base = Path("__file__").parent
FILE = base/"player_record.json"


class DetectiveSystem:

    # player details save
    def save_details(self, data):
        with open(FILE, 'w') as fw:
            json.dump(data, fw, indent=4) 
        return

    # load player details
    def load_details(self):
        try:
            with open(FILE) as fr:
                return json.load(fr)
        except (FileNotFoundError ,  json.decoder.JSONDecodeError):
            return {}

    # player ID generation
    def player_id(self):
        player_rec = self.load_details()
        if not player_rec:
            id = "P0001"
            return id

        # last player id extract
        id = list(player_rec.items())[-1][-1]
        id_num = int(id[1:]) + 1
        
        if id_num > 9999:
            return "Player full!"

        # new player id
        return  f"P{id_num:04d}"


    # new account details 
    def account_verify(self, name=None):
        # load data
        data = self.load_details()
        
        if not name:
            return (None, "Requirement not full fill.")

        name_pattern = re.compile(r"[A-Za-z]+")
        if not name_pattern.fullmatch(name):
            return (None, "Name should only contains character and space.")

        id = self.player_id()
        if id == "Player full!":
            return "Player full!"

        # record save
        data[id] = name
        self.save_details(data)
        
        return (data, "Successfully account has been created.")

    @staticmethod
    def get_cases_library():
        cases = {
            1: {
                "title": "the missing diamond",
                "difficulty": "easy",
                "location": "adc",
                "objective": "Identify the thief and recover the missing diamond.",
            },
            2: {
                "title": "the midnight server breach",
                "difficulty": "medium",
                "location": "xyz",
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
        briefing = {
            1: """A priceless diamond vanished during a\n charity gala with no signs of forced entry.""",
            2: """Confidential company data was stolen after a suspicious midnight network intrusion.""",
            3: """A renowned professor collapsed after a faculty dinner under mysterious circumstances.""",
            4: "A wealthy guest was found dead in a locked hotel suite late at night.",
            5: "A software developer disappeared days before releasing a revolutionary application.",
            6: "An ancient artifact was secretly replaced with an almost perfect replica.",
            7: "A series of threatening letters has caused panic throughout the city.",
            8: "A passenger disappeared from a moving train without leaving any evidence behind.",
        }

        return briefing

player_details = DetectiveSystem()
         
class PlayerGround:
    @staticmethod
    def get_start():

        while True: 
            print("[1] Create New Detective")
            print("[2] Load Existing Detective")
            print("[3] Exit\n")
            
            try:
                player = int(input("Player: ").strip())
                
                if not player in {1, 2, 3}:
                    print("Invalid input! Only select [1], [2] or [3].")
                    
                elif player == 3:
                    print("\nPlay next time.")
                    return # exit from game
                
                # create new detective identity
                elif player == 1:
                    player_name = input("\nYour name: ").strip().lower()
                    
                    details, message = (player_details.account_verify(player_name))
                    print(message)
                    print("Your details:")
                    
                    if not details:
                        return
                    
                    width = 20
                    for id, detail in details.items():
                        print("╔" + "═" * width + "╗")
                        print(f"║ {'Name : ' + detail['Name']:<18} ║")
                        print(f"║ {'ID   : ' + str(id):<18} ║")
                        print(f"║ {'':<18} ║")
                        print("╚" + "═" * width + "╝")
                        
                elif player == 2:
                    players_id = player_details.load_details()

                    # user id
                    id = input("Your ID (hint: Pxxxx):\n⮩ ").strip()
                    
                    if not id in players_id:
                        return "Player not found!"

                    # Player/Detective profile show
                    
                # call main function  
                main()

            except Exception as e:
                print(f"Error: {e}")
        
    @staticmethod
    def select_case():
        while True:
            # print cases
            ui.UI.case_library()

            try:
                case = int(input("Select a case: ").strip())
                # check case validity
                cases = player_details.get_cases_library()
                brief = player_details.case_briefing_screen()
                
                if case not in cases:
                    print("Case is not vaild.")

                # read the briefing
                width = 60
                print("╔" + "═" * width + "╗")
                print(f"║{'READ CAREFULLY'.center(width)}║")
                print("╠" + "═" * width + "╣")

                print(f"║ {'• Case       : ' + cases[case]['title'].title():<58} ║")
                print(f"║ {'• Difficulty : ' + cases[case]['difficulty'].title():<58} ║")
                print(f"║ {'• Location   : ' + cases[case]['location'].title():<58} ║")

                print("╠" + "═" * width + "╣")

                print(f"║ {'• Briefing:':<58} ║")
                for line in brief[case].splitlines():
                    print(f"║ {line.title():<58} ║")

                print("╠" + "═" * width + "╣")

                print(f"║ {'• Objective:':<58} ║")
                for line in cases[case]['objective'].splitlines():
                    print(f"║ {line.title():<58} ║")

                print("╚" + "═" * width + "╝")
                
                
            except Exception as e:
                print(f"ERROR: {e}")

    @staticmethod
    def get_investigation(detective, case, difficulty,
                        evidence, suspects, hints, progress):
        return {
            "Detective": "",
            "Case": "",
            "Difficulty": "",
            "Evidence": "",
            "Suspects": "",
            "Hints": "",
            "Progress": "",
        }
    
            
# PlayerGround().select_case()


def main():
    pass 

def re_play():
    pass 


def profile(name=None, rank=None, case_won=None,
            case_lost=None, xp=None, rating=None):
    
    # load data
    name = player_details.load_details()
    width = 50

    print("╔" + "═" * width + "╗")
    print(f"║{'DETECTIVE PROFILE'.center(width)}║")
    print("╠" + "═" * width + "╣")

    print(f"║ Name       : {name:<34}║")
    print(f"║ Rank       : {rank:<34}║")
    print(f"║ Cases Won  : {case_won:<34}║")
    print(f"║ Cases Lost : {case_lost:<34}║")
    print(f"║ XP         : {xp:<34}║")
    print(f"║ Rating     : {rating:<34}║")

    print(f"║{'':<50}║")
    print("╚" + "═" * width + "╝")
