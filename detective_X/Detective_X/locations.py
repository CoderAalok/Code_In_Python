import ui
import json
from pathlib import Path

base = Path(__file__).parent
FILE_INV = base / "investigation.json"


# ──────────── Helpers ──────────────────────
class Helper:
    # Load investigation record
    @staticmethod
    def _load_inv():
        try:
            with open(FILE_INV) as f:
                return json.load(f)
            
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    # Save update record
    @staticmethod
    def _save_inv(data):
        with open(FILE_INV, 'w') as f:
            json.dump(data, f, indent=4)

    # fetch player active case record
    @staticmethod
    def _get_record(inv_data, player_id, case_id):
        return next(
            (r for r in inv_data.get(player_id, []) if r["Case"] == case_id),
            None
        )


# ────── MAIN CLASS OF CASE_1  ───────
class VisitLocationCase1:
    # ────── MAIN METHOD ────────
    @staticmethod
    def visit_location_case1(player_id, case_id):
        # fetch Location UI 
        location_ui = ui.LocationCase1()


        # call -> selected location
        locations = {
            1: VisitLocationCase1._exhibition_room,
            2: VisitLocationCase1._security_room,
            3: VisitLocationCase1._dining_hall,
        }

        #  ────── LOOP ──────
        while True:
            # display available locations
            location_ui.visit_location_ui()
            
            try:
                location = int(input("Select location [0-3]: ").strip())
                if locations.get(location):
                    locations[location](location_ui, player_id, case_id)
                    
                elif location == 0:
                    return
                
                else:
                    print("[!] Invalid option.")
                    continue 
                
            except Exception as e:
                print(f"Error: {e}")
                continue



    # ──────── LOCATION: EXHIBITION ROOM ───────
    @staticmethod
    def _exhibition_room(loc, player_id, case_id):
        CLUES = {
            'case':  ("Scratch marks on the diamond case lock",               # ----------------> Evidence
                    "🔍 Fresh scratch marks around the lock forced open from inside!"),  # -----> Message
            
            'floor': ("Muddy footprint near the case",                        # ---------------------> Evidence
                    "🔍 A single muddy footprint faces the emergency exit size 10."),  # -----> Message
            
            'panel': ("Tampered alarm wire in access panel",                  # -----------------> Evidence
                    "🔍 The alarm wire has been cleanly cut someone knew exactly where it was."),     # -----> Message

            'exit':  ("Scratched emergency exit push-bar",                    # -----------------> Evidence
                    "🔍 Scratches on the emergency push-bar confirm the thief escaped through this door!"),  # -----> Message
        }

        
        spot_map = {
            1: 'case',
            2: 'floor', 
            3: 'panel',
            0: 'exit',
        }

        #  ────── LOOP ──────
        while True:
            # display available exhibition room UI
            loc.exhibition_room_ui()
            
            try:
                spot = int(input("Search [0-3]: ").strip())
                if spot == 0:
                    return
                
                key = spot_map.get(spot)
                if not key:
                    print("[!] Invalid option.")
                    continue
                
                VisitLocationCase1._search_spot(loc, player_id, case_id, key, CLUES[key])
                
            except Exception as e:
                print(f"Error: {e}")
                continue


    # ──────── LOCATION: SECURITY ROOM ───────
    @staticmethod
    def _security_room(loc, player_id, case_id):
        CLUES = {
            'cctv': ("CCTV footage: figure at 11:47 PM", # ------> Evidence
                    "🎥 Footage shows a hooded figure near the diamond case at exactly 11:47 PM."),     #-----> Message
                    
            'log':  ("Access log: Keycard #7 used at 11:45 PM",# ------> Evidence
                    "📋 The log shows Keycard #7 was swiped at 11:45 PM 2 mins before the theft."),     #-----> Message
                        
            'desk': ("Torn uniform cloth on guard desk",  # ------> Evidence
                    "🧵 A torn piece of dark blue uniform cloth is tucked under the desk."),    #-----> Message
                    
            'rack': ("Missing keycard slot #7",   # ------> Evidence
                    "🔑 Keycard slot #7 is empty belongs to staff on night duty."),     #-----> Message
        }
        
        spot_map = {
            1: 'cctv', 
            2: 'log', 
            3: 'desk', 
            4: 'rack',
        }

        #  ────── LOOP ──────
        while True:
            # display available security room UI
            loc.security_room_ui()
            
            try:
                spot = int(input("Search [0-4]: ").strip())
                if spot == 0:
                    return
                
                key = spot_map.get(spot)
                if not key:
                    print("[!] Invalid option.")
                    continue
                
                VisitLocationCase1._search_spot(loc, player_id, case_id, key, CLUES[key])
                
            except Exception as e:
                print(f"Error: {e}")
                continue
            

    # ──────── LOCATION: DINING HALL ────────
    @staticmethod
    def _dining_hall(loc, player_id, case_id):
        CLUES = {
            'table':   ("Wine glass with lipstick at seat 4",  # ------> Evidence
                        "🍷 A wine glass with red lipstick sits untouched at seat 4 — possible DNA."),  #-----> Message
                        
            'kitchen': ("Staff roster: 3 names on night duty",  # ------> Evidence
                        "📋 Roster shows only 3 staff on duty: Elena, Marcus, and Chef Doyle."),    #-----> Message
                        
            'trash':   ("Crumpled note: '11:30 PM — east exit'",        # ------> Evidence
                        "📝 A crumpled note reads: '11:30 PM — east exit'. The theft was planned!"),    #-----> Message
                        
            'window':  ("Muddy shoe marks on window ledge",     # ------> Evidence
                        "👟 Same mud pattern as the Exhibition Room footprint — same suspect!"),   #-----> Message
        }
        
        spot_map = {
            1: 'table', 
            2: 'kitchen', 
            3: 'trash', 
            4: 'window'
        }

        #  ────── LOOP ──────
        while True:
            # display available dining room UI
            loc.dining_room_ui()
            
            try:
                spot = int(input("Search [0-4]: ").strip())
                if spot == 0:
                    return
                
                key = spot_map.get(spot)
                if not key:
                    print("[!] Invalid option.")
                    continue
                
                VisitLocationCase1._search_spot(loc, player_id, case_id, key, CLUES[key])
                
            except Exception as e:
                print(f"Error: {e}")
                continue


    # ────────── SHARED SEARCH HELPER ──────────
    @staticmethod
    def _search_spot(loc, player_id, case_id, status_key, clue, total_evidence=12):
        evidence_label, reveal_msg = clue

        # Whether already searched
        if loc.status[status_key] == 'Searched':
            print(f"[Already Searched]  {evidence_label}")
            return

        # reveal the clue
        print(reveal_msg)

        # mark spot as searched on UI object
        loc.status[status_key] = 'Searched'

        # save evidence into investigation.json file
        inv = Helper()._load_inv()
        record = Helper()._get_record(inv, player_id, case_id)
        
        if record and evidence_label not in record["Evidence"]:
            record["Evidence"].append(evidence_label)
            
            # each of 12 total spots = ~8% progress
            record["Progress"] = min(100, int((len(record['Evidence']) / total_evidence) * 100))
            Helper()._save_inv(inv)
            
            print(f"[✓] Evidence saved: '{evidence_label}'")

        return



