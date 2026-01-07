class Train:
    def __init__(self,name,ticket,seats,fare):
        self.t = ticket
        self.s = seats
        self.f = fare
        self.n = name
    def getStatus(self):
        print(f"The Name of Train {self.n}")
        print(f"{len(self.s)} Seats available")
        print(f"The Fare of a ticket Rs. {self.f}")
        
    # Ticket Booking
    def bookTicket(self):
        if len(self.s) != 0:
            # passanger = int(input("How many seats do you want to book: "))
            # if passanger and passanger <= self.s:
            print(f"Your seats has been booked! And you seat no. is {self.s[0]}")
            self.s.pop(0)
            # else:
            #     print("No longer seats are available!")
        else:
            print("Seats are full!")
    # Ticket Cancellition
    def cancleTicket(self):
        # panger = int(input("How many seats do you want to cancle: "))
        SeatNo = int(input("Which seatsNo. do you want to cancle: "))
        if not SeatNo in self.s:
            self.s.append(SeatNo)
        else:
            print(f"Sorry! {SeatNo} No. seat not booked.")

Hanuman = Train("Hanuman Express 429272",5,[1,2,3,4,5],150)
Hanuman.getStatus()
Hanuman.bookTicket()
Hanuman.bookTicket()
Hanuman.bookTicket()
Hanuman.bookTicket()
Hanuman.bookTicket()
Hanuman.bookTicket()

