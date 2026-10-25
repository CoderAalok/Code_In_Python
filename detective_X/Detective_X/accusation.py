from pathlib import Path
import json
from unittest import case 
import ui, detective_system, detective_x, suspects

# ------ Config -------
base = Path(__file__).parent
FILE = base / "player_record.json"
FILE_INV = base / "investigation.json"
FILE_DATA = base / "data" 

SYSTEM = detective_system.DetectiveSystem()

class FinalAccusation:
    """Final Accusation: Here the final determination did the detective find the real criminal"""
    
    # ═══════════════════ ALL 12 CASE CLUES ═══════════════════
    ALL_CASE_EVIDENCE = {
        "case_001": [
            "Scratch marks on the diamond case lock",
            "Muddy footprint near the case",
            "Tampered alarm wire in access panel",
            "Scratched emergency exit push-bar",
            "CCTV footage: figure at 11:47 PM",
            "Access log: Keycard #7 used at 11:45 PM",
            "Torn uniform cloth on guard desk",
            "Missing keycard slot #7",
            "Wine glass with lipstick at seat 4",
            "Staff roster: 3 names on night duty",
            "Crumpled note: '11:30 PM — east exit'",
            "Muddy shoe marks on window ledge"
        ],
        "case_002": [
            "Rogue Raspberry Pi plugged into Rack C",
            "Internal Port 8080 rule alteration",
            "Overhead fiber cable tapped",
            "Console session open under 'root_admin'",
            "Sticky note with override password",
            "Foreign IP address traffic destination",
            "Reconstructed offshore wire slip",
            "Night shift security log gap",
            "Empty server room master key hook",
            "Shredded network topology blueprint",
            "UPS surge bypass record",
            "Unlocked fire escape latch"
        ],
        "case_003": [
            "Missing 50ml Potassium Cyanide bottle",
            "Lethal dose of cyanide in Earl Grey cup",
            "Sugar dispenser contaminated with powder",
            "Falsified checkout signature in log",
            "Discarded vinyl gloves smelling of almonds",
            "Discarded coffee pod in sink trash",
            "Annotated thesis manuscript draft",
            "Denial letter for Julian's fellowship",
            "Locked drawer forced with scalpel",
            "Department roster with Julian on duty",
            "Draft of faculty misconduct complaint",
            "Almond-scented chemical residue in trap"
        ]
    }

    CASE_SOLUTIONS = {
        # ═══════════════════ CASE 1: THE MISSING DIAMOND ═══════════════════
        "case_001": {
            "culprit": "Arthur Vance",
            "key_evidence": [
                "Torn uniform cloth on guard desk",
                "CCTV footage: figure at 11:47 PM",
                "Scratched emergency exit push-bar",
                "Access log: Keycard #7 used at 11:45 PM"
            ],
            "min_evidence": 2,
            "crime_story": (
                "Deep in debt, Arthur used stolen Keycard #7 to pick the diamond lock "
                "and fled, snagging his uniform as he ran."
            ),
            "clues_connection": (
                "Tool marks match the exit push-bar, and torn desk fabric matches Arthur's uniform."
            ),
            "missed_reasons": [
                "Arthur's false alibi",
                "Torn uniform cloth on desk",
                "Emergency exit scratch marks"
            ]
        },

        # ═══════════════════ CASE 2: THE MIDNIGHT SERVER BREACH ═══════════════════
        "case_002": {
            "culprit": "Kevin Miller",
            "key_evidence": [
                "Rogue Raspberry Pi plugged into Rack C",
                "Console session open under 'root_admin'",
                "Sticky note with override password",
                "Foreign IP address traffic destination"
            ],
            "min_evidence": 2,
            "crime_story": (
                "Bribed by a rival, Kevin plugged a rogue Pi into Rack C to leak "
                "project files during the midnight surge."
            ),
            "clues_connection": (
                "The rogue Pi ran on Port 8080 using root credentials found on the desk."
            ),
            "missed_reasons": [
                "Midnight root session",
                "Rogue Raspberry Pi on Port 8080",
                "Foreign IP linked to offshore wire"
            ]
        },

        # ═══════════════════ CASE 3: THE POISONED PROFESSOR ═══════════════════
        "case_003": {
            "culprit": "Julian Drake",
            "key_evidence": [
                "Sugar dispenser contaminated with powder",
                "Missing 50ml Potassium Cyanide bottle",
                "Discarded vinyl gloves smelling of almonds",
                "Falsified checkout signature in log"
            ],
            "min_evidence": 2,
            "crime_story": (
                "Fearing exposure for plagiarism, Julian stole cyanide from Vault 304 "
                "and poisoned the faculty sugar dispenser."
            ),
            "clues_connection": (
                "Cyanide purity matched Vault 304, and forged checkout logs tied to Julian."
            ),
            "missed_reasons": [
                "Forged cyanide checkout log",
                "Cyanide in communal sugar dispenser",
                "Almond-scented gloves in trash"
            ]
        }
    }

    
    @classmethod
    def final_accusation(cls, player_id: str, case_id: str):
        # load data/record
        inv_record = SYSTEM.load_records(FILE_INV)
        player_inv = SYSTEM._get_record(inv_record, player_id, case_id)
        detective_record = SYSTEM.load_records(FILE)
        player_record = SYSTEM._player_record(detective_record, player_id)

        # -------- check validation record --------
        if player_inv is None:
            print("[!] Investigation not found.")
            return False

        if not player_record:
            print("[!] Player record not found.")
            return False

        # -------- fetch suspects --------
        suspect = [sup for sup in player_inv.get('Suspects', [])]
        if not suspect:
            import suspects as sus_module
            case_suspects = sus_module.Dispatch.suspects_map.get(case_id, {})
            suspect = [s["name"] for s in case_suspects.values()]

        records = {}
        
        while True:
            # ---------------- display final accusation box ----------------
            ui.AccusationUI.accusation_ui(suspect)

            try:
                select_suspect = int(input(f"Select Suspect [0-{len(suspect)}]: ").strip())
                if select_suspect == 0:
                    return False
                
                case_solution = cls.CASE_SOLUTIONS.get(case_id)
                if not case_solution:
                    print("[!] Case ID not match.")
                    return False

                # -------- data fetch from CASE Solution --------
                accused = suspect[select_suspect - 1]
                culprit = case_solution.get('culprit', "")
                missed_evidence = case_solution.get('missed_reasons', [])
                key_evidence = case_solution.get('key_evidence', [])
                min_evidence = case_solution.get('min_evidence', 2)

                # data fetch from Investigation.json and player record.json
                xp = player_record.get("XP", 0)
                scores = player_inv.get("Scores", 0)
                contradictions = player_inv.get('Contradictions', [])
                hint = player_inv.get('Hints', {})

                # -------- Penalty ------------
                PENALTY_SCORE = 300
                PENALTY_XP = PENALTY_SCORE // 2
                
                # check selected culprit match
                if accused != case_solution['culprit']:
                    ui.AccusationUI.wrong_accusation(accused, culprit, missed_evidence)

                    player_inv["Scores"] = max(0, scores - PENALTY_SCORE)
                    player_record["XP"] = max(0, xp - PENALTY_XP)
                    player_record["Rank"] = SYSTEM.get_rank(player_record["XP"])
                    player_record["Cases_Lost"] = player_record.get("Cases_Lost", 0) + 1
                    player_record["Active_Case"] = None
                    
                    # save updated records
                    SYSTEM.save_record(inv_record, FILE_INV)
                    SYSTEM.save_record(detective_record, FILE)
                    input("\nPress Enter to return to Main Menu...")
                    return True


                # --------------- ACTUAL CULPRIT ---------------
                # Player's collected evidence from investigation
                player_collected = player_inv.get("Evidence", [])
                
                if not player_collected:
                    print("[!] You have not gathered any evidence yet.")
                    return False

                # ------------ All possible clues for the active case ----------
                all_case_evidence = cls.ALL_CASE_EVIDENCE.get(case_id, [])

                # --------------- DISPLAY ALL POSSIBLE CASE CLUES ------------
                width = 54
                print("\n" + "╔" + "═" * width + "╗")
                print(f"║{f'CASE EVIDENCE DOSSIER'.center(width)}║")
                print("╠" + "═" * width + "╣")
                print(f"║{'':<{width}}║")
        
                for i, evid in enumerate(all_case_evidence, 1):
                    print(f"║  [{i:>2}] {evid:<{width-9}}  ║")

                print(f"║{'':<{width}}║")
                print("╚" + "═" * width + "╝")

                print(f"\n✓ You have gathered {len(player_collected)}/{len(all_case_evidence)} total case clues.")
                evid_num = input(f"Select your gathered evidence numbers (e.g. 1, 2, 3): ").strip()
                selected_indices = [int(x.strip()) - 1 for x in evid_num.split(",") if x.strip().isdigit()]
                player_selected = [all_case_evidence[i] for i in selected_indices if 0 <= i < len(all_case_evidence)]

                if not player_selected:
                    print("[!] No valid evidence selected.")
                    input("\nPress Enter to continue...")
                    continue

                # Normalization function for clean, reliable clue matching
                clean_text = lambda s: " ".join(
                    s.lower().replace("—", " ").replace("-", " ").replace("'", "").split()
                )

                # Verify player_selected against player_collected
                collected_clean = [clean_text(c) for c in player_collected]
                verified_evidence = [evid for evid in player_selected if clean_text(evid) in collected_clean]


                # Match verified evidence against key incriminating clues
                key_clues_clean = {clean_text(k) for k in key_evidence}
                matched_evidence = [evid for evid in verified_evidence if clean_text(evid) in key_clues_clean]

                # Check if matched key evidence satisfies minimum requirement
                if len(matched_evidence) < min_evidence:
                    print(f"\n[!] INSUFFICIENT DECISIVE PROOF! ({len(matched_evidence)}/{min_evidence} key clues matched)")
                    print("    The evidence presented does not conclusively incriminate the suspect.")
                    print(f"    You must present at least {min_evidence} decisive clues to secure a conviction.")
                    input("\nPress Enter to return to the Investigation Dashboard...")
                    return False


                # ------------- Evidence confirmation ----------------
                ui.AccusationUI.confirm_accusation(verified_evidence, culprit)
                    
                confirm = input("Confirm accusation and close case? [Y/N]: ").strip().lower()

                if confirm not in ["y", "yes"]:
                    print("\n[!] Accusation cancelled.")
                    return False

                # Mark case completed in player record
                completed = player_record.setdefault('Completed_Cases', [])
                if case_id in completed:
                    print(f"[!] {case_id} already solved.")
                    return False

                # solved case
                completed.append(case_id)
                
                pending = player_record.get('Pending_Cases', [])
                if case_id in pending:
                    pending.remove(case_id)

                player_record['Active_Case'] = None

                # --------  AWARD BONUSES -------------
                AWARD_SCORE = 500
                AWARD_XP = AWARD_SCORE // 2

                player_inv["Scores"] += AWARD_SCORE
                player_record["XP"] += AWARD_XP
                player_record["Rank"] = SYSTEM.get_rank(player_record["XP"])
                player_record["Cases_Won"] = player_record.get("Cases_Won", 0) + 1

                score = player_inv.get("Scores", 0)
                earned_rating = detective_system.DetectiveSystem.get_rating(score)
                player_record["Rating"] = earned_rating

                # save updated records
                SYSTEM.save_record(inv_record, FILE_INV)
                SYSTEM.save_record(detective_record, FILE)

                # Display: case solved dashboard
                records.update(
                    {
                        'culprit': culprit,
                        "scores": score,
                        "evidence": player_collected,
                        "contradictions": contradictions,
                        "hints": hint.get("Used", []),
                        "xp": player_record.get("XP", 0),
                        "rating": earned_rating,
                        "rank": player_record.get("Rank", "Rookie")
                    }
                )

                ui.AccusationUI.culprit_ui(records)


                # ---------  FOR SAFTY : HANDLE POSSILBE CASES --------------
                case_i = int(case_id.split("_")[-1])
                
                brief = detective_x.GenerativeSystem.case_briefing_screen()
                if not brief.get(case_i):
                    print("[!] Brief case not found.")
                    return False
                
                
                # collect cases as record
                data = {
                    "name": player_inv['Detective'],
                    "case_id": case_id,
                    "title": player_inv['Title'],
                    "difficulty": player_inv['Difficulty'],
                    "location": player_inv['Location'],
                    "culprit": culprit,
                    "briefing": brief[case_i],
                    "suspects": list(suspects.Dispatch.suspects_map.get(case_id, {}).values()),
                }
                
                #  -------------  SAVE THE CASE AS RECORD -----------------
                SYSTEM.create_new(data, FILE_DATA / f"{case_id}.json")
                

                # Narrative breakdown of how crime happened and clues connect
                print("➤ HOW THE CRIME HAPPENED:")
                print(f"➥ {case_solution.get('crime_story', '')}\n")
                print("➤ HOW THE CLUES CONNECT:")
                print(f"➥ {case_solution.get('clues_connection', '')}")

                input("\nPress Enter to return to Main Menu...")
                return True

            except ValueError:
                print("[!] Invalid option.")
            
            except Exception as e:
                print(f"Error: {e}")

