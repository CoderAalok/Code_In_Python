
from datetime import datetime
from dateutil.relativedelta import relativedelta

def english_date(en_birth_date): #output: age
    current_date = (datetime.today()).date()
    age = current_date.year - en_birth_date.year
    
    if (current_date.month, current_date.day) < (en_birth_date.month, en_birth_date.day):
        age -= 1

    return age

def nepali_date(np_birth_date):  #output: age 
    # This gives current Nepali date  (Exclude leap date-> y, m, d)
    date = (datetime.today()).date()
    y = date.year
    m = date.month
    d = date.day

    # Nepali current date
    Nepali_date_format = datetime(y, m, d)
    current_date =  (Nepali_date_format + relativedelta(years=56, month=9, days=32)).date()  

    age = current_date.year - np_birth_date.year
    
    if (current_date.month, current_date.day) < (np_birth_date.month, np_birth_date.day):
        age -= 1
    
    return age

def age_date_calculate(age):  #output: english and nepali date
    en_current_date = (datetime.today()).date()
    # Exact year give but not month and day
    en_date = en_current_date - relativedelta(years=age)
    
    
    date = (datetime.today()).date()
    y = date.year
    m = date.month
    d = date.day

    # Nepali current date
    Nepali_date_format = datetime(y, m, d)
    np_current_date =  (Nepali_date_format + relativedelta(years=56, month=9, days=32)).date()  

    np_date = np_current_date - relativedelta(years=age)
    
    return (en_date, np_date)


user = input("Select (1) or (2):\n1. Date of Birth\n2. Age\n⤷ ")

calculates = {
    "1": english_date,
    "2": nepali_date
}
try:
    if user == '1':
        age = input("Enter your age\n⤷ ")
        en_date, np_date = age_date_calculate(int(age))
        print(f"Your Birthday Date in\nEnglish Date: {en_date} and\nNepali Date: {np_date}")

    elif user == '2':
        date_type = input("Select (1) or (2):\n1. English Date\n2. Nepali Date\n⤷ ")
        if calculates.get(date_type):
            year = input("Enter your birth year\n⤷ ")
            month = input("Enter your birth month\n⤷ ")
            day = input("Enter your birth day\n⤷ ")
            age = None
            
            if date_type == '1':
                # English Birth date
                E_date_format = f"{year}-{month}-{day}"
                E_date = (datetime.strptime(E_date_format, "%Y-%m-%d")).date()
                check_age = calculates.get(date_type)
                if check_age:
                    age = check_age(E_date)
            else:
                # Nepali Birth date
                N_date_format = f"{year}-{month}-{day}"
                N_date = (datetime.strptime(N_date_format, "%Y-%m-%d")).date()
                check_age = calculates.get(date_type)
                if check_age:
                    age = check_age(N_date)

            print(f"Your age: {age}")

except Exception as e:
    print(f"Error: {e}")