class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
    def __repr__(self):
        return "Name: " + self.name + "\n" + "Animal type: " + self.animal_type + "\n" + "Age: " + self.age
    def __str__(self):
        return "Name: " + self.name + "\n" + "Animal type: " + self.animal_type + "\n" + "Age: " + self.age

    def set_name(self):
        name_variable = str(input("What is the pet's name? "))
        self.name = name_variable
    def set_animal_type(self):
        animal_type_variable = str(input("What type of animal is the pet? "))
        self.animal_type = animal_type_variable
    def set_age(self):
        age_variable = str(input("What is the pet's age? "))
        self.age = age_variable

    def get_name(self):
        print("Name:",self.name)
    def get_animal_type(self):
        print("Animal type:",  self.animal_type)
    def get_age(self):
        print("Age:", self.age)


pet1 = Pet("Bob","Titan","12")
print(pet1)