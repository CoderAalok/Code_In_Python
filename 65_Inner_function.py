
#             if client == '1':
#                 excersise = input("Which excersise has been you done?\n⤷ ").strip().title()
#                 set_up("Excersise.log", client_name, excersise)
            
#             elif client == '2':
#                 diet = input("Which diet has been you taken?\n⤷ ").strip().title()
#                 set_up("Diet.log", client_name, diet)
                
#             else:
#                 print("Invalid input!")
                
#     else: 
#         print("Invalid input!!")

# except KeyboardInterrupt:
#     print(f"\nOperation cancelled by user")

# finally:
#     print("DONE")


from datetime import datetime
import logging
import json
logging.basicConfig(filename="Excersise.log", level=logging.INFO, format="%(asctime)s %(message)s")
logging.basicConfig(filename="Diet.log", level=logging.INFO, format="%(asctime)s %(message)s")

def new_register(newclient, registerID):
    try:
        with open("register.json", 'r')as f:
            register_id = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        register_id = {}
    
    register_id[newclient] = registerID
    
    with open("register.json", 'w')as f:
        json.dump(register_id, f, indent=4)

def check_register_id(name, registerID):
    try:
        with open("register.json", 'r')as f:
            register_id = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        register_id = {}
    
    if register_id:
        for name, id in register_id.items():
            if register_id.get(name) == registerID or id == registerID:
                return False #this ensure that ID already registered
        return True
    else:
        return True #not registered

def client_exercise(name, excersise):    
    logging.info(f"Name: {name} -> Excersise: {excersise}")

def client_diet(name, diet):
    logging.info(f"Name: {name} -> Diet:{diet}")
    

try:
    client_unknown = (input("1. New register\n2. Add information\n⤷ ").strip())
    if client_unknown == '1':
        # For Register
        register_name = input("New register name:\n⤷").strip().title()
        
        #Check ID is already registered or not
        while True:
            register_id = input("New register ID:\n⤷ ").strip()
            if len(register_id) < 4:
                print("ID must be 4 length.")
                continue
            
            is_register = check_register_id(register_name, register_id)
            
            if not is_register:
                print("This ID already has been registered. Try another")
                continue
            
            else:
                new_register(register_name, register_id)
                print("Register successful.")
                break

    elif client_unknown == '2':
        client_name = input("Name:\n⤷ ").strip().title()
        
        found = False
        while not found:
            register_id = input("Register ID:\n⤷ ").strip()
            register = check_register_id(client_name, register_id)
            
            if register:
                print("ID is not found!") #Request for new registation/not match
                found = False
                break
            
            # ID is found/match
            else:
                found = True

        if found:
            client = (input("Select:\n1. Excersise\n2. Diet\n⤷ ").replace(" ","").strip())

            if client == '1':
                excersise = input("Which excersise has been you done?\n⤷ ").strip().title()
                client_exercise(client_name, excersise)
            
            elif client == '2':
                diet = input("Which diet has been you taken?\n⤷ ").strip().title()
                client_diet(client_name, diet)
                
            else:
                print("Invalid input!")
                
    else: 
        print("Invalid input!!")

except KeyboardInterrupt:

    print(f"\nOperation cancelled by user")

finally:
    print("DONE")