class Train:
    def __init__(self,name, tickets,seats,place,fare ):
        self.tickets = tickets #list
        self.seats = seats  #list
        self.place = place    #list
        self.fare = fare #int
        self.name = name #str

    #Distination chose
    def get_place(self):
            # for i in self.place:
                if self.place.lower()  in ['jaynagar' , 'janakpur','kolkata','delhi','panjab','japan']:
                    place_hold = input("From which station are you pickup the train? >>> ").lower().strip()
                    if  place_hold in  ['jaynagar' , 'janakpur','kolkata','delhi','panjab','japan']:
                        return True
                    else:
                        print("Sorry sir! Hanuman Nepal Train only goes ['Jaynagar' , 'Janakpur','kolkata','delhi','panjab','japan'] these places.")
                        return False
                else:
                    print("Sorry sir! Hanuman Nepal Train only goes ['Jaynagar' , 'Janakpur','kolkata','delhi','panjab','japan'] these places.")
                return False

    def get_name_ticket_seats_fare(self):
        net_ticket = 0
        seats_book = []
        count = 0

        try:
            while True:
                #Pre-Ticket booking
                ticket_no = int(input("How many Tickets do you need? >>> "))
                if ticket_no <=0 or ticket_no > len(self.tickets):
                    print(f"Please enter 1 to {len(self.tickets)} ")
                    continue  #Repeat the iteration until the condition  become false

                if net_ticket == 0:  #intial case
                    net_ticket += len(self.tickets) - ticket_no  #remaming tickets
                elif net_ticket >= ticket_no:  #more than one execution 
                    net_ticket -= ticket_no
                else:
                    print(f"Sorry! Only {net_ticket} ticket's are available right now.")
                    continue  #condition true move forward  and break
                break

            # available_ticket = self.tickets[:-ticket_no]  #remaning tickets
            sold_ticket = self.tickets[-ticket_no :] #sold tickets

            #Seat Booking process
            for i in range(1,(ticket_no)+1):
                while True:
                    try:
                        select = int(input(f"Ticket_{i}, Seat_No.: "))
                        if select not in self.seats:
                            print(f"Sorry sir! Seat_No. {select} is not available right now!.")
                            continue

                    except ValueError:
                        print("Typing Mistake! <Tryaging!>")
                        continue
                    if select in self.seats:
                        seats_book.append(select)
                        self.seats.remove(select)
                        count = True
                    break

            while True:
                #Ticket Cancelation process
                choice = input("Please conform this ticket for further process? Cancel: (Yes or  No): >>>    ").lower().strip()
                if choice == 'yes':
                    cancel_ticket = int(input("How many tickets do you want to cancel: >>>  "))
                    if cancel_ticket > len(sold_ticket) or  cancel_ticket <= 0:
                        print("Sorry sir! there is no any tickets no. as you mentioned. ")
                        continue
                    else:
                        cancel_ticket1 = len(sold_ticket) - cancel_ticket
                        ticket_no = cancel_ticket1
                        net_ticket = ticket_no
                        sold_ticket = sold_ticket[:-cancel_ticket]
                        for j in range(1,cancel_ticket+1):
                            while True:
                                try:
                                    cancel_1 = int(input(f"Ticket:{j}, Please enter which seat you cancel: >>>  "))
                                except ValueError:
                                    print("Typing Mistake! Please enter a valid input.")
                                    continue
                                
                                if cancel_1 not in seats_book :
                                    print("Invaild Seat no.! Please enter correct no.: >>> ")
                                    continue
                                else:
                                    seats_book.remove(cancel_1)
                                    self.seats.append(cancel_1)
                                    print(f"Cancelled! Ticket: {j} , seat: {cancel_1} ")
                                    break
                elif choice  == 'no':
                    print("Okay! your tickets and seats are confomed. ")
                else:
                    print("Default input type!")
                    continue
                break

            while True:
                #Payment process
                if count : 
                    net_amount = self.fare * ticket_no
                    payment =  (input(f"Your net amount is {net_amount}, Pay now: >>>>"))
                    if int(payment) != (net_amount) or not payment.isdigit() :
                        print("Payment is Incompleted.")
                        continue  #until execute the loop when the payment != to net_amou

                    else:
                            print("\nPayment Successful.\nNow your ticket has been Booked.")
                            print()
                else:
                    print("Seat booking process failed.")

                print("\t\t ***** Ticket Booked Details ******\n")
                print(f"\t\t Name: {(self.name).title()}\n\t\t No. of Tickets: {len(sold_ticket)}\n\t\t Ticket_No.: {sold_ticket},\n\t\t Seat_No.: {seats_book}\n\t\t Place: {(self.place)}\n\t\t Fare: {net_amount}")
                print()
                break

        except ValueError:
            print("Typing Mistake?")

print("____*Welcome To Hanuman Nepal Railway Station*____")
print()
name = input("Ticket resister by >>> ")
while True:
    place = input("Where do you want to go? >>> ").title()
    
    seats = [1,2,3]  #Available seats 
    tickets = [1,2,3] #Availale tickets

    book = Train(name,tickets,seats,place,300)

    if book.get_place():
        book.get_name_ticket_seats_fare()
    break
