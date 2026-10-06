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


def main():

    # Number Systems
    number_systems = {
        1: BinaryNumberSystem,
        2: OctalNumberSystem,
        3: DecimalNumberSystem,
        4: HexadecimalNumberSystem
    }

    # Conversion Options
    conversion_options = {
        1: {
            1: ("Binary → Octal", "binary_octal"),
            2: ("Binary → Decimal", "binary_decimal"),
            3: ("Binary → Hexadecimal", "binary_hexadecimal")
        },

        2: {
            1: ("Octal → Binary", "octal_binary"),
            2: ("Octal → Decimal", "octal_decimal"),
            3: ("Octal → Hexadecimal", "octal_hexadecimal")
        },

        3: {
            1: ("Decimal → Binary", "decimal_binary"),
            2: ("Decimal → Octal", "decimal_octal"),
            3: ("Decimal → Hexadecimal", "decimal_hexadecimal")
        },

        4: {
            1: ("Hexadecimal → Binary", "hexadecimal_binary"),
            2: ("Hexadecimal → Octal", "hexadecimal_octal"),
            3: ("Hexadecimal → Decimal", "hexadecimal_decimal")
        }
    }

    # Menu Names
    system_names = {
        1: "BINARY",
        2: "OCTAL",
        3: "DECIMAL",
        4: "HEXADECIMAL"
    }

    while True:
        try:

            # Main Menu
            print("""
                ┌─────────────────────────────────────────────┐
                │              NUMBER SYSTEMS                 │
                ├───────┬─────────────────────────────────────┤
                │   1   │ BinaryNumberSystem                  │
                │   2   │ OctalNumberSystem                   │
                │   3   │ DecimalNumberSystem                 │
                │   4   │ HexadecimalNumberSystem             │
                │   5   │ Exit                                │
                └───────┴─────────────────────────────────────┘
            """)

            num_sys = int(input("Select number system: ").strip())

            # Exit
            if num_sys == 5:
                print("Exiting")
                break

            # Invalid number system
            if num_sys not in number_systems:
                print("Invalid number system.")
                continue

            # Conversion Menu
            while True:

                name = system_names[num_sys]
                options = conversion_options[num_sys]

                print(f"""
                    ┌─────────────────────────────────────────────┐
                    │          {name} NUMBER SYSTEMS              │
                    ├───────┬─────────────────────────────────────┤
                    │   1   │ {options[1][0]:<35} │
                    │   2   │ {options[2][0]:<35} │
                    │   3   │ {options[3][0]:<35} │
                    │   4   │ Back                                │
                    └───────┴─────────────────────────────────────┘
                """)

                conversion = int(input("Select conversion: ").strip())

                # Back
                if conversion == 4:
                    break

                # Invalid option
                if conversion not in options:
                    print("Invalid option. Only [1-4] select.")
                    continue

                # Get method name
                method_name = options[conversion][1]

                # Input number
                value = input(f"Enter {name.lower()} number: ").strip().upper()

                # Create object
                obj = number_systems[num_sys](value)

                # Get method dynamically
                method = getattr(obj, method_name)

                # Execute conversion
                result = method()

                # Conversion name
                conversion_name = options[conversion][0]
                print(f"{conversion_name}:")
                print(f"{value} -> {result}")

        except Exception as e:
            print(f"Error: {e}")


# Main Driver
if __name__ == "__main__":
    main()