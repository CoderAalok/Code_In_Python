
import json
import sys
from datetime import datetime

def get_datetime():
    current_datetime = datetime.now()
    return current_datetime

def client_excersise(date, name, excersise):
    with open(f"{name}_excersise.txt", 'a+')as f:
        f.write(f"[{date}] Name: {name} -> Excersise: {excersise}\n")

def client_diet(date, name, diet):
    with open(f"{name}_diet.txt", 'a+')as f:
        f.write(f"[{date}] Name: {name} -> Excersise: {diet}\n")

def get_info(type, clients, select_client):
    name = clients.get(select_client)
    filename = f"{name}_{type}.txt"

    try:
        with open(filename, 'r')as f:
            lines = f.readlines()
            if lines:
                for line in lines:
                    print(line)
            else:
                print("No any client properties are found.")

    except FileNotFoundError:
        print("File does not exit.") 
    
def stored_clients_name(client_name):
    try:
        with open("clients.json", 'r')as f:
            clients = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        clients = {}
        
    # For new client
    if not clients:
        clients["1"] = client_name
        with open("clients.json", 'w')as f:
            json.dump(clients, f, indent=4)
    
    else:
        found = False
        for name in clients.values():
            if name == client_name:
                found = True
                break
            
        if not found:
            n = int(list(clients.keys())[-1])
            clients[n+1] = client_name
            with open("clients.json", 'w')as f:
                json.dump(clients, f, indent=4)
        else:
            return

# Manager -> To retrieve client activities
selected = {
            '1':"Retrieve info",
            '2': "Skip"
        }

type = None

while type is None:
    manager = input("Press:\n1. Retrieve info\n2. Skip\n⤷ ").strip()
    if selected.get(manager):
        type = manager
    else:
        print("Enter only 1 or 2.")

if type == '1':

    try:
        with open("clients.json", 'r')as f:
            clients = json.load(f)
            
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        clients = {}

    if clients:
        print("Below existing client:")
        for i,v in clients.items():
            print(f"{i}: {v}")  #show all existing clients name

        while True:
            select_client = input("Which client info retrieve?\nSelect number:\n⤷ ").strip()

            # check selected number client exist or not
            if clients.get(select_client):
                types = input("For which type\n1. Excersise\n2. Diet\n⤷ ").strip()

                management = {
                                "1":"excersise",
                                "2":"diet"
                            }

                if management.get(types):
                    type_name = management.get(types)
                    get_info(type_name, clients, select_client)
                    sys.exit(0) #Exit
                
                else:
                    print("Enter only 1 or 2.")

            else:
                print(f"Only these {list(clients.keys())} clients exist.")   
    else:
        print("Client is not found.")
        sys.exit(0) #Exit

# Client gives -> What they done?
client_name = input("Client Name:\n⤷  ").strip().title()

management = {
        "1":"Excersise",
        "2":"Diet"
    }

select = None

while select is None:
    
    physical = input("What do you wants to lock?\nPress:\n1. Excersise\n2. Diet\n⤷ ").strip()
    
    if management.get(physical):
        select = physical
    else:
        print("Enter only 1 or 2.")

if select == '1':
    
    while True:
        excersise = input("Which excersise has been you done?\n⤷ ").strip().title()
        if not excersise:
            print("Excersise is blank?")
            continue
        
        else:
            stored_clients_name(client_name)
            date = get_datetime()
            client_excersise(date, client_name, excersise)
            break

else:
    
    while True:
        diet = input("Which diet has been you ate?\n⤷ ").strip().title()
        if not diet:
            print("Diet is blank?")
            continue
        
        else:
            stored_clients_name(client_name)
            date = get_datetime()
            client_diet(date, client_name, diet)
            break 