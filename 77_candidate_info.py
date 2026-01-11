class Information:
    def __init__(self,
                first_name,
                *mid_name,
                last_name, 
                year,
                month,
                day,
                district,
                vdc,
                rm,
                ward_no):
        
        self._first_name = first_name
        self._mid_name = mid_name
        self._last_name = last_name
        self._year = year
        self._month = month
        self._day = day
        self._district = district
        self._vdc = vdc
        self._rm = rm
        self._ward_no = ward_no
        
        
    def get_candidate_info(self):
        import re
        pattern = re.compile(r"^[a-zA-Z]+$")
        pattern_date_birth = re.compile(r'^[0-9]+$')
        
        # Your Info 
        check = True
        
        # First name
        check_first_name = bool(pattern.match(self._first_name))
        if not check_first_name:
            print("Only valid name!")
            check = False
        
        # Mid name (optional)
        check_mid_name = bool(pattern.match(self._mid_name))
        if not check_mid_name:
            print("Only valid name!")
            check = False
            
        # Last name
        check_last_name = bool(pattern.match(self._last_name))
        if not check_last_name:
            print("Only valid name!")
            check = False
        
        # Gender 
        # option show like 
        # 1. Male
        # 2. Female 
        # 3. Other

        
        # Date of Birth (In Nepali context)
        # Days
        check_day = bool(pattern_date_birth.match(self._day))
        if not check_day:
            print("Invalid day!")
            check = False
            
        # Month
        check_month = bool(pattern_date_birth.match(self._month))
        if not check_month:
            print("Invalid month!")
            check = False
            
        # Year
        check_year = bool(pattern_date_birth.match(self._year))
        if not check_year:
            print("Invalid year!")
            check = False

        
        
        
        return check #This ensure if any mistake easily catch
    
    
first_name = input("Enter your first name: ").title()
# Mid name (optional)
mid_name = input("Enter your mid name: ").title()
last_name = input("Enter your last name: ").title()

# gender = input("Enter your gender:\n1. Male\n2. Female\n3. Other ").title()

year = input("Enter your year: ")
month = input("Enter your month: ")

day = input("Enter your day: ")

district = input()
vdc = input()
rm = input()
ward_no = input()