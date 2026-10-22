import json
from pathlib import Path

# ---------- Config -----------
base = Path(__file__).parent
FILE = base / "player_record.json"
FILE_INV = base / "investigation.json"


class InvestigationNotebook:
    """Dynamic detective notebook tracking confirmed findings and open questions."""

    NOTEBOOK_ITEMS = {
        "case_001": [
            {
                "trigger": "Scratch marks on the diamond case lock",
                "confirmed": "Diamond case lock was picked from inside",
                "open": "Was diamond case forced open or picked from inside?"
            },
            {
                "trigger": "Tampered alarm wire in access panel",
                "confirmed": "Security alarm wire was deliberately cut in access panel",
                "open": "How was the exhibition room alarm silenced?"
            },
            {
                "trigger": "Access log: Keycard #7 used at 11:45 PM",
                "confirmed": "Keycard #7 swiped at security door at 11:45 PM",
                "open": "Whose keycard was swiped prior to the blackout?"
            },
            {
                "trigger": "CCTV footage: figure at 11:47 PM",
                "confirmed": "CCTV captured shadowy figure fleeing at 11:47 PM",
                "open": "Who was the shadowy figure captured on CCTV cameras?"
            },
            {
                "trigger": "Crumpled note: '11:30 PM — east exit'",
                "confirmed": "Rendezvous note planned meeting at east exit at 11:30 PM",
                "open": "Did an insider coordinate a midnight escape plan?"
            },
            {
                "trigger": "Scratched emergency exit push-bar",
                "confirmed": "East emergency exit push-bar was forced for the escape",
                "open": "Which exit door did the perpetrator escape through?"
            },
            {
                "trigger": "Muddy footprint near the case",
                "confirmed": "Thomas Blackwood's size 10 shoes match muddy prints",
                "open": "Who left the size 10 muddy prints near the case?"
            },
            {
                "trigger": "Wine glass with lipstick at seat 4",
                "confirmed": "Evelyn Reed's lipstick confirms presence near crime scene",
                "open": "Was Evelyn Reed truly in the main ballroom all night?"
            },
            {
                "trigger": "Torn uniform cloth on guard desk",
                "confirmed": "Torn uniform cloth links night guard to the crime scene",
                "open": "Was security personnel involved in the theft?"
            },
            {
                "trigger": "Muddy shoe marks on window ledge",
                "confirmed": "Muddy shoe prints on window ledge match escape trail",
                "open": "Were windows used as an alternate entry or exit?"
            }
        ],
        "case_002": [
            {
                "trigger": "Rogue Raspberry Pi plugged into Rack C",
                "confirmed": "Marcus Vance's rogue Raspberry Pi created a hardware backdoor",
                "open": "Who installed the unauthorized hardware sniffer?"
            },
            {
                "trigger": "Dropped contractor visitor badge",
                "confirmed": "Sarah Lin's contractor badge confirms unauthorized access",
                "open": "Did third-party contractors have off-hours server access?"
            },
            {
                "trigger": "Sticky note with override password",
                "confirmed": "Kevin Miller's override password compromised root access",
                "open": "How were root administrative privileges obtained?"
            },
            {
                "trigger": "Console session open under 'root_admin'",
                "confirmed": "Root admin console session was active during the breach",
                "open": "Whose credentials were used to bypass the root firewall?"
            },
            {
                "trigger": "Foreign IP address traffic destination",
                "confirmed": "Exfiltrated company data was routed to offshore foreign IP",
                "open": "Where was the stolen confidential project data sent?"
            },
            {
                "trigger": "Unlocked fire escape latch",
                "confirmed": "Physical intruder escaped via unlocked fire escape latch",
                "open": "How did the physical intruder enter and leave the facility?"
            },
            {
                "trigger": "UPS surge bypass record",
                "confirmed": "UPS surge bypass was triggered to induce simulated blackout",
                "open": "What caused the momentary power surge in Server Room B?"
            }
        ],
        "case_003": [
            {
                "trigger": "Missing 50ml Potassium Cyanide bottle",
                "confirmed": "Potassium Cyanide identified as the missing lethal agent",
                "open": "What toxic substance caused Professor Sterling's collapse?"
            },
            {
                "trigger": "Lethal dose of cyanide in Earl Grey cup",
                "confirmed": "Cyanide was administered via Sterling's Earl Grey cup",
                "open": "How was the poison delivered to the victim?"
            },
            {
                "trigger": "Hostile tenure dispute letter",
                "confirmed": "Dr. Clara Higgins's dispute letter reveals hostile tenure motive",
                "open": "Did rival faculty members harbor motives against Sterling?"
            },
            {
                "trigger": "Patent dispute lawsuit draft",
                "confirmed": "Dean Robert Hayes suppressed patent dispute royalties",
                "open": "Were valuable commercial research patents contested?"
            },
            {
                "trigger": "Falsified checkout signature in log",
                "confirmed": "Julian Drake's forged chemical checkout signature confirmed",
                "open": "Who signed out the restricted chemical inventory?"
            },
            {
                "trigger": "Discarded vinyl gloves smelling of almonds",
                "confirmed": "Discarded vinyl gloves with cyanide residue found in trash",
                "open": "Where did the poisoner discard their forensic gear?"
            },
            {
                "trigger": "Traces of bitter almond residue",
                "confirmed": "Bitter almond cyanide residue confirms targeted poisoning",
                "open": "Was the collapse accidental or premeditated poisoning?"
            }
        ]
    }

    @classmethod
    def display_notebook(cls, player_id: str, case_id: str):
        """Renders the investigation notebook showing confirmed findings and open questions."""
        try:
            with open(FILE_INV, "r", encoding="utf-8") as f:
                inv_data = json.load(f)
        except Exception:
            inv_data = {}

        player_cases = inv_data.get(player_id, [])
        record = next((c for c in player_cases if c.get("Case") == case_id), None)

        if not record:
            print("[!] Investigation record not found.")
            return

        evidence_collected = [e.lower() for e in record.get("Evidence", [])]
        contradictions_caught = [c.lower() for c in record.get("Contradictions", [])]

        items = cls.NOTEBOOK_ITEMS.get(case_id, cls.NOTEBOOK_ITEMS.get("case_001", []))

        confirmed_list = []
        open_list = []

        for item in items:
            trigger = item["trigger"].lower()
            # Clean trigger and evidence for robust fuzzy matching
            import re
            clean_trigger = re.sub(r"[^a-z0-9 ]", "", trigger)

            is_confirmed = False
            for ev in evidence_collected:
                clean_ev = re.sub(r"[^a-z0-9 ]", "", ev)
                if clean_trigger in clean_ev or clean_ev in clean_trigger:
                    is_confirmed = True
                    break
                # Also check core keyword match
                words = [w for w in clean_trigger.split() if len(w) > 3]
                if words and all(w in clean_ev for w in words[:3]):
                    is_confirmed = True
                    break

            if not is_confirmed:
                for c in contradictions_caught:
                    clean_c = re.sub(r"[^a-z0-9 ]", "", c)
                    if clean_trigger in clean_c or clean_c in clean_trigger:
                        is_confirmed = True
                        break

            if is_confirmed:
                confirmed_list.append(f"✓ {item['confirmed']}")
            else:
                open_list.append(f"? {item['open']}")

        all_lines = confirmed_list + open_list

        width = 72
        title = "INVESTIGATION NOTEBOOK".center(width + 2)
        print("\n" + "╔" + "═" * (width + 2) + "╗")
        print("║" + title + "║")
        print("╠" + "═" * (width + 2) + "╣")
        print("║ " + " " * width + " ║")

        for line in all_lines:
            if len(line) > width:
                line = line[:width - 3] + "..."
            pad = width - len(line)
            print("║ " + line + " " * pad + " ║")

        print("║ " + " " * width + " ║")
        print("╚" + "═" * (width + 2) + "╝")
        input("\nPress Enter to return to Dashboard...")


if __name__ == "__main__":
    InvestigationNotebook.display_notebook("P0001", "case_009")