# ──────────────── MAIN CLASS OF CASE_2 ────────────────
class VisitLocationCase2:
    #  ──────── MAIN METHOD ───────
    @staticmethod
    def visit_location_case2(player_id: str, case_id: str):
        # call -> location case2 UI
        location_ui = ui.LocationCase2()

        locations = {
            1: VisitLocationCase2._server_room,
            2: VisitLocationCase2._network_operation,
            3: VisitLocationCase2._cso_office,
        }

        # ------- LOOP ---------
        while True:
            # DISPLAY UI
            location_ui.visit_location_ui()

            try: 
                location = int(input("Select visit location [0-3]: ").strip())
                if location == 0:
                    return
                
                if location not in locations:
                    print("[!] Invalid option.")
                    continue

                locations[location](location_ui, player_id, case_id)

            except ValueError as e:
                print(f"Error: {e}")
                continue

                    
    #  ──────── LOCATION: SERVER ROOM VAULT ───────
    @staticmethod
    def _server_room(location_ui, player_id, case_id):
        CLUES = {
            'rack':     ("Rogue Raspberry Pi plugged into Rack C",
                         "🔌 A hardware implant is plugged into the rear diagnostic port of Server Rack C!"),
                         
            'vent':     ("Dropped contractor visitor badge",
                         "🪪 A visitor badge labeled 'Apex Cooling Maintenance' is caught in the floor vent."),
                         
            'terminal': ("Console session open under 'root_admin'",
                         "💻 The active terminal shows 'data_dump.sh' executed at 11:58 PM."),
                         
            'power':    ("UPS surge bypass record",
                         "⚡ Battery logs show a deliberate 3-second power fluctuation used to blind alarms."),
        }
        
        # map the specific object by integer
        spot_map = {
            1: 'rack',
            2: 'vent',
            3: 'terminal',
            4: 'power'
        }

        while True:
            # display UI
            location_ui.server_room_vault()

            try:
                search_index = int(input("Search [0-4]: ").strip())
                if search_index == 0:
                    return  # ---> exit

                # verify 
                key = spot_map.get(search_index)
                if not key:
                    print("[!] Invalid option.")
                    continue

                # update and save
                VisitLocationCase2._search_evidence(location_ui, player_id, case_id, key, CLUES[key])
                
            except ValueError as e:
                print(f"Error: {e}")
                continue

    #  ──────── LOCATION: NETWORK OPERATION CENTER ───────
    @staticmethod
    def _network_operation(location_ui, player_id, case_id):
        CLUES = {
            'monitor':  ("Foreign IP address traffic destination",
                         "🌐 Traffic traces show 42.8 GB uploaded to a hidden proxy server in Luxembourg."),
                         
            'operator': ("Sticky note with override password",
                         "📝 Taped beneath the keyboard is a handwritten note: 'Night Override: Hydra99'."),
                         
            'firewall': ("Internal Port 8080 rule alteration",
                         "🖨️ The firewall printer shows an unauthorized rule change timestamped at 11:50 PM."),
                         
            'trash':    ("Fast food receipt at 11:40 PM",
                         "🧾 A diner receipt shows the night operator was away during the breach window."),
                         
        }

        # map the specific object by integer
        spot_map = {
            1: 'monitor',
            2: 'operator',
            3: 'firewall',
            4: 'trash',
        }
        
        while True:
            # display UI
            location_ui.network_operations_center()
            
            try:
                search_index = int(input("Search [0-4]: ").strip())
                if search_index == 0:
                    return  # ---> exit

                # verify 
                key = spot_map.get(search_index)
                if not key:
                    print("[!] Invalid option.")
                    continue

                # update and save
                VisitLocationCase2._search_evidence(location_ui, player_id, case_id, key, CLUES[key])
                
            except ValueError as e:
                print(f"Error: {e}")
                continue
                

    #  ──────── LOCATION: CSO EXECUTIVE OFFICE ───────
    @staticmethod
    def _cso_office(location_ui, player_id, case_id):
        CLUES = {
            'desk':     ("Undated signed resignation letter",
                         "📄 A draft resignation letter sits tucked under the desk blotter."),
                         
            'safe':     ("Empty encrypted drive compartment",
                         "🔐 The velvet-lined compartment for 'Master Backup Vault #3' is completely empty."),
                         
            'shredder': ("Reconstructed offshore wire slip",
                         "📑 Pieced-together paper strips confirm an offshore wire acknowledgment."),
                         
            'balcony':  ("Unlocked fire escape latch",
                         "🚪 The heavy balcony door is unlocked, with fresh scuff marks on the fire ladder."),
                         
        }

        # map the specific object by integer
        spot_map = {
            1: 'desk', 
            2: 'safe', 
            3: 'shredder', 
            4: 'balcony'
        }
        
        while True:
            # display UI
            location_ui.cso_office()
            
            try:
                search_index = int(input("Search [0-4]: ").strip())
                if search_index == 0:
                    return  # ---> exit

                # verify 
                key = spot_map.get(search_index)
                if not key:
                    print("[!] Invalid option.")
                    continue

                # update and save
                VisitLocationCase2._search_evidence(location_ui, player_id, case_id, key, CLUES[key])
                
            except ValueError as e:
                print(f"Error: {e}")
                continue
    
    @staticmethod
    def _search_evidence(location_ui, player_id, case_id, key, clue, total_evidence=12):
        evidence, message = clue

        if location_ui.status[key] == 'SEARCHED':
            print(f"[Already searched]   {evidence}")
            return

        # show clue/message -> evidence
        print(message)

        # update status
        location_ui.status[key] = 'SEARCHED'

        # load investigation record
        inv_record = Helper()._load_inv()

        # fetch player record
        record = Helper()._get_record(inv_record, player_id, case_id)

        # prevent duplicate evidence
        if record and evidence not in record["Evidence"]:
            # add new evidence
            record['Evidence'].append(evidence)

            # case_id -> Medium level
            record["Progress"] = min(100, int((len(record['Evidence']) / total_evidence) * 100))

            # save updated record
            Helper()._save_inv(inv_record)

            print(f"[✓] Evidence saved: '{evidence}'")

        return


