import json
from datetime import datetime, timedelta, date
from time import sleep
import sys

# Like Backend
def load_file(filename, default=None):
    
    try:
        with open(filename, "r")as r:
            return json.load(r)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        default = []
        return default  #new file create

def write_file(filename, _data_):

    with open(filename, "w")as w:
        json.dump(_data_, w, indent=4)

class User:
    # user details
    filename = "Auth.json"
    @classmethod
    def new_register(cls, name, userid, password, address, contact):
        new_data = load_file(cls.filename)

        user_data = dict(
            [
                ("Name", name),
                ("UserID", userid),
                ("Password", password),
                ("Address", address),
                ("Contact", contact)
            ]
        )
        
        # checking/verifying from all data
        register_found = next(
            (data for data in new_data if data["UserID"] == user_data["UserID"]),
            None
        )
        #To confirm the user not already register
            
        # New register
        if register_found is None:
            new_data.append(user_data) 
            write_file(cls.filename, new_data)
            return True,"Successfully you've registered your account."
        
        return False,f"'{userid}' already registered. Please try another." 

    @staticmethod
    def search_book(book_search): #book-> title(name->book)/author/category
        filename = "books.json"
        books = load_file(filename)

        titles = []
        status = [] # one or may more than one books
        bookid = []
        query = book_search.lower().split()
        
        # Searching every possible word matches
        for book in books:
            
           if any(q in book["title"].lower().split() or 
                  q in book["author"].lower().split() or 
                  q in book["category"].lower().split()
                  for q in query
                ):

                titles.append(book["title"])
                status.append(book["status"])
                bookid.append(book["book_id"])

        return (titles, status, bookid)
    
    @staticmethod
    def book_Limit(userId):
        filename1 = "Borrowed.json"
        borrowed_data = load_file(filename1)
        
        user_Data = next(
            (data for data in borrowed_data if data["UserID"] == userId),
            None
        )
        
        # This ensure the user is new so eligible for borrowed
        if user_Data is None:
            return True
        
        unreturned_books = 0
        for re in user_Data["Borrowed_Data"]:
            if not re["returned"]:  #count unreturned books
                unreturned_books += 1
        
        if unreturned_books >= 3:  #not more than three
            return False
        return True
        # no changes so not needed to write file
        
    @staticmethod
    def request_order(bookid, userId):
        filename = "books.json"
        books = load_file(filename)

        book_data = next(
            (book for book in books if book["book_id"] == bookid),
            None
        )

        # Method access (Boolean gives)
        b_limit = userdata.book_Limit(userId)
        
        if not book_data is None:    
            if book_data["status"] == "AVAILABLE":
                
                return (True, b_limit)
            return (False, b_limit)

        else:
            print("BookID is not found!")
        
    @staticmethod
    def renewal_request(userId):
        filename = "Borrowed.json"
        _data = load_file(filename)
        
        user_data = next(
            (d for d in _data if d["UserID"] == userId),
            None
        )

        if user_data is None:
            print("Borrowed data is not found!")
            return
        
        # checking to find bookid 
        valid_book = False
        index_ID = 0
        while not valid_book:
            bookid = return_bookid()  # user input renewal bookid
            
            for book_info in user_data["Borrowed_Data"]:
                
                if book_info["book_id"] == bookid: # check book_id existing in borrowed data
                    
                    index_ID = user_data["Borrowed_Data"].index(book_info) #position of borrowed data
                    
                    if not book_info["returned"]: #To confirm the book is unreturned
                        valid_book = True
                    else:
                        print("Cannot renewal returned book.")
                else:
                    print("BookID is not match.")
    
        return (bookid, index_ID)
    
    @staticmethod
    def view_borrowed_book(userId, bookid):
        filename = "borrow_order.json"
        records = load_file(filename)
        
        user_data = next(
            (d for d in records if d["UserID"] == userId),
            None
        )
        # just for safe( while we know that after borrow any order then it will be executed)
        if user_data is None:
            print("User data is not found!")
            return
        
        last_order = user_data["Borrow_Order"][-1]
        
        write_file(filename, records)
        return last_order

