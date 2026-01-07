# Check if a given string is binary string or not - I

# strr = "010101010jkk"
# for i in strr:
#     if i in ["0",'1']:
#         print("True -> Is binary string")
#     else:
#         print("False -> Is not binary string")

    
# Check if a given string is binary string or not - II
def binary_string(strr):
    if not strr.isdigit() :
        return False
    if all(i in ['0','1'] for i in  strr ):
        return True
    else:
        return False
print(binary_string('01010101'))   
        
           
