
# # Library Management System
# import time
# class Library:
    
#     def get_info(self):
        
#         print('------------Welcome to Hanuman Library-----------\n')
        
#         print("-------Authentic Books/Magazine/DVD are available-------")
    
#     def display_title(self,title):

#         print("\n>>>>• Title •<<<<")
#         print("⁃"*40)

#         for key in title.keys():
#             print(f"● {key}")
    
#         print("⁃"*40)
        
     
# # Books Review     
# class Book(Library):
    
#     # Book Title
    
#     # Book Details
#     def get_book_info(self,title,book):  #call by user

#         value = list(book[title])  #book = books(dict)
#         print("\n>>>>• HERE Book details  •<<<<")
        
#         print("\n‣ About Book:\n(Title\\Genre\\Author\\Page\\Item_ID\\ISBN\\Status)")
        
#         print('-'*40)

#         print(f"• Title: {title:>5}")  #title = key   
#         print()

#         lable1 = ["Genre","Author","Page","Item_ID","ISBN","Status"]
#         for i,v in enumerate(lable1):
#                 print(f"• {v}: {value[i]:>5}")
#                 print()
#         print('-'*40)
        

# # Updated contents like newspaper,science and research and more   
# class Magazine(Library):
    
#     # Magazine
#     def get_magazine_info(self,title,magazine):
       
#         value = list(magazine[title])
        
#         print("\n>>>>• HERE Magazine details •<<<<")
        
#         print("\n‣ About Magazine:\n(Title\\Author\\Item_ID\\Issue\\Date\\Status)")
        
#         print('-'*40)
            
#         print(f"• Title: {title:>5}")
#         print()

#         lable2 = ["Author","Item_id","Issue","Date","Status"]
#         for i,v in enumerate(lable2):
#             print(f"• {v}: {value[i]:>5}")
#             print()
#         print('-'*40)
        
# # Digital content based/ physical environment
# class DVD(Library):
#     # DVD 
#     def get_DVD_info(self,title,dvd):

#         value = list(dvd[title])
        
#         print("\n>>>>• HERE DVD details •<<<<")
        
#         print("\n‣ About DVD:\n(Title\\Author\\Item_ID\\Director\\Duration\\Status)")
        
#         print('-'*40)
        
#         print(f"• Title: {title:>5}")
#         print()

#         lable3 = ["Author","Item_ID","Director","Duration","Status"]
#         for i,v in enumerate(lable3):
#             print(f"• {v}: {value[i]:>5}")
#             print()
#         print('-'*40)
        

# # User System
# class UserSystem(Library):
#     def __init__(self,name,userID):
#         self.name = name
#         self.userID = userID
    
#     def get_login(self):
#         if (
#             not self.name.isalpha() or
#             self.name.isdigit() or
#             not self.userID.strip('!@#,.;:/$*_+-%') or 
#             not self.userID.isalnum() 
#         ):
#             return False
#         else:
#             return True
    
# class BorrowSystem(UserSystem):

#     def get_borrow(self,title,category):
        
#         if title in category:
            
#             print("Let's check....")
#             time.sleep(1.0)
#             if category[title][-1] == "Available":
                
#                 print("Yes! this item is available, So you can borrow it.")
#                 category[title][-1] = "Borrowed"
#                 return "Borrowed"
            
#             else:
#                 return "Unavailable"

#         else:
#             return None

# class CheckBorrow(BorrowSystem):

#     def display_borrow(self,borrow_li):
        
#         print("⁃⁃⁃⁃⁃⁃⁃|•| Borrowed list |•|⁃⁃⁃⁃⁃⁃⁃")

#         proof = ["UserID","Category","Title","Status"]
#         for val in proof:
#             print(f"{val:<20}",end='')
#         print()
#         print("-"*80)
        
#         for j in range(len(borrow_li)):   
#             for detail in borrow_li[j]:
#                 print(f"{detail:<20}",end='')
#             print()
        

# class Return(CheckBorrow):

#     def get_back(self,userid,borrow_li,title,category):  
#             # To confrim user
#             for rec in borrow_li:
#                 if rec[0] == userid and rec[2] == title: 
                 
#                     category[title][-1] = "Available"
#                     borrow_li.remove(rec)
#                     print(f"\n➢ {userid} borrow back!")
#                     return

#             else:
#                 print("User not found!")  
                    
        
# # Librarian's site
# print("-----Add More Items-----")
# print("Select: \n• Book\n• Magazine\n• DVD\n else skip to enter...")
# librarian = input("Your choice: ").strip().title()

