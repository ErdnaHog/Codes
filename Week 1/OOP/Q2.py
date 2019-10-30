class Customer:
    def __init__(self,customer_id,name):
        self.__customer_id = ""
        self.set_customer_id(customer_id)
        self.__name = name

    def set_customer_id(self,customer_id):
        self.__customer_id = customer_id
        self.is_id_valid()

    def set_name(self,name):
        self.__name = name

    def display_details(self):
        print("===== Customer Details =====")
        print(f"Customer ID: {self.__customer_id}")
        print(f"Customer Name: {self.__name}")

    def is_id_valid(self):
        if len(self.__customer_id) != 6:
            self.__customer_id = input("Length is incorrect! \nTry again: ")
            self.is_id_valid()
        else:
            if not(self.__customer_id[:5].isdigit() and self.__customer_id[-1].isalpha()):
                self.__customer_id = input("Format is incorrect! \nTry again: ")
                self.is_id_valid()

num_of_customers = int(input("Enter number of customers: "))

customer_list = []
for i in range(num_of_customers):
    customer = Customer(input("Enter Customer ID: "),input("Enter Customer Name: "))
    customer_list.append(customer)
for customer in customer_list:
    customer.display_details()
