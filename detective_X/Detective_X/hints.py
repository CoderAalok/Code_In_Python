import json
from pathlib import Path
import textwrap
import locations, ui, detective_system

# ---------- Config -----------
base = Path(__file__).parent
FILE = base / "player_record.json"
FILE_INV = base / "investigation.json"

SYSTEM = detective_system.DetectiveSystem()

class HintSystem:
    """Hint stage: 1, 2, 3 for each case, and each hint -50 pts deducts"""
    CASE_HINTS = {
        # ═══════════════════ CASE 1: THE MISSING DIAMOND ═══════════════════
        "case_001": [
            {
                "hint_id": "hint_1",
                "title": "SECURITY & PERIMETER RECONNAISSANCE",
                "description": "The thief did not remain in the Grand Ballroom. Focus your search on the Security Office access logs and investigate the ground around the Conservatory Garden."
            },
            {
                "hint_id": "hint_2",
                "title": "FORCED ENTRY & ESCAPE TRAIL",
                "description": "Inspect the East Emergency Exit push-bar and compare its scratch marks to the lock on the diamond display case. Also note the vacant keycard slot #7."
            },
            {
                "hint_id": "hint_3",
                "title": "GUARD UNIFORM DISCREPANCY",
                "description": "Arthur Vance claims he never left the security desk, but CCTV at 11:47 PM captures a fleeing figure in a torn uniform. The fabric on the desk proves he wasn't at his post!"
            }
        ],

        # ═══════════════════ CASE 2: THE MIDNIGHT SERVER BREACH ═══════════════════
        "case_002": [
            {
                "hint_id": "hint_1",
                "title": "PHYSICAL INTRUSION & LOGS",
                "description": "This breach wasn't purely remote. Check the physical hardware inside Server Room B and examine the terminal logs inside the Security Operations Center."
            },
            {
                "hint_id": "hint_2",
                "title": "NETWORK TAP & CREDENTIALS",
                "description": "Look for rogue devices attached to Rack C and correlate them with Port 8080 traffic. Check around Console Terminal A for compromised administrative credentials."
            },
            {
                "hint_id": "hint_3",
                "title": "ROOT SESSION CONTRADICTION",
                "description": "Kevin Miller claims he logged off at 10 PM and was asleep, but unauthorized console commands were executed under root_admin during the midnight power surge!"
            }
        ],

        # ═══════════════════ CASE 3: THE POISONED PROFESSOR ═══════════════════
        "case_003": [
            {
                "hint_id": "hint_1",
                "title": "DEPARTMENT INVENTORY & REAGENT TRACE",
                "description": "The toxic agent came from within the department. Thoroughly examine the chemical storage vault in Chemistry Lab 304 and inspect the Professor's study."
            },
            {
                "hint_id": "hint_2",
                "title": "DELIVERY VECTOR & DISPOSAL",
                "description": "Analyze the Earl Grey tea cup and the communal sugar dispenser in the Faculty Lounge. Check the hazardous waste disposal logs for recent cyanide checkouts."
            },
            {
                "hint_id": "hint_3",
                "title": "FALSIFIED LOGS & CONTAMINATION",
                "description": "Julian Drake claims he never handled cyanide reagents, but the chemical checkout log signature was forged, and vinyl gloves in the trash smell distinctly of bitter almonds!"
            }
        ]
    }

    @classmethod
    def request_hint(cls, player_id: str, case_id: str):
        """Interactive hint console. Player can choose any hint; confirming deducts 50 points."""
        inv_data = SYSTEM.load_records(FILE_INV)
        record = SYSTEM._get_record(inv_data, player_id, case_id)

        player_data = SYSTEM.load_records(FILE)
        detective = player_data.get(player_id)
        
        if not record:
            print("[!] Investigation record not found!")
            return

        if not detective:
            print("[!] Player record not found.")
            return 
    
        hints_record = record.setdefault("Hints", {})
        used_hints = hints_record.setdefault("Used", [])
        available_hints = hints_record.setdefault("Available", ["hint_1", "hint_2", "hint_3"]) # By default available hints: 3

        case_hints = cls.CASE_HINTS.get(case_id, [])
        if not case_hints:
            print(f"[!] No forensic hints available for {case_id}.")
            return

        width = 60
        while True:
            # Display: Available hints
            ui.HintUI.hint_ui(len(available_hints))
            
            # Refresh current score and used count
            current_score = record.get("Scores", 0)

            print("\n" + "╔" + "═" * width + "╗")
            print(f"║{'HINT SYSTEM'.center(width)}║")
            print("╠" + "═" * width + "╣")
            print(f"║{'':<{width}}║")

            for idx, h in enumerate(case_hints, 1):
                title = h["title"]
                menu_label = f"[{idx}] {title[:40]}"
                print(f"║  {menu_label:<{width-2}}║")

            return_line = "[0] Return to Dashboard"
            print(f"║  {return_line:<{width - 4}}  ║")
            print(f"║{'':<{width}}║")
            print("╚" + "═" * width + "╝")

            try:
                choice = input(f"\nSelect hint option [0-{len(case_hints)}]: ").strip()
                if choice == "0":
                    break

                valid_options = [str(i) for i in range(1, len(case_hints) + 1)]
                if choice not in valid_options:
                    print(f"[!] Invalid option. Please select 0 to {len(case_hints)}.")
                    continue

                selected_idx = int(choice) - 1
                hint_data = case_hints[selected_idx]

                # Confirmation prompt before deduction
                print(f"\n[?] Request Hint: '{hint_data['title']}'?")
                print(f"    This will deduct 50 score points from your current score ({current_score} pts).")
                

                # ---------  PENALTY ---------
                PENALTY_SCORES = 50
                PENALTY_XP = PENALTY_SCORES // 2
                
                confirm = input("\nProceed? (y/n): ").strip().lower()
                
                if confirm in ["y", "yes"]:
                    if hint_data["hint_id"] not in used_hints:
                        # Hints update
                        used_hints.append(hint_data["hint_id"])
                        available_hints.remove(hint_data["hint_id"])
                        
                        # Deduct score
                        record["Scores"] = max(0, record.get("Scores", 0) - PENALTY_SCORES)
                        detective["XP"] = max(0, detective.get("XP", 0) - PENALTY_XP)
                        detective["Rank"] = SYSTEM.get_rank(detective.get("XP", 0))
                       
                        # Save to both investigation.json and player_record.json
                        SYSTEM.save_record(inv_data, FILE_INV)
                        SYSTEM.save_record(player_data, FILE)

                        # Display hint dossier card
                        cls._display_hint_card(hint_data, new_score=record["Scores"])
                        
                    else:
                        print("[!] Hint already used.")
                    
                else:
                    print("\n[!] Hint request cancelled. No points deducted.")
                input("\nPress Enter to Continue...")

            except Exception as e:
                print(f"[!] Error: {e}")

    @staticmethod
    def _display_hint_card(hint_data: dict, new_score: int):
        """Renders an attractive, aligned dossier card with the forensic hint."""
        width = 60
        hint_id = hint_data["hint_id"]
        title = hint_data["title"]
        desc = hint_data["description"]

        header = "HINT DOSSIER"
        wrapped_hint = textwrap.wrap(desc, width=width - 6)

        print("\n" + "╔" + "═" * width + "╗")
        print(f"║{header.center(width)}║")
        print("╠" + "═" * width + "╣")
        print(f"║{'':<{width}}║")
        
        id_line = f"Hint ID : {hint_id}"
        topic_line = f"Topic   : {title}"
        
        print(f"║  {id_line:<{width - 4}}  ║")
        print(f"║  {topic_line:<{width - 4}}  ║")
        print("╠" + "═" * width + "╣")
        print(f"║{'':<{width}}║")

        for line in wrapped_hint:
            print(f"║    {line:<{width - 6}}  ║")

        print(f"║{'':<{width}}║")
        cost_info = "• -50 Score deducted"
        score_info = f"• New Score: {new_score} pts"
        print(f"║  {cost_info:<{width - 4}}  ║")
        print(f"║  {score_info:<{width - 4}}  ║")
        print(f"║{'':<{width}}║")

        print("╚" + "═" * width + "╝")


if __name__ == "__main__":
    HintSystem.request_hint("P0001", "case_001")
