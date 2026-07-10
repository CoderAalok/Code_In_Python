VALID_PLACES = ["jaynagar", "janakpur", "kolkata", "delhi", "panjab", "japan"]


def format_places():
    return ", ".join(place.title() for place in VALID_PLACES)


def ask_number(prompt, minimum=1, maximum=None):
    while True:
        value = input(prompt).strip()

        if not value.isdigit():
            print("Typing mistake! Please enter a number.")
            continue

        number = int(value)
        if number < minimum:
            print(f"Please enter {minimum} or more.")
            continue

        if maximum is not None and number > maximum:
            print(f"Please enter {minimum} to {maximum}.")
            continue

        return number


class Train:
    def __init__(self, name, tickets, seats, place, fare):
        self.tickets = tickets
        self.seats = seats
        self.place = place
        self.fare = fare
        self.name = name
        self.pickup = ""
        self.net_amount = 0

    def get_place(self):
        destination = self.place.lower().strip()

        if destination not in VALID_PLACES:
            print(f"Sorry sir! Hanuman Nepal Train only goes to {format_places()}.")
            return False

        while True:
            pickup = input("From which station are you picking up the train? >>> ").lower().strip()

            if pickup not in VALID_PLACES:
                print(f"Sorry sir! Hanuman Nepal Train only goes to {format_places()}.")
                continue

            if pickup == destination:
                print("Pickup station and destination cannot be the same.")
                continue

            self.place = destination.title()
            self.pickup = pickup.title()
            return True

    def get_name_ticket_seats_fare(self):
        available_count = min(len(self.tickets), len(self.seats))
        ticket_count = ask_number(
            "How many Tickets do you need? >>> ",
            minimum=1,
            maximum=available_count,
        )

        sold_tickets = self.tickets[:ticket_count]
        del self.tickets[:ticket_count]

        booked_seats = []
        for ticket_index in range(1, ticket_count + 1):
            while True:
                selected_seat = ask_number(f"Ticket_{ticket_index}, Seat_No.: ")

                if selected_seat not in self.seats:
                    print(f"Sorry sir! Seat_No. {selected_seat} is not available right now!")
                    continue

                booked_seats.append(selected_seat)
                self.seats.remove(selected_seat)
                break

        while True:
            choice = input("Do you want to cancel any selected ticket? (yes/no): >>> ").lower().strip()

            if choice in ("yes", "no"):
                break

            print("Default input type! Please enter yes or no.")

        if choice == "yes":
            cancel_count = ask_number(
                "How many tickets do you want to cancel: >>> ",
                minimum=1,
                maximum=len(sold_tickets),
            )

            for cancel_index in range(1, cancel_count + 1):
                while True:
                    cancel_seat = ask_number(
                        f"Ticket:{cancel_index}, Please enter which seat you want to cancel: >>> "
                    )

                    if cancel_seat not in booked_seats:
                        print("Invalid seat no.! Please enter a booked seat number.")
                        continue

                    seat_index = booked_seats.index(cancel_seat)
                    cancelled_ticket = sold_tickets.pop(seat_index)
                    booked_seats.pop(seat_index)

                    self.tickets.append(cancelled_ticket)
                    self.seats.append(cancel_seat)
                    self.tickets.sort()
                    self.seats.sort()

                    print(f"Cancelled! Ticket: {cancelled_ticket}, seat: {cancel_seat}")
                    break

        if not sold_tickets:
            print("All tickets were cancelled. No payment is required.")
            return

        self.net_amount = self.fare * len(sold_tickets)
        while True:
            payment = input(f"Your net amount is {self.net_amount}, Pay now: >>> ").strip()

            if not payment.isdigit():
                print("Payment is incomplete. Please enter numbers only.")
                continue

            if int(payment) != self.net_amount:
                print("Payment is incomplete.")
                continue

            print("\nPayment Successful.\nNow your ticket has been booked.\n")
            break

        print("\t\t ***** Ticket Booked Details ******\n")
        print(f"Name: {self.name.title()}\n")
        print(f"No. of Tickets: {len(sold_tickets)}\n")
        print(f"Ticket_No.: {sold_tickets}\n")
        print(f"Seat_No.: {booked_seats}\n")
        print(f"Pickup: {self.pickup}\n")
        print(f"Place: {self.place}\n")
        print(f"Fare: {self.net_amount}")
        print()


def main():
    print("____*Welcome To Hanuman Nepal Railway Station*____")
    print()

    while True:
        name = input("Ticket registered by >>> ").strip()
        if name:
            break
        print("Name cannot be empty.")

    while True:
        place = input("Where do you want to go? >>> ").strip()
        seats = [1, 2, 3]
        tickets = [1, 2, 3]

        book = Train(name, tickets, seats, place, 300)
        if book.get_place():
            book.get_name_ticket_seats_fare()
            break


if __name__ == "__main__":
    main()
