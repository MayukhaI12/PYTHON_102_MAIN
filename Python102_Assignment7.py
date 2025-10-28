class Pen:
    def __init__(self, tip_type, ink_color, brand, pen_type):
        self.tip_type = tip_type
        self.ink_color = ink_color
        self.brand = brand
        self.pen_type = pen_type

    def __eq__(self, other):
        return (isinstance(other, Pen) and
                self.tip_type == other.tip_type and
                self.ink_color == other.ink_color and
                self.brand == other.brand and
                self.pen_type == other.pen_type)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Pen):
            raise ValueError("Comparison with non-Pen object")
        return (self.tip_type, self.ink_color, self.brand, self.pen_type) < (other.tip_type, other.ink_color, other.brand, other.pen_type)

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

# Create some Pen objects
pen1 = Pen("Ballpoint", "Blue", "Pilot", "Gel")
pen2 = Pen("Fountain", "Black", "Montblanc", "Luxury")
pen3 = Pen("Ballpoint", "Blue", "Pilot", "Gel")

# Compare Pen objects
print("pen1 == pen2:", pen1 == pen2)
print("pen1 != pen2:", pen1 != pen2)
print("pen1 == pen3:", pen1 == pen3)
print("pen1 < pen2:", pen1 < pen2)
print("pen1 > pen2:", pen1 > pen2)