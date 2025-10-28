
class pen:
    def __init__(self,  tip_type, ink_color, brand, pen_type):
        self.tip_type = tip_type
        self.ink_color = ink_color
        self.brand = brand
        self.pen_type = pen_type

    def get_obj_create_code(self):
        # Generate code to create an instance of the Creator class
        temp_str = f'pen (tip_type:{self.tip_type}, ink_color:{self.ink_color}, brand:{self.brand}, pen_type:{self.pen_type} )'
        return temp_str