import json
from pathlib import Path
class DetectiveSystem:
    # load player details/record
    def load_records(self, file):
        try:
            with open(file, 'r') as fr:
                return json.load(fr)
        except (FileNotFoundError ,  json.decoder.JSONDecodeError):
            return {}

    # create new record file
    @staticmethod
    def create_new(data, file):
        try:
            Path(file).parent.mkdir(parents=True, exist_ok=True)
            with open(file, 'w', encoding='utf-8') as fw:
                json.dump(data, fw, indent=4, ensure_ascii=False)
            return True
        
        except Exception as e:
            print(f"[!] Could not save file: {e}")
            return False
        
    # player details save
    def save_record(self, data, file):
        with open(file, 'w') as fw:
            json.dump(data, fw, indent=4) 
        return


    # fetch player active case record
    @staticmethod
    def _get_record(inv_data, player_id, case_id):
        return next(
            (rec for rec in inv_data.get(player_id, []) if rec["Case"] == case_id),
            None
        )


    # fetch player record from player_record.json
    @staticmethod
    def _player_record(records, player_id):
        return records.get(player_id)

    # ------------- FIND RANK ---------------
    @staticmethod
    def get_rank(xp: int):
        if xp >= 3500:
            return "Master Detective"
        elif xp >= 2000:
            return "Lead Detective"
        elif xp >= 1000:
            return "Senior Investigator"
        elif xp >= 500:
            return "Investigator"
        else:
            return "Rookie"


    # Calculate rating (Based on Score)
    @staticmethod
    def get_rating(score: int):
        if score >= 900:
            return "★★★★★"
        elif score >= 750:
            return "★★★★☆"
        elif score >= 550:
            return "★★★☆☆"
        elif score >= 350:
            return "★★☆☆☆"
        else:
            return "★☆☆☆☆"


    # ------------------ CALCULATE PROGRESS ------------------------
    @staticmethod
    def progress_bar(curr_progress: int, width=10):
        # curr_progress between 0 and 100
        progress = max(0, min(100, curr_progress))
        
        # filled bar
        filled = int((progress / 100 ) * width)
        # empty bar
        empty = width - filled
        
        prog_bar = "█" * filled  + "░" * empty
        return f"{prog_bar} {progress:.1f}%"


    # ------------- CALCULATE XP (BASED ON SCORE) ----------------
    @staticmethod
    def xp_bar(score: int, rank: str, width=10):
        if score < 0:
            print("Score can't be negative.")
            return
        
        rank_map = {
            "Rookie": 499, # 0-499
            "Investigator": 500,  # total Investigator rank >= 500
            "Senior Investigator": 1000, # >= 1000
            "Lead Detective": 2000,  # >= 2000
            "Master Detective": 3500,  # >= 3500
            
        }
        
        if not rank_map.get(rank):
            print("Rank not found!")
            return 

        total_rank = rank_map[rank]
        x_score = max(0, min(total_rank, score))
        
        # number of filled bar use
        filled = int((10 * x_score) / total_rank)
        # empty bar
        empty = width - filled

        xp_bar = "█" * filled  + "░" * empty
        return f"{xp_bar} {x_score} / {total_rank}"

