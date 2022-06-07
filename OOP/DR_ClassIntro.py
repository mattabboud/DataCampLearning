class Customer:
    # code for the class goes here
    def __init__(self, new_name=None, new_salary=None):
        self.name = new_name
        self.salary = new_salary

    def set_name(self, new_name):
        # Create an attribute by assigning a value
        self.name = new_name
        halfvalue = new_name/12

    def identify(self):
        print("I am Customer: " + str(self.name) + ". My salary is: $" + str(self.salary))

    def set_salary(self, new_salary):
        self.salary = new_salary

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self, new_raise):
        self.salary = self.salary + new_raise

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12

    pass


customer1 = Customer()
customer1.set_name("Laura")
customer1.set_salary(50000)
customer1.give_raise(1500)
customer1.identify()
print(customer1.monthly_salary())
dir(customer1)
