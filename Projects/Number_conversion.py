class BinaryNumberSystem:
    def __init__(self, binary: str):
        self.binary = binary
        self.bin = "01"

    
    # Check whether given input is binary
    def check_binary(self):
        for bin in self.binary:
            if bin not in self.bin:
                raise ValueError("Binary digits only 0 or 1.")
        return

    
    def binary_octal(self):
        """Conversion of Binary -> Decimal -> Octal"""

        # Check whether given input is binary
        self.check_binary()

        # Step 1: Convert Binary to Decimal
        decimal = self.binary_decimal()

        # Step 2: Convert Decimal to Octal
        octal = DecimalNumberSystem(decimal).decimal_octal()

        # reuslt
        return octal


    def binary_decimal(self):
        """Conversion of Binary to Decimal: Multiply by 2 in each binary digit"""

        # Check whether given input is binary
        self.check_binary()

        # Convert Binary to Decimal
        decimal = i = 0
        for digit in reversed(self.binary):
            decimal += int(digit) * 2 ** i
            i += 1

        # result
        return decimal
            
 
    def binary_hexadecimal(self):
        """Conversion of Binary -> Decimal -> Hexadecimal"""

        # Check whether given input is binary
        self.check_binary()

        # Step 1: Convert Binary to Decimal
        decimal = self.binary_decimal()

        # Step 2: Convert Decimal to Hexadecimal
        hexadecimal = DecimalNumberSystem(decimal).decimal_hexadecimal()

        # result
        return hexadecimal


class OctalNumberSystem:
    def __init__(self, octal: int):
        self.oct = int(octal)
    
    @staticmethod
    def check_octal(oct):
        if oct < 0:
            raise ValueError("Octal digits of a number must lies between [0-7].")
        
        x = oct
        while x != 0:
            digit = x % 10
            if digit > 7:
                raise ValueError("Octal digits of a number must lies between [0-7].")

            x //= 10

        return

 
    def octal_binary(self):
        """Octal to Binary: We can use group of 3-bits"""
        oct_bin = {
            0: "000",
            1: "001",
            2: "010",
            3: "011",
            4: "100",
            5: "101",
            6: "110",
            7: "111"
        }
        
        x = self.oct
        # check given number is octal or not
        self.check_octal(x)

        # Convert Octal to Binary
        binary = []
        while x != 0:
            digit = x % 10
            binary.append(oct_bin[digit])
            x //= 10
            
        return "".join(binary[::-1]).lstrip('0') or "0"

    
    def octal_decimal(self):
        """Octal to Decimal: Multiply by 8^i each digit of Octal"""
        
        x = self.oct
        # check given number is octal or not
        self.check_octal(x)

        # convert Octal to Decimal
        decimal = i = 0
        while x != 0:
            digit = x % 10
            decimal += digit * 8 ** i
            i += 1
            x //= 10

        return decimal

    
    def octal_hexadecimal(self):
        """Octal -> Decimal -> Hexadecimal"""
        alphabets = {
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F"
        }
        
        # check given number is octal or not
        self.check_octal(self.oct)

        # Step 1: Convert Octal to Decimal
        decimal = self.octal_decimal()

        # Step 2: Convert Decimal to Hexadecimal (Each digit multiply by 16)
        hexadecimal = []
        x = decimal
        
        while x != 0:
            remainder = x % 16
            hexadecimal.append(alphabets.get(remainder, str(remainder)))             
            x //= 16

        return "".join(hexadecimal)[::-1] or "0"


class DecimalNumberSystem:
    def __init__(self, decimal: int):
        self.decimal = int(decimal)

    @staticmethod
    def check_decimal(decimal):
        if decimal < 0:
            raise ValueError("Decimal digits of a number must lies between [0-9].")
        
        x = decimal
        while x != 0:
            digit = x % 10
            if digit > 9:
                raise ValueError("Decimal digits of a number must lies between [0-9].")
            x //= 10
            
        # result
        return

    
    def decimal_binary(self):
        """Conversion of Decimal to Binary: Divide by 2 repeatedly"""
        
        x = self.decimal
        # check whether it is decimal 
        self.check_decimal(x)

        # Convert Decimal to Binary
        binary = []
        while x != 0:
            remainder = x % 2
            binary.append(str(remainder))
            x //= 2

        # result
        return "".join(binary)[::-1].lstrip('0') or "0"


    def decimal_octal(self):
        """Conversion of Decimal to Octal: Divide by 8 repeatedly"""
        
        x = self.decimal
        # check whether it is decimal 
        self.check_decimal(x)
        
        # Convert Decimal to Octal
        octal = []
        while x != 0:
            remainder = x % 8
            octal.append(str(remainder))
            x //= 8

        # result
        return "".join(octal)[::-1] or "0"

    
    def decimal_hexadecimal(self):
        """Conversion of Decimal to Hexadecimal: Divide by 16 repeatedly"""
        alphabets = {
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F"
        }

        x = self.decimal
        # check whether it is decimal 
        self.check_decimal(x)
        
        # Convert Decimal to Hexadecimal
        hexadecimal = []
        while x != 0:
            remainder = x % 16
            hexadecimal.append(alphabets.get(remainder, str(remainder)))
            x //= 16

        # result
        return "".join(hexadecimal)[::-1] or "0"


class HexadecimalNumberSystem:
    def __init__(self, hexadecimal: str):
        self.hexa = str(hexadecimal)
        self.alphabets = {
                "A": 10,
                "B": 11,
                "C": 12,
                "D": 13,
                "E": 14,
                "F": 15
            }
        self.digits = "0123456789"

    # check whether given input is hexadecimal
    def check_hexadecimal(self, hexa):
        for i in hexa:
            if i not in self.alphabets and i not in self.digits:
                raise ValueError("Hexadecimal must lies between [0-9] and [A-F].")
        
        return
                
            
    def hexadecimal_binary(self):
        """Conversion of Hexadecimal to Binary: Grouping 4-bits"""
        hexa_bin = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111"
        }

        # check whether given input is hexadecimal
        self.check_hexadecimal(self.hexa)

        binary = []
        for i in self.hexa:
            binary.append(hexa_bin[i])

        # result
        return "".join(binary) or "0"

        
    def hexadecimal_octal(self):
        """Conversion of Hexadecimal -> Decimal -> Octal"""
        
        # check whether given input is hexadecimal
        self.check_hexadecimal(self.hexa)

        # Step 1: Convert Hexadecimal to Decimal
        decimal = self.hexadecimal_decimal()

        # Step 2:  Convert Decimal to Octal
        octal = DecimalNumberSystem(decimal).decimal_octal()
            
        # result
        return octal

    def hexadecimal_decimal(self):
        """Conversion of Hexadecimal to Decimal: Multiply each hexa by 16"""

        # check whether given input is hexadecimal
        self.check_hexadecimal(self.hexa)


        # Convert Hexadecimal to Decimal
        decimal = 0
        n = 0
        for i in reversed(self.hexa):
            if i.isalpha():
                decimal += self.alphabets.get(i) * 16 ** n
            else:
                decimal += int(i) * 16 ** n
            n += 1
            
        # reuslt
        return decimal


binary = BinaryNumberSystem('10011').binary_decimal()
print(binary)