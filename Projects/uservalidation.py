import re

def valid_user(username, password):
    pattern = re.compile(r"^[a-zA-Z0-9@#_']+$")
    
    check = True
    # check username
    if not username :
        check = False
        
    elif not pattern.match(username):
        check = False
        
    elif len(username) < 4:
        check = False
        
    # check password
    if not password:
        check = False
        
    elif len(password) < 8:
        check = False
        
    return check
