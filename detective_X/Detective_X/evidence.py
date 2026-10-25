import json
from pathlib import Path
import detective_system, ui

# ---------- Config -----------
base = Path(__file__).parent
FILE = base / "player_record.json"
FILE_INV = base / "investigation.json"
EVIDENCE = base / "evidence_data.json"

SYSTEM = detective_system.DetectiveSystem()
class ExamineEvidence:
    EVIDENCE_DATA = SYSTEM.load_records(EVIDENCE)
    
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
                    evidence_info = ExamineEvidence.EVIDENCE_DATA.get(evidence)

                    # whether info exist
                    if not evidence_info:
                        print(f"[!] Dossier notes missing for: '{evidence}'")
                        continue

                    width = 85
                    print("╔" + "═" * width + "╗")
                    print(f"║{'EVIDENCE DOSSIER'.center(width)}║")
                    print("╠" + "═" * width + "╣")
                    print(f"║{'':<{width}}║")
                    
                    print(f"║ Evidence: {evidence:<{width-12}} ║")
                    print(f"║ Found At: {evidence_info['location']:<{width-12}} ║")
                    print(f"║ Category: {evidence_info['category']:<{width-12}} ║")
                    print(f"║ Details : {evidence_info['details']:<{width-12}} ║")
                    
                    print("║" + " " * width + "║")
                    print("╚" + "═" * width + "╝")

                else:
                    print("[!] Invalid option.")
                    continue
                
            except ValueError as e:
                print(f"Error: {e}")
                continue