# No issue (not needed to change)
class Book:
# Backend logic perspective Librarian ADDING/REVOMING/UPDATING logic wrote
    
    @staticmethod
    def add_book(bookid, title, author, category):
        filename = "books.json"
        book_holder = load_file(filename)
        
        add_book = dict(
            [
                ("book_id",bookid),
                ("title",title),
                ("author",author),
                ("category",category),
                ("status","AVAILABLE")
            ]
        )
        
        # Check is bookid repeated 
        if book_holder:
            if any(book["book_id"] == bookid for book in book_holder):
                print("BookID is already exist!")
                return
            
            
        for key, value in add_book.items():
            if not value:
                print(f"{key} is missing!")
                return
        
        book_holder.append(add_book)
        write_file(filename, book_holder)
        
    @staticmethod
    def remove_book(bookid):
        filename = "books.json"
        book_holder = load_file(filename)

        if not book_holder:
            print("Book file is empty!")
            return
        
        book = next((b for b in book_holder if b["book_id"] == bookid),None)
        
        if book is None:
            print("BookID is not found!")
            return

        book_holder.remove(book)
        write_file(filename, book_holder)
    
    @staticmethod
    def update_book(bookid, status):
        filename = "books.json"
        book_holder = load_file(filename)
        
        if not book_holder:
            print("Book file is empty!")
            return
        
        book = next((b for b in book_holder if b["book_id"] == bookid),None)
        
        if book is None:
            print("BookID is not found!")
            return
        
        book["status"] = status
        write_file(filename, book_holder)
        
    @staticmethod
    def update_availiablity(bookId):  #After return the book the book status update
        filename = "books.json"
        books = load_file(filename)
        
        borrowed_book = next((b for b in books if b["book_id"] == bookId),None)
        
        borrowed_book["status"] = "AVAILABLE"

        write_file(filename, books)

# result appear  well
class BorrowOrder:
    def __init__(self, total_days=5):
        self._days = total_days

    def create_borrow_order(self, userid, bookid):
        filename = "borrow_order.json"
        order_record = load_file(filename)
        
        orderid = auto_generation_orderid(order_record)
        
        borrow_date = str(date.today())
        due_date = str(date.today() + timedelta(days=self._days))
        
        # find user old record if exist in file
        userRecord = next(
            (record for record in order_record if record["UserID"] == userid),
            None
        )

        # For new user
        if userRecord is None:   
            userRecord = {
                "UserID":userid,
                "Borrow_Order":[
                    {
                        "book_id":bookid ,
                        "order_id":orderid,
                        "borrow_date":borrow_date,
                        "due_date":due_date,
                        "status":"PENDING"
                    }
                ]
            }

            # Stored in file
            order_record.append(userRecord)

        # For old user
        else:
            userRecord["Borrow_Order"].append(
                {
                    "book_id":bookid,
                    "order_id":orderid,
                    "borrow_date":borrow_date,
                    "due_date":due_date,
                    "status":"PENDING"
                }
            )

        write_file(filename, order_record)  
        return (borrow_date, due_date)
    
    # Book return with fully analysis   
    @staticmethod
    def book_returned(user_id):
        filename = "Borrowed.json"
        _data = load_file(filename)
                
        user_data = next(
            (d for d in _data if d["UserID"] == user_id),  #userid internally pass
            None
        )   

        if user_data is None:
            print("User data is not found!")
            return

        borrow_date = due_date = None
        return_book = False

        while return_book is False:       
            book_id = return_bookid()
            
            for record_dic in user_data["Borrowed_Data"]:
                
                if record_dic["book_id"] == book_id:  
                    if not record_dic["returned"]:  # To ensure unreturned book
                        
                        record_dic["returned"] = True
                        borrow_date = record_dic["borrow_date"]
                        due_date = record_dic["due_date"]
                    
                        # books status update
                        Book.update_availiablity(book_id)
                        
                        # Creating new place of 'return_date'
                        record_dic.setdefault("return_date", []).append(
                            {
                                "bookID":book_id,
                                "date":str(date.today())
                            }
                        )

                        return_book = True
                    
                    else:
                        print("Cannot re-returned the same book!")

            else:
                print("BookID is incorrect!")

        # if return_book:
        write_file(filename, _data)  #update returned and append return date
        return (book_id, borrow_date, due_date)

