class Calculator:
    def __init__(self, n1=0, n2=0):
        self.n1 = n1
        self.n2 = n2
    
    def addition(self):
        return self.n1 + self.n2
    
    def subtraction(self):
        return self.n1 - self.n2
    
    def multiplication(self):
        return self.n1 * self.n2
    
    def divide(self):
        if self.n2 == 0:
            return "Undefined!"
        
        return self.n1 / self.n2
    
    def percentage(self):
        # self.n1 -> total number
        # self.n2 -> how many percentage
        
        return self.n1 + self.n2 / 100 * self.n1
    
    def factorial(self):
        N = self.n1
        M = self.n2
        
        if N < 0 or M < 0:
            return "Not defined!"
        
        fact1 = 1
        fact2 = 1
        
        for n in range(1, N+1):
            fact1 *= n
            
        for m in range(1, M+1):
            fact2 *= m
            
        return fact1, fact2
    

if __name__ == '__main__':
    print("(+) : Addition")
    print("(-) : Subtraction")
    print("(/) : Division")
    print("(% : Percentage (n1 -> total number and n2 = how many percentage(+ve or -ve)")
    print("(!) : Factorial\n")
    
    try:
        n1 = int(input("First number =  "))
        operator = input("Select operator: [ (+), (-), (/), (%), (!) ] =  ")
        n2 = int(input("Second number =  "))
        
        c = Calculator(n1, n2)
        func_operator = {
            '+': c.addition(),
            '-': c.subtraction(),
            '*': c.multiplication(),
            '/': c.divide(),
            '%': c.percentage(),
            '!': c.factorial()
        }
        
        if operator == '!':
            f1, f2 = c.factorial()
            print(f"{n1}{operator} = {f1}")
            print(f"{n2}{operator} = {f2}")            
        
        else: 
            print(f"{n1} {operator} {n2} = {func_operator.get(operator)}")
        
    except (ValueError or SyntaxError or NameError):
        print("Invalid input!")
        