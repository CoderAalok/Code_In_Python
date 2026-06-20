# Example: Single Inheritance

class UserAccount: #Base (or Parent) Class

    def loginAccount(self):
        print("Welcome to Google!")
    
    def loginUser(self,user):
        if not user or user.isdigit() or not user.isalpha():  #if user empty
            print("Username is required!")
            return False
        else:
            return True

    def loginPassword(self,password):
        if not password:  # password empty
            print("Password is required!")
            return
        elif len(password) < 8:
            return False
        else:
            return True
        
class Greet(UserAccount): #Derived (or Child) Class
    account = 'Google'
    def greet(self):
        print(f"{self.account} account successfully created...")



log = Greet()

log.loginAccount()
while True:
    username = input("Enter your Username\nUsername: ").strip()
    #Inherit(accessing) method from Base class
    checkUser = log.loginUser(username) #Return type 

    if checkUser:
        while True:
            password = input("Enter your Password\nPassword: ").strip()
            checkPass = log.loginPassword(password) #Return type 

            if checkPass:
                log.greet()
                break
            else:
                print("Please enter atleast 8 characters Password...")
        break     
    else:
        print("Please enter valid UserName...")
    