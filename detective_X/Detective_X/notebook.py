import json
from pathlib import Path
import locations

# ---------- Config -----------
base = Path(__file__).parent
FILE = base / "player_record.json"
FILE_INV = base / "investigation.json"


class InvestigationNotebook:
    """Dynamic detective notebook tracking confirmed findings and open questions."""
    NOTEBOOK_ENTRIES = {
        "case_001": [
            {
                "category": "Finding",
                "clue_needed": "Scratch marks on the diamond case lock",
                "confirmed_text": "Diamond case lock picked from inside",
                "open_text": "Was diamond case forced or picked?"
            },
            {
                "category": "Finding",
                "clue_needed": "Tampered alarm wire in access panel",
                "confirmed_text": "Alarm wire cleanly severed in panel",
                "open_text": "How was the security alarm disabled?"
            },

            {
                "category": "Timeline",
                "clue_needed": "Access log: Keycard #7 used at 11:45 PM",
                "confirmed_text": "11:45 PM: Keycard #7 used at security door",
                "open_text": "Whose keycard was used before blackout?"
            },
            {
                "category": "Timeline",
                "clue_needed": "CCTV footage: figure at 11:47 PM",
                "confirmed_text": "11:47 PM: Figure in guard uniform on CCTV",
                "open_text": "Who was the shadowy figure on CCTV?"
            },
            {
                "category": "Timeline",
                "clue_needed": "Crumpled note: '11:30 PM — east exit'",
                "confirmed_text": "11:30 PM: Note planned rendezvous at east exit",
                "open_text": "Did the thief plan a midnight meeting?"
            },

            {
                "category": "Compared Evidence",
                "clue_needed": "Scratched emergency exit push-bar",
                "confirmed_text": "Lock scratches match emergency push-bar",
                "open_text": "Which exit door did the thief escape through?"
            },
            {
                "category": "Compared Evidence",
                "clue_needed": "Muddy shoe marks on window ledge",
                "confirmed_text": "Window ledge prints match escape footwear",
                "open_text": "Were windows used as an escape route?"
            },

            {
                "category": "Contradiction",
                "clue_needed": "Crumpled note: '11:30 PM — east exit'",
                "confirmed_text": "Arthur's alibi contradicted by rendezvous note",
                "open_text": "Was Arthur Vance asleep in his quarters?"
            },
            {
                "category": "Contradiction",
                "clue_needed": "Wine glass with lipstick at seat 4",
                "confirmed_text": "Evelyn's presence confirmed near crime scene",
                "open_text": "Was Evelyn Reed truly in the ballroom?"
            },
            {
                "category": "Contradiction",
                "clue_needed": "Muddy footprint near the case",
                "confirmed_text": "Thomas's shoes match size 10 muddy footprint",
                "open_text": "Who left the size 10 prints near the case?"
            },
        ],


        "case_002": [
            {
                "category": "Finding",
                "clue_needed": "Rogue Raspberry Pi plugged into Rack C",
                "confirmed_text": "Hardware sniffer identified on Rack C",
                "open_text": "How was encrypted project data tapped?"
            },
            {
                "category": "Finding",
                "clue_needed": "Console session open under 'root_admin'",
                "confirmed_text": "Root admin console active during breach",
                "open_text": "Whose credentials bypassed root security?"
            },
            {
                "category": "Finding",
                "clue_needed": "Empty encrypted drive compartment",
                "confirmed_text": "Source code SSD missing from server bay",
                "open_text": "What physical storage media was taken?"
            },

            {
                "category": "Timeline",
                "clue_needed": "Fast food receipt at 11:40 PM",
                "confirmed_text": "11:40 PM: Suspect purchase near server facility",
                "open_text": "Who was near facility prior to breach?"
            },
            {
                "category": "Timeline",
                "clue_needed": "UPS surge bypass record",
                "confirmed_text": "11:58 PM: UPS surge triggered power outage",
                "open_text": "What caused the midnight power surge?"
            },

            {
                "category": "Compared Evidence",
                "clue_needed": "Unlocked fire escape latch",
                "confirmed_text": "Fire escape latch matches intruder exit path",
                "open_text": "How did physical intruder leave building?"
            },
            {
                "category": "Compared Evidence",
                "clue_needed": "Foreign IP address traffic destination",
                "confirmed_text": "Port 8080 alteration routed data to foreign IP",
                "open_text": "Where was the exfiltrated data sent?"
            },

            {
                "category": "Contradiction",
                "clue_needed": "Sticky note with override password",
                "confirmed_text": "Kevin's alibi broken: Left password on sticky note",
                "open_text": "Was Kevin Miller's admin account secure?"
            },
            {
                "category": "Contradiction",
                "clue_needed": "Dropped contractor visitor badge",
                "confirmed_text": "Sarah Lin's contractor badge confirms presence",
                "open_text": "Did Sarah Lin work purely remotely that night?"
            },
            {
                "category": "Contradiction",
                "clue_needed": "Rogue Raspberry Pi plugged into Rack C",
                "confirmed_text": "Marcus Vance's MAC address matches rogue hardware",
                "open_text": "Was Marcus Vance involved after resignation?"
            },
        ],


        "case_003": [
            {
                "category": "Finding",
                "clue_needed": "Missing 50ml Potassium Cyanide bottle",
                "confirmed_text": "Potassium Cyanide missing from chemical vault",
                "open_text": "What lethal agent poisoned the professor?"
            },
            {
                "category": "Finding",
                "clue_needed": "Corrosive acid wash down the drain",
                "confirmed_text": "Acid flushed down sink drain to destroy toxins",
                "open_text": "How did culprit destroy chemical residue?"
            },
            {
                "category": "Finding",
                "clue_needed": "Discarded vinyl gloves smelling of almonds",
                "confirmed_text": "Cyanide-tainted vinyl gloves found in bin",
                "open_text": "Where did poisoner discard forensic gear?"
            },

            {
                "category": "Timeline",
                "clue_needed": "Torn calendar page marked 'Dinner 8 PM'",
                "confirmed_text": "8:00 PM: Faculty dinner took place before collapse",
                "open_text": "When did victim last meet with suspects?"
            },
            {
                "category": "Timeline",
                "clue_needed": "Lethal dose of cyanide in Earl Grey cup",
                "confirmed_text": "9:30 PM: Lethal cyanide ingested in Earl Grey tea",
                "open_text": "How was the lethal poison administered?"
            },

            {
                "category": "Compared Evidence",
                "clue_needed": "Sugar dispenser contaminated with powder",
                "confirmed_text": "Sugar dispenser powder matches Earl Grey tea cup",
                "open_text": "Was toxin put in tea cup or sugar container?"
            },
            {
                "category": "Compared Evidence",
                "clue_needed": "Traces of bitter almond residue",
                "confirmed_text": "Bitter almond scent matches missing Cyanide vial",
                "open_text": "Was the collapse caused by natural causes?"
            },

            {
                "category": "Contradiction",
                "clue_needed": "Hostile tenure dispute letter",
                "confirmed_text": "Dr. Higgins's dispute letter exposes tenure motive",
                "open_text": "Did Dr. Clara Higgins hold a grudge?"
            },
            {
                "category": "Contradiction",
                "clue_needed": "Falsified checkout signature in log",
                "confirmed_text": "Julian Drake forged signature in chemical log",
                "open_text": "Did Julian Drake check out chemicals legitimately?"
            },
            {
                "category": "Contradiction",
                "clue_needed": "Patent dispute lawsuit draft",
                "confirmed_text": "Dean Hayes concealed multi-million patent lawsuit",
                "open_text": "Was Dean Hayes truthful about grant disputes?"
            },
        ]
    }      
    
    @classmethod
    def display_notebook(cls, player_id: str, case_id: str):
        # load record
        RECORDS = locations.Helper._load_record(FILE_INV)
        if not RECORDS:
            print("[!] Record not found.")
            return

        # get active case record
        player_record = next(
            (record for record in RECORDS.get(player_id, []) if record['Case'] == case_id),
            None
        )

        if not player_record:
            print("[!] Player record not found.")
            return

        if not player_record['Evidence']:
            print("[!] No evidence found.")
            return 

        ENTRIES = cls.NOTEBOOK_ENTRIES.get(case_id)
        if not ENTRIES:
            print("[!] No Entries found.")
            return

        confirmation_rec = []
        open_text = []
        for entries in ENTRIES:                
            text_cleaner = lambda s: " ".join(s.replace("—", " ").replace("-", " ").split())
            
            if any(text_cleaner(entries["clue_needed"]) == text_cleaner(clue) for clue in player_record.get("Evidence", [])):
                confirmation_rec.append(f"✓ {entries['confirmed_text']}")
                
            else:
                open_text.append(f"? {entries['open_text']}")
        

        width = 60
        print("╔" + "═" * width + "╗")
        print(f"║{'INVESTIGATION NOTEBOOK'.center(width)}║")
        print("╠" + "═" * width + "╣")

        for confirm in confirmation_rec:
            print(f"║{confirm:<{width}}║")
        
        for lines in open_text:
            print(f"║{lines:<{width}}║")
        
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")
        
        input("\nPress Enter to return to Dashboard...")
        
        
if __name__ == "__main__":
    InvestigationNotebook.display_notebook('P0001', "case_001")