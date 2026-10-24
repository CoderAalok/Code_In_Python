import json
from pathlib import Path
import textwrap
import detective_system

# ---------- Config -----------
base = Path(__file__).parent
FILE = base / "player_record.json"
FILE_INV = base / "investigation.json"

SYSTEM = detective_system.DetectiveSystem()
class CompareEvidence:
    """Forensic lab module to cross-reference and correlate two gathered clues."""

    EVIDENCE_PAIRS = {
        # ═══════════════════ CASE 1: THE MISSING DIAMOND ═══════════════════
        "case_001": [
            {
                "pair_id": "c1_pair_tool_marks",
                "clue1": "Scratch marks on the diamond case lock",
                "clue2": "Scratched emergency exit push-bar",
                "title": "LOCKPICK TOOL CORRELATION",
                "deduction": "Forensic scratch patterns match! The same lockpick tool was used to pick the diamond case lock and force the east emergency exit push-bar."
            },
            {
                "pair_id": "c1_pair_keycard_theft",
                "clue1": "Access log: Keycard #7 used at 11:45 PM",
                "clue2": "Missing keycard slot #7",
                "title": "SECURITY CORRIDOR BREACH",
                "deduction": "Keycard #7 was stolen from slot #7 prior to the gala, proving the thief premeditated their security room access in advance."
            },
            {
                "pair_id": "c1_pair_guard_imposter",
                "clue1": "CCTV footage: figure at 11:47 PM",
                "clue2": "Torn uniform cloth on guard desk",
                "title": "GUARD UNIFORM DISGUISE",
                "deduction": "Fabric fiber analysis confirms the torn cloth on the desk matches the security guard uniform worn by the fleeing figure on camera."
            },
            {
                "pair_id": "c1_pair_footwear_trail",
                "clue1": "Muddy footprint near the case",
                "clue2": "Muddy shoe marks on window ledge",
                "title": "ESCAPE TRAIL CORRELATION",
                "deduction": "Both size 10 prints share an identical diamond tread wear, proving the same individual stepped from the display case to the window ledge."
            }
        ],

        # ═══════════════════ CASE 2: THE MIDNIGHT SERVER BREACH ═══════════════════
         "case_002": [
            {
                "pair_id": "c2_pair_hardware_tap",
                "clue1": "Rogue Raspberry Pi plugged into Rack C",
                "clue2": "Internal Port 8080 rule alteration",
                "title": "HARDWARE BACKDOOR DETECTED",
                "deduction": "The rogue Raspberry Pi was mapped directly to the newly opened Port 8080 to sniff confidential internal project data packets."
            },
            {
                "pair_id": "c2_pair_root_theft",
                "clue1": "Console session open under 'root_admin'",
                "clue2": "Sticky note with override password",
                "title": "ADMIN CREDENTIAL THEFT",
                "deduction": "The root password scrawled on the sticky note matches the exact hash used to log into the unauthorized midnight console session."
            },
            {
                "pair_id": "c2_pair_exfiltration",
                "clue1": "Foreign IP address traffic destination",
                "clue2": "Reconstructed offshore wire slip",
                "title": "FINANCIAL MOTIVE CORRELATION",
                "deduction": "The overseas IP receiving the exfiltrated project data traces back to the beneficiary account on the reconstructed offshore wire slip."
            },
            {
                "pair_id": "c2_pair_blackout_escape",
                "clue1": "UPS surge bypass record",
                "clue2": "Unlocked fire escape latch",
                "title": "BLACKOUT COVER FOR ESCAPE",
                "deduction": "The momentary power surge gave the physical intruder a 60-second window of darkness to slip through the fire escape latch undetected."
            }
        ],

        # ═══════════════════ CASE 3: THE POISONED PROFESSOR ═══════════════════
         "case_003": [
            {
                "pair_id": "c3_pair_lethal_agent",
                "clue1": "Missing 50ml Potassium Cyanide bottle",
                "clue2": "Lethal dose of cyanide in Earl Grey cup",
                "title": "LETHAL REAGENT MATCH",
                "deduction": "Chemical concentration in the Earl Grey tea matches the exact purity grade of the Potassium Cyanide missing from the Lab 304 chemical vault."
            },
            {
                "pair_id": "c3_pair_sugar_delivery",
                "clue1": "Sugar dispenser contaminated with powder",
                "clue2": "Lethal dose of cyanide in Earl Grey cup",
                "title": "POISON DELIVERY VECTOR",
                "deduction": "The poison was not added directly to the tea cup, but stirred into the communal sugar dispenser used exclusively by Professor Sterling."
            },
            {
                "pair_id": "c3_pair_forgery_disposal",
                "clue1": "Falsified checkout signature in log",
                "clue2": "Discarded vinyl gloves smelling of almonds",
                "title": "TAMPERED DISPOSAL LINK",
                "deduction": "The person who forged the chemical checkout signature wore and discarded nitrile gloves bearing heavy traces of bitter almond cyanide residue."
            },
            {
                "pair_id": "c3_pair_motive_fusion",
                "clue1": "Hostile tenure dispute letter",
                "clue2": "Patent dispute lawsuit draft",
                "title": "COMPOUND RESEARCH MOTIVE",
                "deduction": "Rival academic disputes combined with multi-million patent royalty lawsuits establish a premeditated motive to silence the victim."
            }
        ]
    }

    @classmethod
    def compare_evidence(cls, player_id: str, case_id: str):
        # fetch data
        inv_data = SYSTEM.load_records(FILE_INV)
        record = SYSTEM._get_record(inv_data, player_id, case_id)  # dictionary
        player_data = SYSTEM.load_records(FILE)
        detective = player_data.get(player_id, {})

        if record is None:
            print("[!] Investigation record not found.")
            return

        if not detective:
            print("[!] Player record not found.")
            return
        
        collected_evidence = record.get("Evidence", [])

        # prevent single evidence comparison 
        if len(collected_evidence) < 2:
            print("\n[!] You need at least 2 clues in your evidence locker to compare.")
            input("Press Enter to return to Dashboard...")
            return

        # Display collected evidence
        width = 55
        print("╔" + "═" * (width + 2) + "╗")
        print(f"║{'COMPARED EVIDENCE'.center(width + 2)}║")
        print("╠" + "═" * (width + 2) + "╣")
        print(f"║{'':<{width + 2}}║")

        for i, evidence in enumerate(collected_evidence, 1):
            text = f"[{i}] {evidence}"
            print(f"║ {text:<{width}} ║")

        print(f"║ {"[0] Return back to Investigation action":<{width}} ║")
        print("║" + " " * (width + 2) + "║")
        print("╚" + "═" * (width + 2) + "╝")


        while True:
            try:
                # Evidence selection 
                evid1_index = int(input("Select first evidence [1-12]: ").strip())

                if evid1_index == 0:
                    return 
                
                evid2_index = int(input("Select second evidence [1-12]: ").strip())

                if evid2_index == 0:
                    return 
            
                if evid1_index == evid2_index:
                    print("[!] You cannot compare same evidence.")
                    return 

                
            
                # Text Normalization
                text_normalize = lambda s: " ".join(
                    s.lower().replace("-", " ").replace("—", " ").replace("'", " ").split()
                )
                
                # clues with normalize
                clue1 = text_normalize(collected_evidence[evid1_index - 1])
                clue2 = text_normalize(collected_evidence[evid2_index - 1])

                evidence_data = cls.EVIDENCE_PAIRS.get(case_id, [])  # list of dictionary

                matched_evidence = None
                for pair in evidence_data:
                    pair_clue1 = text_normalize(pair['clue1'])
                    pair_clue2 = text_normalize(pair['clue2'])

                    # Evidence comparison
                    if (pair_clue1 == clue1 and pair_clue2 == clue2) or (pair_clue1 == clue2 and pair_clue2 == clue1):
                        matched_evidence = pair
                        break 
                    
                if matched_evidence:
                    comparison = record.setdefault("Comparisons", [])

                    # whether comparison already has done
                    if matched_evidence.get("pair_id") in comparison:
                        print("\n[✓] You have already compared this evidence. Try another one.\n") 

                    else:
                        # add compared evidence
                        comparison.append(matched_evidence["pair_id"])

                        # give points and update rank
                        record['Scores'] += 40
                        detective['XP'] += 20
                        detective['Rank'] = SYSTEM.get_rank(detective['XP'])

                        # Save updated records
                        SYSTEM.save_record(inv_data, FILE_INV)
                        SYSTEM.save_record(player_data, FILE)
                        
                        # Display deduction
                        display_deduction(matched_evidence['title'], matched_evidence['deduction'])
                    
                else:
                    print("[!] Compared evidence doen not matched.")
                    
                input("\nPress Enter to Continue....")
                    
                
            except ValueError:
                print("[!] Invalid option.")

            except Exception as e:
                print(f"Error: {e}")
                

def display_deduction(title, deduction):

    width = 62
    wrap_text = textwrap.wrap(deduction, width=width-6)
    
    print("╔" + "═" * (width + 2) + "╗")
    print(f"║{title.center(width + 2)}║")
    print("╠" + "═" * (width + 2) + "╣")
    print(f"║{'':<{width + 2}}║")

    for text in wrap_text:
        print(f"║   {text:<{width-3}}  ║")

    print(f"║{'':<{width + 2}}║")
    print(f"║  {'• Score +40 pts awarded!':<{width-4}}    ║")
    print(f"║  {'• Detective XP +20 awarded!':<{width-2}}  ║")
    
    print(f"║{'':<{width + 2}}║")
    print("╚" + "═" * (width + 2) + "╝")

