
# E-Commerce
import random
class ECommerce:
    def greet(self):
        print("-"*15,"Welcome Hanuman Store","-"*15)
        print(" "*5,"Exclusive products are available in our shop"," "*5)


class SignUp(ECommerce): 
    def __init__(self,username,password):
        
        self.username = username
        self.password = password
        
    def get_login(self):
        
        login_user = {
            "Username":self.username.replace(" ","").isalnum() and 
                        len(self.username) >= 4,
                    
            "Password":len(self.password) >= 8   #allow all special character and other also
                        
        }
        invalid = []
        for key,val in login_user.items():
            if not val:
                invalid.append(key)
        
        if invalid:
            return False, f"{' and '.join(invalid)}"      
        return True, "Login Successful..."

    
    
class ProductCatalog(ECommerce):
    
    def __init__(self,books,electronics):  # verify the global value
        self.books = books
        self.electronics = electronics
        
    def display_products(self,select):

        section = {
                   1:self.books,
                   2:self.electronics
                } 
        return  section.get(select)


# After saw product
class BuyingProduct(ProductCatalog):
    
    def add_to_cart(self,item_no,item_key,item):

        if item_no not in item_key:
            return False,"Item not listed!"

        item_value = item_key[item_no]     
        if item[item_value]["Quantity"] <= 0:
            return False,"Out of stock!" 
            
        item[item_value]["Quantity"] -= 1  #qty decrease -1
        item[item_value]["Sold"] += 1  #sold increase +1
        return True,"Item added to cart" 


# Selected items details
class Customer(BuyingProduct):
    def detail_items(self,name,contact,location,address,cart,qty,amount):
        details_book = [
            ("Name",name),
            ("Contact",contact),
            ("Location",location),
            ("Address",address),
            ("Items",cart),
            ("Quantity",qty),
            ("Net amount $",amount),
            ("Delivery_agent","Unknown")
            ]
        
        print("\n","*"*15," Order Details ","*"*15)
        for key,value in details_book:
            print(f"{key}: {value}") 
        print('*'*40)    


class OrderManagement(Customer):
    def bill_details(self,name,contact,location,address,cart,qty,amount):
        super().detail_items(name,contact,location,address,cart,qty,amount)
        print("Last step confirm your order.")

    def is_confirmed(self,confirm):
        return confirm == ""
    
    def re_start(self):
        self.cart = []
        self.qty = 0
        self.amount = 0
        
    def order_confirm(self):
        
        delivery_agent = ["Maxico","Jack","Berry","Jonny","Bieber","Kaif"]
        print("✔ Successfully, your order has been confirmed ")
    
        confirm_details = [
            ("Order","Confirmed"),
            ("Delivery By",random.choice(delivery_agent)),
            ("Status Update", "Packed -> Shipped")
        ]

        print("༝"*5,"Your order in a way","༝"*5)
    
        for k,v in confirm_details:
            print(f"● {k}: {v}")
    
        print("༝"*25)
        print("Thanks for shopping.")
    


class CustomerAuthentication:
    def __init__(self,name,contact,location,address):
        self.name = name
        self.contact = contact
        self.location = location
        self.address = address
    
    def get_valid(self):
        validations = {
            "Name": self.name.replace(" ","").isalpha() and len(self.name)>=4,
            "Contact":self.contact.isdigit() and len(self.contact)==10,
            "Location":self.location.replace(" ","").isalnum() and len(self.location)>=6,
            "Address":self.address.replace(" ","").isalnum() and len(self.address)>=6
        }
        
        for detail,info in validations.items():
            if not info :
                return False, f"Invalid {detail}"

        return True,"All informations are valid."



print("────</>──── Login Page ────</>────")
username = input("Username: ").strip().title()
password = input("Password: ").strip()
print("-"*35)