# # Book Library
# books = {
#     "Harry Potter and the Sorcerer's Stone ":["Fantasy","J.K. Rowling",309,"BK001", "9780439708180","Available"] ,
#     "To Kill a Mockingbird": ["Fiction / Classic","Harper Lee",281,"BK002","9780061120084","Available"] ,          
#     "A Brief History of Time":["Science / Non-fiction","Stephen Hawking",212,"BK003","9780553380163","Available"],
#     "The Hobbit": ["Fantasy", "J.R.R. Tolkien", 310, "BK003", "9780547928227", "Unavailable"],
#     "The Great Gatsby": ["Classic", "F. Scott Fitzgerald", 180, "BK004", "9780743273565", "Available"]
# }

# # Magazine Library
# magazines = {
#     "National Geographic": ["Nathan Lump", "MG001", "Issue 215", "2025-01-15", "Available"],
#     "Time Magazine": ["Sam Jacobs", "MG002", "Issue 48", "2025-02-01", "Unavailable"],
#     "Scientific American": ["Laura Helmuth", "MG003", "Issue 327", "2025-01-01", "Available"],
#     "Forbes": ["Randall Lane", "MG004", "Issue 145", "2025-01-20", "Available"],
#     "Vogue": ["Anna Wintour", "MG005", "Issue 1210", "2025-02-10", "Available"]
# }
# # DVD Library
# dvds = {
#     "Avatar": ["James Cameron", "DV001", "James Cameron", "162 min", "Available"],
#     "Inception": ["Christopher Nolan", "DV002", "Christopher Nolan", "148 min", "Unavailable"],
#     "The Lion King": ["Disney Animation Team", "DV003", "Roger Allers & Rob Minkoff", "88 min", "Available"],
#     "Interstellar": ["Jonathan Nolan & Christopher Nolan", "DV004", "Christopher Nolan", "169 min", "Available"],
#     "Harry Potter Collection": ["J.K. Rowling", "DV005", "Various Directors", "1200 min", "Unavailable"]
# }

# if librarian in ["Book","Magazine","Dvd"]:
    
#     times = int(input(f"How many times {librarian} add: ").strip())
#     for _ in range(times):
        
#         # Common for all
#         title = input("Title: ").title().strip()
#         author = input("Author: ").title().strip()
#         status = input("Status: ").title().strip()
#         item_id = input("Item_ID: ").strip()
   
#         # For Book  
#         if librarian == "Book":
#             genre = input("Genre/Content: ").title().strip()
#             page = int(input("Page: ").strip())
#             isbn = input("ISBN: ").strip()
            
#             #appending according to key->len(books) perspective
#             books[title] = [genre,author,page,item_id,isbn,status]

#         # For Magazine   
#         elif librarian == "Magazine":  
#             issue = input("Issue Number: ").strip()
#             date = input("Date: ").strip().capitalize()
            
#             #appending according to key->len(books) perspective
#             magazines[title] = [author,item_id,issue,date,status]

#         # For DVD  
#         elif librarian == "Dvd":
#             director = input("Director: ").title().strip()
#             duration = input("Duration: ").strip()
            
#             #appending according to key->len(books) perspective
#             dvds[title] = [author,item_id,director,duration,status]

# else:
#     print("Okay!....")

# # User System
# name = input("Enter your Name: ").strip().title()
# userid = input("Enter your UserID: ").strip()
# system = Return(name,userid)

# # Library 
# system.get_info()

# result = system.get_login()

# if result:

#     print("\n::---Below these Categories---::")
#     # values
#     titleCategory = input("\n• Book\n• Magazine\n• DVD\nSearch/Select.... ").strip().lower() 
#     # keys
#     category = {
#         'book':books,
#         'magazine':magazines,
#         'dvd':dvds
#     }
    
#     if titleCategory in category: 
#         system.display_title(category[titleCategory]) 
#     else:
#         print("Out of these category!!")

# else:
#     print("Invalid input...")

# # Borrow System
# title = input("Search/Select any title....").strip().title()
# status = system.get_borrow(title,category[titleCategory])

# if status == 'Borrowed':

#     borrow_li = [[userid,titleCategory,title,status]]
#     print("Borrow sucessfully!")

#     # Check Borrow
#     system.display_borrow(borrow_li)

#     # Return 
#     system.get_back(userid,borrow_li,title,category[titleCategory])
    
# elif status == 'Unavailable':  
#     print("Currently this item is not available.")

# else:
#     print("Item is not found.")






""" 
            Library --> Book --> Magazine --> DVD 
               |
            UserSystem
                |
            BorrowSystem
                |
            CheckBorrow
                |
              Return
               

"""