class RenewalOrder:
    def __init__(self, grace_day=3):
        self.grace_day = grace_day
    # Renewal request for existing user
    @staticmethod
    def create_renewal(userid, bookid): #user_data accessed from borrowed.json
        
        filename1 = "renewal_record.json"
        renewal_data = load_file(filename1)

        # After found user_data, check is user has already any renewal the book 
        data_renewal = next(
            (r for r in renewal_data if r["UserID"] == userid),
            None
        )

        #New renewal   
        if data_renewal is None:
            data_renewal = {}

            data_renewal["UserID"] = userid
            
            data_renewal["Renewal_Book"] = [
                {
                    "book_id":bookid,
                    "renewal_request":str(date.today()),
                    "status":"PENDING"     #Initially, for renewal request -> 'PENDING'
                }
            ]

            renewal_data.append(data_renewal)

        # Already exists in renewal directory
        else:
            data_renewal["Renewal_Book"].append(
                {
                    "book_id":bookid,
                    "renewal_request":str(date.today()),
                    "status":"PENDING"
                }
            )
        
        write_file(filename1, renewal_data) #data saved into renewal file but still waiting for approved
    
    def update_due_date(self, userid, index_ID):
        filename = "Borrowed.json"
        borrowed_file = load_file(filename)
        
        # borrowed_file
        user_data = next(
            (data1 for data1 in borrowed_file if data1["UserID"] == userid),
            None
        )

        # In case not found
        if user_data is None:
            print("Borrowed data is not found!")
            return
        
        # Now finding due date from borrowed file
        old_due_date = user_data["Borrowed_Data"][index_ID]["due_date"]  #due date found (as a string) (User wants to renewal that book of due date)
        
        # now convert str time into datetime
        old_due_date = datetime.strptime(old_due_date, "%Y-%m-%d").date()
        
        current_date = date.today()
        
        # Using algorithm like if user reweneal before 
        # the due date or exact on due date its fine, else subtract grace day according to (current date and due date) days 
        last_days = (current_date - old_due_date).days
        if last_days < self.grace_day:
        
            extra_day = self.grace_day - last_days
            
            # Add day into due_date
            new_due_date = str(old_due_date + timedelta(days=extra_day))
            
            # now update in borrowed file user due_date
            user_data["Borrowed_Data"][index_ID]["borrow_date"] = user_data["Borrowed_Data"][index_ID]["due_date"]
            user_data["Borrowed_Data"][index_ID]["due_date"] = new_due_date
            
            write_file(filename, borrowed_file)
            
            return True
        
        return False

class Librarian(User):

    def __init__(self, max_day=5, grace_day=3):
        self.day = max_day
        self.grace_day = grace_day

    @staticmethod
    def approve_borrow_order(userid):
        filename = "borrow_order.json"
        book_Data = "books.json"

        borrow_data = load_file(filename)
        books = load_file(book_Data)
        
        user_data = next(
            (data for data in borrow_data if data["UserID"] == userid),
            None
        )
        # For safe
        if user_data is None:
            print("UserID is not found!")
            return
        
        last_order = user_data["Borrow_Order"][-1]
        bookid = last_order["book_id"]
        
        # Find user borrowed book
        book_data = next(
            (book for book in books if book["book_id"] == bookid),
            None
        )
        # For safe
        if book_data is None:
            print("BookID is not found!")
            return
        
        # Changing borrow order status
        last_order["status"] = "CONFIRMED"
        last_order["Delivery In"] = "PROCESSING" #This will static
        # Changing book status
        book_data["status"] = "UNAVAILABLE"
        
        write_file(filename, borrow_data)
        write_file(book_Data, books)            

    def approve_renewal_order(self, userid, index_ID):
        filename = "renewal_record.json"
        renewal_file = load_file(filename)

        # renewal_File 
        # Access bookid from renewal saved data, to ensure what exact book user wants to renewal
        user_data = next(
            (data1 for data1 in renewal_file if data1["UserID"] == userid),
            None
        )

        # In case not found
        if user_data is None:
            print("Renewal file data is not found!")
            return
        
        last_order = user_data["Renewal_Book"][index_ID]
        approve = renewal_order.update_due_date(userid, index_ID)

        if approve:
            # now change status renewal data
            last_order["status"] = "APPROVED"
            print("Successfully, renewal borrowed book.")

        # If more or equal to grace day then request rejected
        else:
            last_order["status"] = "REJECTED"
            print("Renewal request rejected due to exceded to time period.")
        
        write_file(filename, renewal_file)

    def calculate_fine(self, start_date, end_date):
        start_day = datetime.strptime(start_date, "%Y-%m-%d")
        end_day = datetime.strptime(end_date, "%Y-%m-%d")
        
        return_day = (end_day - start_day).days
        
        if return_day <= self.day:
            return True, self.day #within day
        elif return_day > self.day:
            extra_day = (return_day - self.day)
            return False, extra_day #Exceeded day

