class Person:
    def __init__(self, name1, address, telephone_number):
        self.name = name1
        self.address = address
        self.telephone_number = telephone_number
    def display_info(self):
        print("Name                 :",self.name)
        print("Address              :", self.address)
        print("Telephone_number     :", self.telephone_number)

class Customer(Person):
    def __init__(self, name1, address, telephone_number, customer_number, mailing_preference: bool):
        super().__init__(name1, address, telephone_number)
        self.customer_number = customer_number
        self.mailing_preference = mailing_preference
    def display_info(self):
        super().display_info()
        print("CUstomer Number      :", self.customer_number)
        print("Mailing Preference   :", self.mailing_preference)

#testing
customer_1 = Customer("Bob","1549 Address Ln" ,"314-159-2653", "58979", True)
customer_1.display_info()