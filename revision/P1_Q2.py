class Customer:
    def __init__(self, customer_id, name):
        self.__customer_id = customer_id
        self.__name = name

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_name(self, name):
        self.__name = name

    def display_details(self):
        return f"===== Customer Details ===== \nCustomer ID: {self.get_customer_id()} \nCustomer Name: {self.get_name()}"

c1 = Customer("1234A", "Andrea Tan")
c2 = Customer("7895", "Lee Chit Boon")
c3 = Customer("7895B", "Lee Chit Boon")

print(c1.display_details())
print(c2.display_details())
print(c3.display_details())