class IssuedRecord: #BorrowedRecode
    @staticmethod
    def borrow_Record(user_id,book_id,borrow_date,due_date,returned):
        
        filename = "Borrowed.json"
        data = load_file(filename)
        
        # find user old record existing in file
        userRecord = next(
            (record for record in data if record["UserID"] == user_id),
            None
        )
        
        # For new user
        if userRecord is None:   
            userRecord = {
                "UserID":user_id,
                "Borrowed_Data":[
                    {
                        "book_id":book_id ,
                        "borrow_date":borrow_date,
                        "due_date":due_date,
                        "returned":returned
                    }
                ]
            }
            # Stored in file
            data.append(userRecord)
        
        # For old user
        else:
            userRecord["Borrowed_Data"].append(
                {
                    "book_id":book_id ,
                    "borrow_date":borrow_date,
                    "due_date":due_date,
                    "returned":returned
                }
            )
      
        write_file(filename, data)

# Complete 
class Fine:
    @staticmethod
    def fine_amount(userid, bookid, late_day):
        filename = "fine_record.json"
        user_data = load_file(filename)
        
        charge = 10 # per day
        total_fine = (late_day * charge)
        
        record = next(
            (data for data in user_data if data["UserID"] == userid),
            None
        )
        
        if record is None:
            # Creating new user fine History
            new_data = {
                    "UserID":userid,
                    "Fine":[
                    {
                        "bookid":bookid,
                        "total_amount":total_fine,
                        "late_day":late_day,
                        "Payment":0
                    }
                ]
            }
            # stored fine data in file
            user_data.append(new_data)
        
        else:
            data["Fine"].append(
                {
                "bookid":bookid,
                "total_amount":total_fine,
                "late_day":late_day,
                "Payment":0
                }
            )
           
        write_file(filename, user_data)
        return total_fine
    
    @staticmethod
    def fine_pay(userid, amount, total_amount):
        filename = "fine_record.json"
        fine = load_file(filename)
        
        if not fine:
            print("Fine record is empty!")
            return
        
        user_data = next((record for record in fine if record["UserID"] == userid),None)
        
        if user_data is None:
            print("UserID is not found!")
            return
        
        latest_payment = user_data["Fine"][-1]
        already_paid = latest_payment.get("Payment",0)
        
        if (already_paid + amount) > total_amount:
            
            refund = (already_paid + amount) - total_amount
            latest_payment["Payment"] = total_amount
            write_file(filename, fine)
                        
            print("Payment successful.")
            print(f"Get back your money Rs. {refund}, due to exceed total amount.")
            return True
        
        
        latest_payment["Payment"] = (already_paid + amount)
        write_file(filename, fine)
        
        if latest_payment["Payment"] == total_amount:
            print("Payment sucessful.")            
            return True
        
        print(f"Remaining fine Rs. {total_amount - latest_payment['Payment']}.")
        return False

