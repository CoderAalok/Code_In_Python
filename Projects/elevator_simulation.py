import time


class Elevator:
    def __init__(self, current_floor=0, target=0):
        self.target = target
        self.current_floor = current_floor
        self.up_awaiting = set()
        self.down_awaiting = set()
        

    def upward(self):
        for floor in range(self.current_floor, self.target + 1):
            print(f"FLOOR: {floor}")
            time.sleep(2)

            if floor in self.up_awaiting:
                print("Successfully arrived.")
                self.up_awaiting.pop()
                break
            self.current_floor += 1

        # check downward request
        if self.down_awaiting:
            self.downward()

        # move to next request
        self.main()

            
    def downward(self):
        for floor in range(self.current_floor, 0, -1):
            print(f"FLOOR: {floor}")
            time.sleep(2)
            
            if floor in self.down_awaiting:
                print("Successfully arrived.")
                self.down_awaiting.pop()
                break
            self.current_floor -= 1

        # check upward request
        if self.up_awaiting:
            self.upward()

        # move to next request
        self.main()

 
    # it job is to verify the where to move
    def main(self):

        while True:
            print("""
        ● Downward -> 0
        ● Upward -> 1
        ● Exit -> -1
            """)
            
            try:
                direction = int(input("Direction: ").strip())
  
                if direction not in {-1, 0, 1}:
                    print("Only [0], [1] or [-1]")
                    continue

                # upward
                if direction == 1:
                    self.current_floor = int(input("Current Floor: ").strip())
                    self.target = int(input("Target Floor: ").strip())
                    self.up_awaiting.add(self.target)
                    
                    if self.target > 9 or self.current_floor > 9:
                        print("Not exist.")
                        continue 
                    
                    self.upward()
                    self.up_awaiting.add(self.target)

                # downward
                elif direction == 0:
                    self.current_floor = int(input("Current Floor: ").strip())
                    self.target = int(input("Target Floor: ").strip())
                    
                    if self.target <= 0 or self.current_floor <= 0:
                        print("Not exist.")
                        continue

                    self.down_awaiting.add(self.target)
                    self.downward()
                    
                elif direction == -1:
                    return
                
            except ValueError:
                print("ERROR: Invalid input.")
            
e = Elevator()
e.main()