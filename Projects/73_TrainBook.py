class Train:
    def __init__(self, ticket, fare=200):
        self.n = "Hanuman Express 1177"
        self.t = ticket
        self.f = fare
        self.s = list(range(1, 11))
    
    def getStatus(self):
        print("=========== About Train ============")
        print(f"Name of Train {self.n}")
        print(f"{len(self.s)} Seats available")
        print(f"Fare of per ticket Rs. {self.f}\n")

    # Ticket Booking
    def bookTicket(self):
        
        if len(self.s) >= self.t:
            
            print(f"Total fare: Rs. {self.f * self.t}")
            print(f"Your seats has been booked.")
            
            seats = []
            for _ in range(self.t):
                seats.append(str(self.s[0]))
                self.s.pop(0)
                
            print(f"Seats no.: {",".join(seats)}")
        
        elif len(self.s) == 0:
            print("Seats are full!")
            
        elif self.t > len(self.s):
            print(f"Only {len(self.s)} seats are available.")
            

    # Ticket Cancellition
    def cancleTicket(self):
        SeatNo = int(input("Which seatsNo. do you want to cancle: "))
        if not SeatNo in self.s:
            self.s.insert(SeatNo-1,SeatNo)
        else:
            print(f"Sorry! {SeatNo} No. seat not booked.")

if __name__ == "__main__":
    try:
        
        ticket = int(input("How many tickets do you want?  ").strip())
        Hanuman = Train(ticket)
        Hanuman.getStatus()
        Hanuman.bookTicket()
        Hanuman.bookTicket()
        Hanuman.bookTicket()
        
        
    except ValueError:
        print("Invalid Input!!")