# Just in this function call entire function gives an output
def borrow_book_flow(userid):
    while True:
        print("\nNOTE: Make sure every possible word matches books are shows.\n")
        book_search = input("Search any books (title/author/category): ").replace("  ","").strip().lower()
        
        # restriction: Invalid input or Search out of content or Books not found in a catalog
        title, status, bookid = userdata.search_book(book_search)
        
        if title:
            break  #Exit from loop  for further process
        else:
            print("Oops! book is not found.")
            continue

    i = 1
    book_li = {} #storing titile representing by number
    for t, s in zip(title, status):
        book_li[i] = t
        print(f"⇨ {i}. {t} ({s})")
        i += 1
    
    title_id = {} #storing title as key and bookid as value
    for t, b_id in zip(title, bookid):
        title_id[t] = b_id
    
    while True:
        try:
            
            user = input("Do you want to borrowing (yes/no)? ").strip().lower()
            # Except 'yes' enter any thing then exit from loop
            if user == "no" :
                print("See you text time...")
                sys.exit(0)
            elif user != "yes":
                print("Only enter (yes/no).")
                continue
            
            order = int(input("Which one of the book do you wants to borrow?\nPlease enter that number: ").strip())
            
            if order not in book_li:
                print(f"Only enter {list(book_li.keys())}.")
                continue
            
            t = book_li[order] #take title(t)
            bookId = title_id[t] #bookid found
            break
        
        except ValueError as e:
            print(f"Invalid {e}")
            sys.exit(0)

    try:
        # When request true that is ( book is not borrowed then move forward )
        user_request, user_eligiblity = userdata.request_order(bookId, userid)
        if user_request:

            if user_eligiblity:
                
                borrow_date, due_date = bookborrow.create_borrow_order(userid, bookId)

                userdata.approve_borrow_order(userid)
                
                borrowed.borrow_Record(userid, bookId, borrow_date, due_date, False)
                
                print("Successfully! Your order has been confirmed.\n")
                
                user_data = User.view_borrowed_book(userid, bookId)
                print(f"-------Below your borrowing details:--------\n")
                for order, value in user_data.items():
                    print(f"{order} : {value}")
        
                return True #More borrow

            else:
                print("Your borrowing limit exceeded so, Immediatly return atleast one.")
                return_book(userid)
                return True
            
        else:
            print("This book is already borrowed by someone.")
            return True # Get one more chance to borrow another book

    except (NameError) as e:
        print(f"Runtime error: {e}")

def auto_generation_orderid(order_record):
    try:
        
        key_id = []
        if order_record:
            for record in order_record:
                for i in range(len(record.get("Borrow_Order", []))):
                    key_id.append(int(record["Borrow_Order"][i]["order_id"][3:]))
                    
            max_id = max(key_id)
            max_id += 1
            
            return f"UoB{max_id}"
        
        return f"UoB100"
    
    except (KeyError) as e:
        print(e)

def return_bookid():
    specialChar = "!@#$%^&*()_+-=:;|<>,.?/`~'"
    while True:
        book_id = input("BookID: ").replace(" ","").strip()
        if not book_id:
            print("BookID is empty.")
            continue
        elif any(s in book_id for s in specialChar):
            print("BookID should not contains special character.")
            continue
        elif len(book_id) < 5:
            print("Length of BookID must be 5.")
            continue
        break
    return book_id

# Find Unique userid 
def userid_authorize():
    filename = "Auth.json"
    data = load_file(filename)
    

    while True:
        user_id = input("UserID: ").replace("  ","").strip().lower()
        
        is_unique = not any(d.get("UserID") == user_id for d in data)

        if is_unique:
            print("Successfully registered.")
            return user_id
        
        else:
            print("UserID is already registered.")

#  Verifying user authentication ( After registered user login only)
def check_authorization():
    filename = "Auth.json"
    user_data = load_file(filename)
    
    # Ensure does the file exist or not
    if not user_data:
        print("File does not exist.")
        return False

    try:
        while True:
            user_id = input("UserID: ").replace("  ","").strip().lower()
            
            userData = next(
                (d for d in user_data if d.get("UserID",False) == user_id),
                None
            )
            
            if userData is None:
                print("UserID is incorrect!")
                continue
            break

