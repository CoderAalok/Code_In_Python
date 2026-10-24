import json
from pathlib import Path
import ui, locations
base = Path(__file__).parent
FILE_INV = base / "investigation.json"
FILE = base / "player_record.json"



# ──────────── HELPERS ──────────────────────
Helper = locations.Helper

# ──────────── ROUTING DISPATCH ────────────
class Dispatch:
    SUSPECTS1 = {
        1: {
            "name": "Arthur Vance",
            "role": "Head Butler",
            "age": 54,
            "alibi": "Wine cellar from 11:15 to 11:55 PM selecting vintage wines.",
            "motive": "Severe gambling debts to underground creditors.",
            "status": "Unquestioned",
            "contradiction_clue": "Crumpled note: '11:30 PM — east exit'",
            "questions": {
                1: (
                    "Inquire about whereabouts at 11:45 PM",
                    "Arthur: 'I was down in the private wine cellar inventorying bottles.\n"
                    " The cellar door is heavy oak and soundproof, Detective. I heard nothing.'"
                ),
                2: (
                    "Ask about relationship with Lord Blackwood",
                    "Arthur: 'I have served the Blackwood family loyally for fifteen years.\n"
                    " His lordship pays me handsomely. Why would I jeopardize my position?'"
                ),
                3: (
                    "Confront with Crumpled East Exit Note",
                    "Arthur: *hesitates and turns pale*\n"
                    " 'T-that note... Alright, I admit it! I was meeting a loan shark at the east exit\n"
                    " to beg for more time on my debts. But when I got there, someone ran past me toward\n"
                    " the gardens in a guard uniform! I swear I did NOT touch the diamond!'"
                )
            }
        },
        
        2: {
            "name": "Evelyn Reed",
            "role": "Gala Coordinator",
            "age": 38,
            "alibi": "Private phone call on dining balcony with champagne guests.",
            "motive": "Facing bankruptcy after a failed luxury jewelry venture.",
            "status": "Unquestioned",
            "contradiction_clue": "Wine glass with lipstick at seat 4",
            "questions": {
                1: (
                    "Inquire about whereabouts at 11:45 PM",
                    "Evelyn: 'I was on the terrace on a call with our pastry supplier until midnight.\n"
                    " Several prestigious donors saw me there and can vouch for me.'"
                ),
                2: (
                    "Ask about access to the exhibition hall",
                    "Evelyn: 'As the event planner, I had the schedule, but only authorized security\n"
                    " guards had keycards to the diamond display case.'"
                ),
                3: (
                    "Confront with Wine Glass & Lipstick Mark",
                    "Evelyn: 'Yes, that is my shade of lipstick at table 4. I took two sips of champagne\n"
                    " before heading out to take my call. Check with the guests—I never went near the gallery!'"
                )
            }
        },
        
        3: {
            "name": "Thomas Blackwood",
            "role": "Estranged Nephew",
            "age": 29,
            "alibi": "Claims he had a migraine and left the mansion before 11:00 PM.",
            "motive": "Disinherited playboy facing immense debts; size 10 boot wearer.",
            "status": "Unquestioned",
            "contradiction_clue": "Muddy footprint near the case",
            "questions": {
                1: (
                    "Inquire about whereabouts at 11:45 PM",
                    "Thomas: 'I told you already, Detective! My head was throbbing, so I hailed an Uber\n"
                    " and left before 11:00 PM. I wasn't even in the mansion when the diamond vanished.'"
                ),
                2: (
                    "Ask about his disinheritance by Lord Blackwood",
                    "Thomas: *scoffs bitterly*\n"
                    " 'My uncle is a greedy old hypocrite. Cut me off because I wouldn't work at his firm.\n"
                    " But stealing? That's ridiculous. I have standards.'"
                ),
                3: (
                    "Confront with Muddy Size 10 Footprint & Security Log",
                    "Thomas: *eyes widen in panic*\n"
                    " 'Muddy boots?! Keycard #7?! That—that's circumstantial garbage!\n"
                    " Anyone could wear size 10 boots! You have no proof it was me!'"
                )
            }
        }
    }


    SUSPECTS2 = {
        1: {
            "name": "Kevin Miller",
            "role": "Lead Network Admin",
            "age": 36,
            "alibi": "Clocked out at 6:00 PM and streamed video games from home all night.",
            "motive": "Bitter after being passed over for promotion to Chief Security Officer.",
            "status": "Unquestioned",
            "contradiction_clue": "Sticky note with admin credentials",
            "questions": {
                1: (
                    "Inquire about whereabouts during midnight breach",
                    "Kevin: 'I was in my apartment streaming gameplay on Twitch from 8 PM to 2 AM.\n"
                    " Hundreds of viewers in my stream chat can verify I was live all night.'"
                ),
                2: (
                    "Ask about root access to the core server vault",
                    "Kevin: 'I manage the domain controllers, so of course I have root privileges.\n"
                    " But all commands are logged. I wouldn't be foolish enough to use my own console.'"
                ),
                3: (
                    "Confront with Sticky Note with Admin Credentials",
                    "Kevin: *turns pale and drops his pen in shock*\n"
                    " 'W-where did you find that?! That was taped under my keyboard in the NOC!\n"
                    " IT forced a 24-character password change last week so I wrote it down.\n"
                    " Someone must have snuck to my desk and stolen it! I swear I didn't initiate that breach!'"
                )
            }
        },
        2: {
            "name": "Sarah Lin",
            "role": "Cloud Migration Contractor",
            "age": 31,
            "alibi": "Dinner downtown with partner until 11:30 PM, then went home to sleep.",
            "motive": "Severe personal debt from her failing side-consulting startup.",
            "status": "Unquestioned",
            "contradiction_clue": "Dropped contractor visitor badge",
            "questions": {
                1: (
                    "Inquire about physical presence in the datacenter",
                    "Sarah: 'I work remotely on the AWS migration 90% of the time.\n"
                    " I had no reason to be on-site last night. I was having sushi downtown until late.'"
                ),
                2: (
                    "Ask about authorization for server vault access",
                    "Sarah: 'Contractors are restricted to the staging suite.\n"
                    " None of our badges have clearance to open the main Server Vault or CSO office.'"
                ),
                3: (
                    "Confront with Dropped Contractor Visitor Badge #449",
                    "Sarah: *eyes widen in shock and disbelief*\n"
                    " 'My visitor badge?! I filed an incident ticket three days ago saying I lost it in the lobby!\n"
                    " Check the security log—someone stole my badge #449 to bypass the turnstiles!\n"
                    " I had nothing to do with planting rogue hardware!'"
                )
            }
        },
        3: {
            "name": "Marcus Vance",
            "role": "Disgruntled Ex-Developer",
            "age": 42,
            "alibi": "Drinking alone at a local dive bar until closing time at 2:00 AM.",
            "motive": "Fired two weeks ago; Project Aegis was his creation; stole source code for revenge.",
            "status": "Unquestioned",
            "contradiction_clue": "Rogue Raspberry Pi plugged into Rack C",
            "questions": {
                1: (
                    "Inquire about whereabouts during the breach",
                    "Marcus: *smirks coldly and takes a slow sip*\n"
                    " 'I was nursing scotch at The Rusty Anchor bar until closing time.\n"
                    " Nobody bothers me there, and I don't bother anyone else.'"
                ),
                2: (
                    "Ask about his dismissal from Project Aegis",
                    "Marcus: *clenches teeth with simmering rage*\n"
                    " 'Project Aegis was MY life's work! 40,000 lines of custom firmware!\n"
                    " Management terminated me two weeks before the patent so they could keep the equity.\n"
                    " But breaking in? Why bother? They can rot for all I care.'"
                ),
                3: (
                    "Confront with Rogue Raspberry Pi on Rack C",
                    "Marcus: *expression violently snaps into panic and fury*\n"
                    " 'A Raspberry Pi on Rack C?! How... how did your security team trace that in the dark?!\n"
                    " That bypass packet-sniffer was supposed to trigger as a power glitch!\n"
                    " Aegis was MINE! They had no right to lock me out of my own code!'"
                )
            }
        }
    }


    SUSPECTS3 = {
        1: {
            "name": "Dr. Clara Higgins",
            "role": "Rival Biochemistry Researcher",
            "age": 44,
            "alibi": "Working late in her private study revising a grant proposal until 10:30 PM.",
            "motive": "Professor Bell blocked her $2M federal research grant and opposed her tenure.",
            "status": "Unquestioned",
            "contradiction_clue": "Threatening tenure rejection dispute letter",
            "questions": {
                1: (
                    "Inquire about whereabouts during the faculty dinner",
                    "Dr. Higgins: 'I boycotted that dinner. Jonathan Bell made it his personal mission\n"
                    " to demean my research. I was in my private office rewriting my grant submission.'"
                ),
                2: (
                    "Ask about access to the Poison Reagent Cabinet",
                    "Dr. Higgins: 'As an associate professor, I have keys to the chemical storage.\n"
                    " But dozens of researchers use that lab. Jonathan had enemies everywhere.'"
                ),
                3: (
                    "Confront with Threatening Dispute Letter",
                    "Dr. Higgins: *eyes flare with anger, then nervously waver*\n"
                    " 'That letter was written in frustration! He threatened to revoke my tenure!\n"
                    " Yes, I confronted him in his study at 7:00 PM, but he was alive and drinking his tea when I left!\n"
                    " I had nothing to do with cyanide!'"
                )
            }
        },
        2: {
            "name": "Julian Drake",
            "role": "Senior Graduate Lab Assistant",
            "age": 26,
            "alibi": "Grading undergraduate chemistry midterm exams in the university library.",
            "motive": "Bell discovered Julian falsified doctoral data and drafted an academic misconduct expulsion.",
            "status": "Unquestioned",
            "contradiction_clue": "Missing 50ml Potassium Cyanide bottle",
            "questions": {
                1: (
                    "Inquire about movements on the evening of the collapse",
                    "Julian: 'I was in the quiet study cubicles in the library grading lab papers.\n"
                    " I didn't even know Professor Bell had collapsed until the ambulance sirens arrived.'"
                ),
                2: (
                    "Ask about his doctoral dissertation and relationship with Bell",
                    "Julian: 'Professor Bell was my mentor. He pushed me hard, but we were on the verge\n"
                    " of publishing breakthrough cancer research together. I owed him my whole career.'"
                ),
                3: (
                    "Confront with Missing Cyanide Bottle & Nitrile Residue",
                    "Julian: *hands begin trembling uncontrollably as his voice cracks in panic*\n"
                    " 'Cyanide bottle #42?! Nitrile gloves in the lounge trash?!\n"
                    " He was going to ruin me! He drafted a misconduct report to revoke my PhD and ban me for life!\n"
                    " Four years of research... gone! I just wanted him sick so he couldn't file the report!\n"
                    " I didn't think the dose would kill him!'"
                )
            }
        },
        3: {
            "name": "Dean Robert Hayes",
            "role": "Dean of Faculty of Science",
            "age": 58,
            "alibi": "Hosting high-profile alumni and private university benefactors downtown.",
            "motive": "Bell discovered Hayes was embezzling departmental endowment funds.",
            "status": "Unquestioned",
            "contradiction_clue": "Stolen departmental grant allocation file",
            "questions": {
                1: (
                    "Inquire about whereabouts on the night of the incident",
                    "Dean Hayes: 'I was hosting a black-tie endowment gala at the Grand Plaza Hotel.\n"
                    " The university president and dozens of wealthy donors can verify I was on stage all night.'"
                ),
                2: (
                    "Ask about financial tensions with Professor Bell",
                    "Dean Hayes: 'Jonathan was a brilliant scientist, but administratively impossible.\n"
                    " Constantly demanding bigger budgets. But murder? That is preposterous.'"
                ),
                3: (
                    "Confront with Stolen Grant Allocation File",
                    "Dean Hayes: *clears throat uncomfortably and straightens his silk tie*\n"
                    " 'A missing grant audit file? That is strictly confidential university business, Detective.\n"
                    " Jonathan was auditing our accounts, but my records are pristine.\n"
                    " Check the gala cameras—I was five miles away when his tea was poisoned!'"
                )
            }
        }
    }


    suspects_map = {
        'case_001': SUSPECTS1,
        'case_002': SUSPECTS2,
        'case_003': SUSPECTS3,
    }
    
    @classmethod
    def view_suspect_profiles(cls, player_id: str, case_id: str):
        suspect = cls.suspects_map.get(case_id)
        if not suspect:
            print("[!] Case ID not match.")
            return
        
        try:
            # Profile View
            CaseSuspects(suspect).view_profiles(player_id, case_id)

        except Exception as e:
            print(f"Error: {e}")

    # Detective ask questions to suspects 
    @classmethod
    def question_suspects(cls, player_id: str, case_id: str):
        suspect = cls.suspects_map.get(case_id)
        
        if not suspect:
            print("[!] Case ID not match.")
            return
        
        try:
            # suspects  questions
            CaseSuspects(suspect).question_suspects(player_id, case_id)
            
        except Exception as e:
            print(f"Error: {e}")
     

