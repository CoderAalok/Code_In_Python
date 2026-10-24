import locations
from pathlib import Path

# ------------ Config ------------
base = Path(__file__).parent
FILE_INV = base / "investigation.json"


class TimeLine:
    TIMELINE_DATA = {
        "case_001": [
            {"time": "10:00 PM", "clue_needed": None, "event": "Gala commences in ballroom"},
            {"time": "11:15 PM", "clue_needed": None, "event": "Diamond verified on display"},
            {"time": "11:30 PM", "clue_needed": "Crumpled note: '11:30 PM — east exit'", "event": "Rendezvous note dropped at exit"},
            {"time": "11:45 PM", "clue_needed": "Access log: Keycard #7 used at 11:45 PM", "event": "Keycard #7 used at security door"},
            {"time": "11:46 PM", "clue_needed": "Tampered alarm wire in access panel", "event": "Alarm wire cut; blackout triggered"},
            {"time": "11:47 PM", "clue_needed": "CCTV footage: figure at 11:47 PM", "event": "Figure in guard uniform on CCTV"},
            {"time": "11:50 PM", "clue_needed": "Scratched emergency exit push-bar", "event": "Emergency exit push-bar forced open"},
            {"time": "11:55 PM", "clue_needed": None, "event": "Diamond reported missing"},
        ],

        "case_002": [
            {"time": "11:00 PM", "clue_needed": None, "event": "NOC regular evening staff log out"},
            {"time": "11:40 PM", "clue_needed": "Fast food receipt at 11:40 PM", "event": "Suspect purchase made near facility"},
            {"time": "11:55 PM", "clue_needed": "Rogue Raspberry Pi plugged into Rack C", "event": "Rogue hardware sniffer tapped Rack C"},
            {"time": "11:58 PM", "clue_needed": "UPS surge bypass record", "event": "UPS surge bypass triggered blackout"},
            {"time": "12:00 AM", "clue_needed": "Console session open under 'root_admin'", "event": "Root console session open on switch"},
            {"time": "12:05 AM", "clue_needed": "Foreign IP address traffic destination", "event": "Data exfiltration routed to foreign IP"},
            {"time": "12:12 AM", "clue_needed": "Unlocked fire escape latch", "event": "Intruder fled through fire escape"},
            {"time": "12:20 AM", "clue_needed": None, "event": "Off-site security audit triggered"},
        ],

        "case_003": [
            {"time": "07:30 PM", "clue_needed": "Missing 50ml Potassium Cyanide bottle", "event": "Potassium Cyanide missing from vault"},
            {"time": "08:00 PM", "clue_needed": "Torn calendar page marked 'Dinner 8 PM'", "event": "Faculty dinner begins in dining hall"},
            {"time": "08:45 PM", "clue_needed": None, "event": "Professor orders Earl Grey tea"},
            {"time": "09:15 PM", "clue_needed": "Falsified checkout signature in log", "event": "Lab 304 re-entered under forged log"},
            {"time": "09:30 PM", "clue_needed": "Lethal dose of cyanide in Earl Grey cup", "event": "Cyanide ingested via Earl Grey cup"},
            {"time": "09:35 PM", "clue_needed": "Corrosive acid wash down the drain", "event": "Acid flushed down sink to wipe traces"},
            {"time": "09:45 PM", "clue_needed": None, "event": "Professor collapses; emergency summoned"},
        ]
    }

    
    @classmethod
    def time_line(cls, player_id: str, case_id: str):
        # load record
        RECORDS = locations.Helper._load_record(FILE_INV)
        if not RECORDS:
            print("[!] No investigation record not found.")
            return

        # get player record
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

        timelines = []
        text_cleaner = lambda s: " ".join(s.replace("-", " ").replace("—", " ").split())
        collected_evidence = player_record.get("Evidence", [])
        
        for data in cls.TIMELINE_DATA.get(case_id, []):
            if data.get('clue_needed') is None:
                timelines.append(f" ✓ {data['time']} - {data['event']}")
            
            elif any(text_cleaner(data.get("clue_needed").lower()) == text_cleaner(clue.lower()) for clue in collected_evidence):
                timelines.append(f" ✓ {data['time']} - {data['event']}")

            else:
                timelines.append(f" ? {data['time']} - [ Hidden Event - Search rooms ]")

        
        width = 60
        print("╔" + "═" * width + "╗")
        print(f"║{'CRIME TIMELINE'.center(width)}║")
        print("╠" + "═" * width + "╣")

        for line in timelines:
            print(f"║{line:<{width}}║")
        
        print("║" + " " * width + "║")
        print("╚" + "═" * width + "╝")
        
        input("\nPress Enter to return to Dashboard...")


if __name__ == "__main__":
    TimeLine.time_line('P0003', 'case_002')