# After userid correct 
        max_attempt = 3
        attempt = 0
        
        while attempt != max_attempt:
            _password = input("Password: ").replace("  ","").strip()
            
            if userData["Password"] == _password:
                print("Successfully login...")
                return user_id #True
            
            else:
                print("Password is incorrect!")
                print(f"Only {2-attempt} attempt left. ")
                attempt += 1
                continue
            
        print("Login temporarily disabled.")
        return False

    except (KeyError) as e:
        print(e)

# No issue (not needed to change)
def late_payment(days, uid, bookid):
    print(f"You are {days} days late, so you must pay a fine.")
    # call fine class
    total_amount = Fine.fine_amount(uid, bookid, days)
    print(f"Pay Rs. {total_amount}\n")
    
    while True:
        try:

            amount = int(input("Enter an amount: ").strip())
            payment = Fine.fine_pay(uid, amount, total_amount)
            
            if payment:
                print("Thank you for payment.")
                break
            
            elif amount <= 0:
                print("Invalid amount!")
                continue
            
            else:
                print("Don't delay for payment.")
                break

        except ValueError as e:
            print(f"Invalid input: {e}")

def return_book(uid):
    try:
            
        bookid, borrow_date, due_date = bookborrow.book_returned(uid)
        date_verify, days = userdata.calculate_fine(borrow_date, due_date)

        if date_verify: # This ensure book returned at the time
            print(f"You returned the borrowed book within {days} days.")
            print("Thank you for returning the borrowed book.")
            return
        
        else:
            late_payment(days, uid, bookid)
            
    except (ArithmeticError, ValueError, TypeError) as e:
            print(e)
            
def renewal_book(unreturned_books, uid):
    
    if unreturned_books == 0:
        return
    try:
        if  unreturned_books >= 3:
            return_book(uid) 
            return 
        
        print("WARNING: Before borrowing a new book, you must return atleast one book.")
    
        bookid, indexId = userdata.renewal_request(uid)
        renewal_order.create_renewal(uid, bookid)
        
        print("Wait a moment...")
        sleep(1.5)
        
        userdata.approve_renewal_order(uid, indexId)
        print("Renewal successful.")

    except (ArithmeticError, ValueError, TypeError) as e:
        print(e)


userdata = Librarian()
bookborrow = BorrowOrder()
renewal_order = RenewalOrder()
borrowed = IssuedRecord()


# Testing for Librarian input
print("What do you want to do?")
while True:
    try:
        librarian = int(input("\n1.Add Book\n2.Remove Book\n3.Update Book\n4.Exit : ").strip())
        
        if librarian not in [1,2,3,4]:
            print("Enter only either (1), (2), (3) or (4).")
            continue
        break
        
    except ValueError as e:
        print(f"Invalid input: {e}")
        
if librarian == 1:
    print("NOTE: You should gives (book_id, title, author, category)")
    bookid = return_bookid()
    informs = []
    
    name_required = ["Title", "Author Name", "Category"]
    for name in name_required:
        while True:
            info = input(f"{name}: ").replace("  ","").strip().title()
            if not info:
                print(f"{name} is required!")
                continue
            elif any(s in info for s in "!@#$%^&*_+-=:;|<>,.?/`~'"):
                print(f"{name} contains special character!")
                continue
            elif len(info) < 5:
                print(f"{name} length too small!")
                continue
            break
        informs.append(info)
    
    title, author, category = informs
    Book.add_book(bookid, title, author, category)
    
elif librarian == 2:
    print("You should only gives BookID")
    bookid = return_bookid()
    Book.remove_book(bookid)
    
elif librarian == 3:
    print("You should gives BookID and Status")
    bookid = return_bookid()
    while True:
        status = input("Status: AVAILABLE or UNAVAILABLE").replace("  ","").strip().upper()
        if not status:
            print("Status is required!")
            continue
        elif status not in ["AVAILABLE", "UNAVAILABLE"]:
            print("Input only AVAILABLE or UNAVAILABLE")
            continue
        break
    Book.update_book(bookid, status)

else:
    print("!DONE!")