# ──────────── CASE SUSPECTS ────────────
class CaseSuspects:
    """Suspect database and interrogation logic for Cases."""
    def __init__(self, suspects):
        self.SUSPECTS = suspects


    def view_profiles(self, player_id, case_id):
        inv_data = Helper._load_record(FILE_INV)
        record = Helper._get_record(inv_data, player_id, case_id)

        if not record:
            print("Record is empty!")
            return
        
        # collect those suspects name who profile already viewed
        record["Suspects"].extend(suspect["name"] for suspect in self.SUSPECTS.values() if suspect["name"] not in record["Suspects"])

        # save record
        Helper._save_record(inv_data, FILE_INV)

        # --------- LOOP ----------
        while True:
            ui.UI.suspect_selection_ui(self.SUSPECTS, title="SUSPECT DOSSIERS")
            try:
                choice = int(input("Select suspect to inspect [0-3]: ").strip())
                if choice == 0:
                    return

                suspect = self.SUSPECTS.get(choice)
                if not suspect:
                    print("[!] Invalid option. Select [0-3].")
                    continue
                
                # suspect profile
                ui.UI.suspect_profile_ui(suspect)
                
                input("\nPress Enter to return to suspect list...")

            except ValueError:
                print("[!] Please enter a number.")
                
            except Exception as e:
                print(f"Error: {e}")


    def question_suspects(self, player_id, case_id):
        inv_data = Helper._load_record(FILE_INV)
        record = Helper._get_record(inv_data, player_id, case_id)

        if not record:
            print("Investigation record not found!")
            return

        # collect those suspects name who profile already viewed
        record["Suspects"].extend(suspect["name"] for suspect in self.SUSPECTS.values() if suspect["name"] not in record["Suspects"])

        # save record
        Helper._save_record(inv_data, FILE_INV)

        # --------- LOOP ----------
        while True:
            ui.UI.suspect_selection_ui(self.SUSPECTS, title="QUESTION SUSPECTS")
            try:
                choice = int(input("Select suspect to interrogate [0-3]: ").strip())
                if choice == 0:
                    return

                suspect = self.SUSPECTS.get(choice)
                if suspect is None:
                    print("[!] Invalid option. Select [0-3].")
                    continue

                # Mark suspect as questioned
                suspect["status"] = "Questioned"

                # Interrogation submenu
                self._interrogate(player_id, case_id, suspect)

            except ValueError:
                print("[!] Select valid option[0-3].")
                
            except Exception as e:
                print(f"Error: {e}")


    # Interrrogate pluged to question_suspects
    def _interrogate(self, player_id, case_id, suspect):
        while True:
            ui.UI.interrogation_ui(suspect["name"], suspect["questions"])
            try:
                q_choice = int(input("Choose question [0-3]: ").strip())
                if q_choice == 0:
                    return

                if q_choice not in suspect["questions"]:
                    print("[!] Invalid choice. Only select [0-3].")
                    continue

                q_label, q_response = suspect["questions"][q_choice]
                print(f"\n[{suspect["name"]}]: {q_label}")
                print(f"{q_response}\n")

                # Handle Question 3 (Confrontation & Contradiction)
                if q_choice == 3:
                    self._handle_confrontation(player_id, case_id, suspect)

                input("Press Enter to continue questioning...")

            except ValueError:
                print("[!] Select valid option [0-3].")
            except Exception as e:
                print(f"Error: {e}")


    # _handle_confrontation  pluged to interrogate
    def _handle_confrontation(self, player_id, case_id, suspect):
        inv_data = Helper._load_record(FILE_INV)
        record = Helper._get_record(inv_data, player_id, case_id)
        player_data = Helper._load_record(FILE)
        detective = player_data.get(player_id, {})

        if not record or not detective:
            return

        needed_clue = suspect["contradiction_clue"]
        collected_evidence = record.get("Evidence", [])

        text_cleaner = lambda s: " ".join(s.replace("-", " ").replace("—", " ").split())
        
        # Check whether detective has found the required clue
        has_clue = any(text_cleaner(needed_clue.lower()) in text_cleaner(ev.lower()) for ev in collected_evidence)

        if not has_clue:
            print(f"⚠️  [HINT]: You have not found the clue '{needed_clue}' yet!")
            print("   Search more rooms before confronting this suspect.\n")
            return

        # Check if contradiction was already caught
        if suspect["name"] in record['Contradictions']:
            print(f"[✓] You already exposed {suspect['name']}'s contradiction earlier.\n")
            return

        # prevent giving points to the same suspects
        if suspect["name"] not in record["Contradictions"]:
            # ADD CONTRADICTION DETECTED!
            record['Contradictions'].append(suspect["name"])  # This suspect lying proven

            # give award
            record["Scores"] += 50
            detective["XP"] += 25
            detective["Rank"] = Helper.get_rank(detective["XP"])

        # save record
        Helper._save_record(inv_data, FILE_INV)
        Helper._save_record(player_data, FILE)

        print("╔" + "═" * 55 + "╗")
        print("║" + "🚨 CONTRADICTION DETECTED! 🚨".center(55) + "║")
        print("╠" + "═" * 55 + "╣")
        
        print(f"║ {'• Contradiction proven against ' + suspect['name'] + '!':<53} ║")
        print(f"║ {'• Score +50 pts awarded!':<53} ║")
        print(f"║ {'• Detective XP +25 awarded! (Rank: ' + detective['Rank'] + ')':<53} ║")
        
        print("╚" + "═" * 55 + "╝\n")

    