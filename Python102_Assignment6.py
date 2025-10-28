# Assignment 6
class ClassCreator:
    def __init__(self, class_name, properties):
        self.class_name = class_name
        self.properties = properties

    def get_obj_create_code(self):
        # Generate code for property initialization
        prop_init_code = "\n".join([f"        self.{prop} = {prop}" for prop in self.properties])

        # Generate the complete class code
        class_code = f"class {self.class_name}:\n" + prop_init_code + "\n"

        return class_code

# Define the properties for the Pen class
pen_properties = ["tip_type", "ink_color", "brand", "pen_type"]

# Create a ClassCreator instance for the Pen class
pen_class_creator = ClassCreator("Pen", pen_properties)

# Generate and print the code for the Pen class
pen_class_code = pen_class_creator.get_obj_create_code()
print(pen_class_code)