# Register/Login(Only required -> userid)
try:
    logged_in = False
    special_char = "|!@#$%^&*)(}{_+-=:;<>,.?/`~'"

    while True:
        user = input("1.Register\n2.Login: ").strip()
        if user == "1":
            while True:
                user_name = input("Name: ").replace(" ","").strip().title()
                if not user_name:
                    print("Name is required.")
                    continue
                elif not user_name.isalpha():
                    print("Name should contain only characters.")
                    continue
                elif len(user_name) < 4:
                    print("Length must greater than 4.")
                    continue
                break
            
            while True:
                userID = input("UserID: ").replace(" ","").strip().lower()
                if not userID :
                    print("UserID must be required.")
                    continue
                elif not any(s in userID for s in special_char):
                    print("Atleast one special character.")
                    continue
                elif len(userID) < 4:
                    print("Length must greater than 4.")
                    continue
                break
           
            while True:
                password = input("Password: ").replace("  ","").strip()
                if not password:
                    print("Password must be required.")
                    continue
                elif len(password) < 8:
                    print("Password atleast 8 characters.")
                    continue
                elif not any(p in password for p in "0123456789"):
                    print("Atleast one number.")
                    continue
                elif not any(s in password for s in special_char):
                    print("Atleast one special character.")
                    continue
                break
            
            while True:
                address = input("Address: ").replace("  ","").strip().title()
                if not address:
                    print("Address must be required.")
                    continue
                elif any(s in address for s in special_char):
                    print("Invalid address.")
                    continue
                elif len(address) < 5:
                    print("Length must greater than 5.")
                    continue
                break
            
            while True:
                contact_number = input("Contact Number: ").replace(" ","").strip()
                if not contact_number:
                    print("Contact number must be required.")
                    continue
                elif not contact_number.isdigit():
                    print("Invalid input!.")
                    continue
                elif len(contact_number) != 10:
                    print("Invalid number!")
                    continue
                break

            is_register,msg = userdata.new_register(user_name, userID, password, address, contact_number)
            if is_register: #userid distict 
                print(msg)
                print("\nLogin your account.")
                logged_in = check_authorization()  # check_authorization() ->> boolean and userid
                    
            else: #userid same
                print(msg)
                userId = userid_authorize()
                userdata.new_register(user_name, userId, password, address, contact_number)
                
                print("\nLogin your account.")
                logged_in = check_authorization()
                
    
        elif user == "2":
            print("\nLogin your account.")
            logged_in = check_authorization()

        else:
            print("Select 1 or 2.")
            continue
        break
        
except (NameError, TypeError, KeyError) as e:
    print(e)

if logged_in:
    uID = logged_in

    # To ensure the old user borrowed any books only
    filename = "Borrowed.json"
    borrowed_record = load_file(filename)
          
    call_func = {
        "1":return_book,
        "2":renewal_book,
        "3":borrow_book_flow
    }
    
    unreturned_books = 0
    for data in borrowed_record:
        if data["UserID"] == uID:
            for rec in data.get("Borrowed_Data", []):
                if not rec.get("returned", True):  #rec["returned"] = bool
                    unreturned_books += 1 #Count unreturned books
            break        

    # Execute only when user borrowed but must (unreturned)
    if unreturned_books:
        while True:
            print("Do you want to do this with your borrowed book?")
            user_try = input("\n1] Return\n2] Renewal\n3] Later to do that : ").strip()

            if user_try in call_func:
                if user_try == "3":
                    call_func[user_try](uID)
                    break
                elif user_try == '2':
                    call_func[user_try](unreturned_books, uID)
                    break
                else:
                    call_func[user_try](uID)
                    break
                
            else:
                print("Enter only either (1), (2) or (3).")

        print("Now choice is your either quit or borrowing again.")
        while True:
            user_quit = input("'Quit' → 'q'\n'Borrowing' → 'b': ").strip().lower()
            if user_quit == "q":
                sys.exit(0)
            elif user_quit == "b":
                break  #Exit from this loop and enter into __main__ condition
            else:
                print("Invalid input!")
                continue            

    if __name__ == "__main__":
        get_chance = borrow_book_flow(uID)
        if get_chance:
            while True:
                user = input("Do you want to borrow another book (yes/no)?").strip().lower()
                
                choice = {
                    "yes":True,
                    "no":False
                }
                if choice.get(user):
                    borrow_book_flow(uID)
                    continue

                print("See you later...")
                break
                
