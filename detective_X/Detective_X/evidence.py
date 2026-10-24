import json
from pathlib import Path
import locations, ui

# ---------- Config -----------
base = Path(__file__).parent
FILE = base / "player_record.json"
FILE_INV = base / "investigation.json"

class ExamineEvidence:
    EVIDENCE_DATA = {
        # ═══════════════════ CASE 1: THE MISSING DIAMOND (12 Clues) ═══════════════════
        # Exhibition Room 
        "Scratch marks on the diamond case lock": {
            "location": "Exhibition Room",
            "category": "Physical",
            "details": "Fresh scratch marks around the lock, forced open from inside."
        },
        "Muddy footprint near the case": {
            "location": "Exhibition Room",
            "category": "Physical",
            "details": "A single muddy shoe print on marble facing the exit (Size 10)."
        },
        "Tampered alarm wire in access panel": {
            "location": "Exhibition Room",
            "category": "Physical",
            "details": "The alarm wire was cleanly cut; intruder knew its exact placement."
        },
        "Scratched emergency exit push-bar": {
            "location": "Exhibition Room",
            "category": "Physical",
            "details": "Fresh abrasions on the push-bar prove the thief fled through this door."
        },

        # Security Room 
        "CCTV footage figure at 11:47 PM": {
            "location": "Security Room",
            "category": "Digital",
            "details": "Footage shows a hooded figure near the display at exactly 11:47 PM."
        },
        "Access log Keycard #7 used at 11:45 PM": {
            "location": "Security Room",
            "category": "Digital",
            "details": "Badge log shows Keycard #7 swiped 2 minutes before the theft."
        },
        "Torn uniform cloth on guard desk": {
            "location": "Security Room",
            "category": "Physical",
            "details": "A torn strip of dark blue guard uniform cloth tucked under the desk."
        },
        "Missing keycard slot #7": {
            "location": "Security Room",
            "category": "Physical",
            "details": "Slot #7 on the keycard rack is empty; assigned to night patrol staff."
        },

        #  Dining Hall 
        "Wine glass with lipstick at seat 4": {
            "location": "Dining Hall",
            "category": "Chemical",
            "details": "Wine glass with distinctive red lipstick residue left at seat 4."
        },
        "Staff roster 3 names on night duty": {
            "location": "Dining Hall",
            "category": "Document",
            "details": "Roster records only 3 staff on night duty: Elena, Marcus, and Doyle."
        },
        "Crumpled note 11:30 PM east exit": {
            "location": "Dining Hall",
            "category": "Document",
            "details": "Handwritten note planning a meeting at the east exit before the theft."
        },
        "Muddy shoe marks on window ledge": {
            "location": "Dining Hall",
            "category": "Physical",
            "details": "Same mud and tread pattern as the footprint near the display case."
        },

        # ═══════════════════ CASE 2: MIDNIGHT CYBER BREACH (12 Clues) ═══════════════════
        # Server Room Vault
        "Rogue Raspberry Pi plugged into Rack C": {
            "location": "Server Room Vault",
            "category": "Digital",
            "details": "Unauthorized hardware implant active on diagnostic port of Rack C."
        },
        "Dropped contractor visitor badge": {
            "location": "Server Room Vault",
            "category": "Physical",
            "details": "Contractor badge for 'Apex Cooling' found caught inside floor vent."
        },
        "Console session open under 'root_admin'": {
            "location": "Server Room Vault",
            "category": "Digital",
            "details": "Active terminal showing data exfiltration script executed at 11:58 PM."
        },
        "UPS surge bypass record": {
            "location": "Server Room Vault",
            "category": "Digital",
            "details": "Battery logs reveal a deliberate 3-second power drop used to blind sensors."
        },

        # Network Operations Center
        "Foreign IP address traffic destination": {
            "location": "Network Operations Center",
            "category": "Digital",
            "details": "Traffic trace logs show 42.8 GB uploaded to a proxy server in Luxembourg."
        },
        "Sticky note with override password": {
            "location": "Network Operations Center",
            "category": "Document",
            "details": "Handwritten note taped under keyboard: 'Night Override: Hydra99'."
        },
        "Internal Port 8080 rule alteration": {
            "location": "Network Operations Center",
            "category": "Digital",
            "details": "Firewall logs show an unauthorized port rule opened at 11:50 PM."
        },
        "Fast food receipt at 11:40 PM": {
            "location": "Network Operations Center",
            "category": "Document",
            "details": "Diner receipt proving the night shift operator stepped away from the console."
        },

        # CSO Executive Office
        "Undated signed resignation letter": {
            "location": "CSO Office",
            "category": "Document",
            "details": "A draft resignation letter found hidden under the desk blotter."
        },
        "Empty encrypted drive compartment": {
            "location": "CSO Office",
            "category": "Physical",
            "details": "Velvet-lined compartment for 'Master Backup Vault #3' is completely empty."
        },
        "Reconstructed offshore wire slip": {
            "location": "CSO Office",
            "category": "Document",
            "details": "Reassembled paper strips confirm a large offshore wire transfer."
        },
        "Unlocked fire escape latch": {
            "location": "CSO Office",
            "category": "Physical",
            "details": "Fire balcony door unlatched with fresh scuff marks on the fire ladder."
        },

        # -------------  CASE 3: THE POISONED PROFESSOR (12 Clues) --------------
        #  Chemistry Research Lab 
        "Missing 50ml Potassium Cyanide bottle": {
            "location": "Chemistry Research Lab",
            "category": "Chemical",
            "details": "Inventory seal on bottle #42 broken; exactly 50ml cyanide is unaccounted for."
        },
        "Traces of bitter almond residue": {
            "location": "Chemistry Research Lab",
            "category": "Chemical",
            "details": "Fume hood airflow disabled; white crystalline powder lines the glass sash."
        },
        "Falsified checkout signature in log": {
            "location": "Chemistry Research Lab",
            "category": "Document",
            "details": "Chemical logbook entry under 'Prof. Higgins' shows a forged signature."
        },
        "Corrosive acid wash down the drain": {
            "location": "Chemistry Research Lab",
            "category": "Chemical",
            "details": "Drain pipe shows acid etching where chemical poison was hastily flushed."
        },

        # ── Professor Personal Study ──
        "Lethal dose of cyanide in Earl Grey cup": {
            "location": "Professor Study",
            "category": "Chemical",
            "details": "Cold tea cup tests positive for high-concentration cyanide in the honey."
        },
        "Hostile tenure dispute letter": {
            "location": "Professor Study",
            "category": "Document",
            "details": "Scathing official letter signed by the Dean threatening immediate termination."
        },
        "Patent dispute lawsuit draft": {
            "location": "Professor Study",
            "category": "Document",
            "details": "Draft court filing showing Bell was suing his assistant for intellectual theft."
        },
        "Torn calendar page marked 'Dinner 8 PM'": {
            "location": "Professor Study",
            "category": "Document",
            "details": "Torn calendar page with a circled note: '8 PM Dinner with Dr. Voss'."
        },

        # ── Faculty Dining Lounge ──
        "Sugar dispenser contaminated with powder": {
            "location": "Faculty Lounge",
            "category": "Chemical",
            "details": "Fine white poison crystals mixed directly into the communal sugar dispenser."
        },
        "Labeled milk carton with punctured cap": {
            "location": "Faculty Lounge",
            "category": "Chemical",
            "details": "Victim's personal almond milk has a tiny syringe needle puncture in the cap."
        },
        "Seminar schedule with altered speaker list": {
            "location": "Faculty Lounge",
            "category": "Document",
            "details": "Notice board schedule shows the keynote speaker was quietly replaced."
        },
        "Discarded vinyl gloves smelling of almonds": {
            "location": "Faculty Lounge",
            "category": "Physical",
            "details": "Disposable gloves found under the sink test positive for cyanide residue."
        }
    }

    
    @staticmethod
    def examine_evidence(player_id: str, case_id: str):
        
        while True:
            # collected evidence show
            collected_evidence = ui.EvidenceUI.evidence_ui(player_id, case_id)  # dictionay {index : evidence}
            if not collected_evidence:
                print("[!] No evidence collected yet.")
                return 

            try:
                evidence_index = int(input(f"Pick an evidence [0-{len(collected_evidence)}]: ").strip())
                if evidence_index == 0:
                    return
                
                if evidence_index in collected_evidence:
                    # get evidence
                    evidence = collected_evidence[evidence_index]
                    evidence_data = ExamineEvidence.EVIDENCE_DATA
                    info = evidence_data.get(evidence)

                    # whether info exist
                    if not info:
                        print("[!] Evidence not found.")
                        return 
                    
                    width = 85
                    print("╔" + "═" * width + "╗")
                    print(f"║{'EVIDENCE DOSSIER'.center(width)}║")
                    print("╠" + "═" * width + "╣")
                    print(f"║{'':<{width}}║")
                    
                    print(f"║ Evidence: {evidence:<{width-12}} ║")
                    print(f"║ Found At: {info['location']:<{width-12}} ║")
                    print(f"║ Category: {info['category']:<{width-12}} ║")
                    print(f"║ Details : {info['details']:<{width-12}} ║")
                    
                    print("║" + " " * width + "║")
                    print("╚" + "═" * width + "╝")

                else:
                    print("[!] Invalid option.")
                    continue
                
            except ValueError as e:
                print(f"Error: {e}")
                continue

# if __name__ == "__main__":
#     ExamineEvidence.examine_evidence("P0001", "case_001")
