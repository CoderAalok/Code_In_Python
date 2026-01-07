"""Output ->> money of given weight """
import logging

logging.basicConfig(filename="selling.log", level=logging.INFO)

def calculate_money(total_amount, given_weight):
    amount = (total_amount*given_weight)/1000
    return round(amount, 2)

def calculate_weight(total_amount, customer_amount):
    try:
        weight = (1000*customer_amount)/total_amount
        return round(weight, 2)
    except ZeroDivisionError:
        return 0

# STDIN
# Mode selection
while True:
    print("Select mode:\n 1.Calculate Money\n 2.Calculate /weight")
    seller = input().replace(" ","").strip()
    
    if seller in ["1", "2"]:
        break
    else:
        print("Enter only 1 or 2.")

modes = {
    "1":calculate_money,
    "2":calculate_weight
}

if seller == "1":
    while True:
        try:
            total_amount = int(input("Given product amount: ").replace(" ","").strip())
            given_weight = int(input("Given Weight in gram: ").replace(" ","").strip())
            
            logging.info(f"Amount: Rs. {modes[seller](total_amount, given_weight)}")
            break 
        
        except ValueError:
            print("Invalid input!")

elif seller == "2":
    while True:
        try:
            total_amount = int(input("Product amount: ").replace(" ","").strip())
            customer_amount = int(input("Customer amount: ").replace(" ","").strip())
            
            logging.info(f"Weight: {modes[seller](total_amount, customer_amount)} gm")
            break 
        
        except ValueError:
            print("Invalid input!")
