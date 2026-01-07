import random 
import string
def captcha_gen(length=6):
    alpha = string.ascii_letters + string.digits
    Captcha = ''.join(random.choices(alpha,k=length))
    return Captcha
