import ui

class Location:
    @staticmethod
    def visit_location():
        # display location to visit
        ui.LocationsUI().visit_location_ui()

        locations = {
            1: ui.LocationsUI().exhibition_room,
            2: ui.LocationsUI().security_room,
            3: ui.LocationsUI().dining_hall,
        }

        while True:
            try:
                location = int(input("Select locaiton [0-3]: ").strip())
                
                if locations.get(location):
                    # call location
                    locations[location]()

                elif location == 0:
                    return 
                
                else:
                    print("[!] Invalid option.")
                    continue
                
            except Exception as e:
                print(f"Error: {e}")
                continue

