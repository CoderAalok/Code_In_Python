import ui
import json
from pathlib import Path


class VisitLocation:
    @staticmethod
    def visit_location(player_id, case_id):
        # display location to visit
        loc = ui.LocationsUI()
        loc.visit_location_ui()

        locations = {
            1: loc.exhibition_room,
            2: loc.security_room,
            3: loc.dining_room
        }

        while True:
            try:
                location = int(input("Select location [0-3]: ").strip())

                if locations.get(location):
                    locations[location]()

                elif location == 0:
                    return

                else:
                    print("[!] Invalid option.")
                    continue

            except Exception as e:
                print(f"Error: {e}")
                continue

   