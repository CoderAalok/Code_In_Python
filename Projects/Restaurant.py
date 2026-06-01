class Restaurant:

    def __init__(self,name,type_,customer):
        self.restaurant_name = name
        self.cuisine_type = type_
        self.total_customer = customer
        self.number_served = 0

    # Information of restaurant
    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Cuisine_Type: {self.cuisine_type}")
    
    # Open restaurant
    def  open_restaurant(self):
        print(f"{self.restaurant_name} is now open.\nWelcome to our Restaurant")
    
    # Number of customer
    def set_number_served(self,num_Served):
        self.number_served = num_Served
        print(f"No. of customer the restaurant has served: {self.number_served}")
    
    # New customer increase
    def incrementCustomer(self,new_customer):
        self.number_served += new_customer
        print(f"Now number of served: {self.number_served}")
    
# Instance Attribute
restaurant = Restaurant("BIG Restaurant","Nepali and Continental",100)
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print()

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(90)

restaurant.incrementCustomer(50)
restaurant.incrementCustomer(20)