books = {

    "Bhagavad Gita": {
        "Price": 20,
        "Quantity": 10,
        "Sold": 6,
        "Status": "In Stock"
    },

    "The Lord of the Rings": {
        "Price": 45,
        "Quantity": 12,
        "Sold": 6,
        "Status": "In Stock"
    },

    "Harry Potter": {
        "Price": 30,
        "Quantity": 15,
        "Sold": 8,
        "Status": "In Stock"
    },

    "The Alchemist": {
        "Price": 18,
        "Quantity": 20,
        "Sold": 10,
        "Status": "In Stock"
    },

    "Ramayana": {
        "Price": 25,
        "Quantity": 9,
        "Sold": 5,
        "Status": "In Stock"
    },

    "Mahabharata": {
        "Price": 35,
        "Quantity": 7,
        "Sold": 3,
        "Status": "In Stock"
    },

    "Atomic Habits": {
        "Price": 22,
        "Quantity": 14,
        "Sold": 9,
        "Status": "In Stock"
    },

    "Rich Dad Poor Dad": {
        "Price": 17,
        "Quantity": 11,
        "Sold": 4,
        "Status": "In Stock"
    },

    "Sapiens": {
        "Price": 28,
        "Quantity": 6,
        "Sold": 2,
        "Status": "In Stock"
    },

    "Wings of Fire": {
        "Price": 16,
        "Quantity": 13,
        "Sold": 5,
        "Status": "In Stock"
    }
}
electronics = {

    "Smartphone": {
        "Price": 300,
        "Quantity": 20,
        "Sold": 5,
        "Status": "In Stock"
    },

    "Wireless Earbuds": {
        "Price": 50,
        "Quantity": 30,
        "Sold": 10,
        "Status": "In Stock"
    },

    "Laptop": {
        "Price": 800,
        "Quantity": 12,
        "Sold": 4,
        "Status": "In Stock"
    },

    "Smart Watch": {
        "Price": 120,
        "Quantity": 18,
        "Sold": 7,
        "Status": "In Stock"
    },

    "Bluetooth Speaker": {
        "Price": 60,
        "Quantity": 25,
        "Sold": 9,
        "Status": "In Stock"
    },

    "Power Bank": {
        "Price": 25,
        "Quantity": 40,
        "Sold": 12,
        "Status": "In Stock"
    },

    "Tablet": {
        "Price": 200,
        "Quantity": 10,
        "Sold": 3,
        "Status": "In Stock"
    },

    "Gaming Mouse": {
        "Price": 35,
        "Quantity": 22,
        "Sold": 8,
        "Status": "In Stock"
    },

    "Keyboard": {
        "Price": 45,
        "Quantity": 16,
        "Sold": 6,
        "Status": "In Stock"
    },

    "LED Monitor": {
        "Price": 150,
        "Quantity": 8,
        "Sold": 2,
        "Status": "In Stock"
    }
}

signin = SignUp(username,password)
order = OrderManagement(books,electronics)


signIn,msg = signin.get_login()

# Login 

if not signIn:
    print(f"Invalid {msg}!")

else:
    print(f"{msg}")
    
    # Calling Base class(Ecommerce)
    signin.greet()
    print("✦ Product sections are:\n1. Book\n2. Electronic\n")
    
    # Shopping section
    try:
        
        customer =  int(input("Shopping any section...").strip())
        item_section = {
            1:"Books Items",
            2:"Electronic Items"
        }
    except ValueError:
        print("Invalid input! Select 1 or 2")


    # Calling Product class(Details view)
    item =  order.display_products(customer)
   
    if item:
        #Item keys are identify through number 
        item_key = {k:v for (k,v) in enumerate(item.keys(), start=1)} #key start from 1
        
        print(f"{"-"*15}{item_section[customer]}{"-"*15}")
        print('⁃'*30)
        for i,(key,value) in enumerate(item.items(),start=1):
            print(f"{i}.{key}")
            for k,v in value.items():
                print(f"{k}: {v}")
            print()
        print('⁃'*30) 
        

        customer = input("Are you interested to buying (yes/no)?").strip().lower()
        # Bill details
        cart = []
        quantity = 0
        net_amount = 0

        check = {
        "yes":True,
        "no": False
        }

        if not check.get(customer,False):
            print("Typing error!")

        while True:
            try:
                item_no = int(input("Select no. of items: ").strip())  #item_key input
                verify,msg = order.add_to_cart(item_no,item_key,item)
                
                
                if verify:  #verify stock available
                    selected_item = item_key[item_no]
                        
                    cart.append(selected_item)   #items adding into cart
                    quantity += 1
                    net_amount += item[selected_item]["Price"]  #amount increment according to specific item
                    
                    print(f"{msg}") #Add successfully
                    
                    if input("Adding more (yes/no): ").strip().lower() != 'yes':
                        break
                        
                else:
                    print(f"{msg}")
                        
                    if input("Tryagain? (yes/no)").strip().lower() != 'yes':
                        break
                
            except ValueError:
               print("Invalid input! Please enter correct items number.")
    else:
        print("Section are not available...")
        exit()

    while True:
    
        # Customer_Info/contact verification
        print("*"*5," Customer details ","*"*5)
        name = input("Name: ").strip().title()
        contact = input("Contact: ").strip()
        location = input("Location: ").strip().title()
        address = input("Address: ").strip().title()

        customer = CustomerAuthentication(name,contact,location,address)
        auth,mess = customer.get_valid()
    
        if auth:
            

            order.bill_details(name,contact,location,address,cart,quantity,net_amount)

            user_confirm = input("❝ Press➥ENTER ❞ and confirm your order\nElse your order automatically cancel!").strip()
            if order.is_confirmed(user_confirm):
                order.order_confirm()
                break
            
            else:
                print("Your order has been cancelled!")
                order.re_start()
                break
        else:
            print(f"{mess}")
            
    
    
        
 
""" 
Working Flow Structure
----------------------------------------

    User_Login
        |
    Select Product Section
        |
    One by one no. of items  select according to chosen section
        |
    User Authentication (for delivery)
        |
    View Bill details
        |
    Lastly confirm
        |
    Order Confirmed

"""