# ──────────── MAIN CLASS ────────────
class VisitLocationCase3:
    # ────── MAIN METHOD ────────
    @staticmethod
    def visit_location_case3(player_id: str, case_id: str):
        location_ui = ui.LocationCase3()

        locations = {
           1: VisitLocationCase3._chemistry_lab,
           2: VisitLocationCase3._professor_study,
           3: VisitLocationCase3._faculty_dining,
        }

        while True:
            # display UI of location of Case_3
            location_ui.visit_location_case3()

            try:
                # select location
                location = int(input("Select location [0-3]: ").strip())

                if location == 0:
                    return
                
                # verify
                if location not in locations:
                    print("[!] Invalid option.")
                    continue

                # call -> selected location
                locations[location](location_ui, player_id, case_id)
                
            except ValueError as e:
                print(f"Error: {e}")
                continue

    # ────── LOCATION: CHEMISTRY RESEARCH LAB ──────
    @staticmethod
    def _chemistry_lab(location_ui, player_id, case_id):
        CLUES = {
            'reagent': ("Missing 50ml Potassium Cyanide bottle",
                        "🧪 The inventory seal on bottle #42-Cyanide is broken; 50ml is unaccounted for."),
                        
            'hood':    ("Traces of bitter almond residue",
                        "💨 Fume hood airflow was turned off; white crystalline powder lines the glass sash."),
                        
            'logbook': ("Falsified checkout signature in log",
                        "📋 A checkout entry under 'Prof. Higgins' shows a forged signature."),
                        
            'sink':    ("Corrosive acid wash down the drain",
                        "🚰 The drain pipe shows fresh acid etching where toxic residue was washed."),
                        
        }
        
        spot_map = {
            1: 'reagent', 
            2: 'hood', 
            3: 'logbook', 
            4: 'sink'
        }
        
        while True:
            # display spot/specific area/object
            location_ui.chemistry_lab()

            try:
                spot_index = int(input('Search [0-4]: ').strip())
                if spot_index == 0:
                    return

                key = spot_map.get(spot_index)
                if not key:
                    print("[!] Invalid option.")
                    continue

                # search evidence
                VisitLocationCase3._search_evidence(location_ui, player_id,  case_id, key, CLUES[key])

            except ValueError as e:
                print(f"Error: {e}")
                continue
            
                
    # ────── LOCATION: PROFESSOR STUDY ──────
    @staticmethod
    def _professor_study(location_ui, player_id, case_id):
        CLUES = {
            'tea':    ("Lethal dose of cyanide in Earl Grey cup",
                       "☕ The cold tea tests positive for high-concentration cyanide in the honey."),
                       
            'letter': ("Hostile tenure dispute letter",
                       "✉️ A scathing letter signed by the Dean threatens immediate dismissal."),
                       
            'drawer': ("Patent dispute lawsuit draft",
                       "📁 Draft court papers show the professor was suing his lab assistant for patent theft."),
                       
            'basket': ("Torn calendar page marked 'Dinner 8 PM'",
                       "🗑️ A crumpled calendar leaf has a circled entry: '8 PM - Dinner with Dr. Voss'."),
                       
        }
        
        spot_map = {
            1: 'tea', 
            2: 'letter', 
            3: 'drawer', 
            4: 'basket'
        }
        
        while True:
            # display spot/specific area/object
            location_ui.professor_study()

            try:
                spot_index = int(input('Search [0-4]: ').strip())
                if spot_index == 0:
                    return

                key = spot_map.get(spot_index)
                if not key:
                    print("[!] Invalid option.")
                    continue

                # search evidence
                VisitLocationCase3._search_evidence(location_ui, player_id,  case_id, key, CLUES[key])

            except ValueError as e:
                print(f"Error: {e}")
                continue
            

    # ────── LOCATION: FACULTY DINING ──────
    @staticmethod
    def _faculty_dining(location_ui, player_id, case_id):
        CLUES = {
            'coffee': ("Sugar dispenser contaminated with powder",
                       "☕ Fine white crystals were mixed into the raw sugar shaker on the counter."),
            'fridge': ("Labeled milk carton with punctured cap",
                       "🥛 The victim's almond milk carton has a tiny syringe puncture in the foil cap."),
            'board':  ("Seminar schedule with altered speaker list",
                       "📌 The official faculty schedule shows someone was quietly substituted as speaker."),
            'gloves': ("Discarded vinyl gloves smelling of almonds",
                       "🧤 Disposable gloves found under the sink test positive for cyanide residue."),
        }
        
        spot_map = {1: 'coffee', 2: 'fridge', 3: 'board', 4: 'gloves'}
        
        while True:
            location_ui.faculty_lounge()
            try:
                spot = int(input("Search [0-4]: ").strip())
                if spot == 0:
                    return
                key = spot_map.get(spot)
                if not key:
                    print("[!] Invalid option.")
                    continue
                VisitLocationCase3._search_evidence(location_ui, player_id, case_id, key, CLUES[key])
            except Exception as e:
                print(f"Error: {e}")

    # ────────── SEARCH EVIDENCE ─────────
    @staticmethod
    def _search_evidence(location_ui, player_id, case_id, key, clue, total_evidence=12):
        evidence, message = clue

        # Check: whether already evidence SEARCHED
        if location_ui.status[key] == 'SEARCHED':
            print(f"[Already searched]  {evidence}")
            return
        
        print(message)
        location_ui.status[key] = 'SEARCHED'

        # load investigation record
        inv_record = Helper()._load_inv()

        # fetch active case record
        record = Helper()._get_record(inv_record, player_id, case_id)

        if record and evidence not in record['Evidence']:
            # add new evidence
            record['Evidence'].append(evidence)

            # progress update
            record["Progress"] = min(100, int((len(record['Evidence']) / total_evidence) * 100))

            Helper()._save_inv(inv_record)
            print(f"[✓] Evidence saved: '{evidence}'")

        return


# MAIN DRIVE CLASS
def main(player_id:str, case_id:str):
    cases = {
        "case_001": VisitLocationCase1.visit_location_case1,
        "case_002": VisitLocationCase2.visit_location_case2,
        "case_003": VisitLocationCase3.visit_location_case3,
    }

    if case_id in cases:
        # call -> CLASS
        cases[case_id](player_id, case_id)
     
    else:
        print("Case ID is not found!")
    
    return
