class Rectangle:
    def __init__(self, *args):
        if len(args) == 0:
            raise ValueError("Must supply arguments")
        # If its a square
        if len(args) == 1:
            self.width = args[0]
            self.height = args[0]
        # If its a rectangle
        elif len(args) == 2:
            self.width = args[0]
            self.height = args[1]
        else:
            raise ValueError("Too many arguments")
        
    def __str__(self):
        if type(self) == Square:
            output_string = f"Square(side={self.width})"
        else:
            output_string = f"Rectangle(width={self.width}, height={self.height})"
        
        return output_string

    def set_width(self, newWidth):
        if type(self) == Square:
            self.height = newWidth
        self.width = newWidth

    def set_height(self, newHeight):
        if type(self) == Square:
            self.width = newHeight
        self.height = newHeight

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (self.height * 2) + (self.width * 2)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        
        output_string = ""
        for i in range(self.height):
            output_string += "*" * self.width + "\n"
        
        return output_string


    def get_amount_inside(self, shape):
        w = self.width // shape.width
        h = self.height // shape.height
        return w * h

class Square(Rectangle):
    def __init__(self, *args):
        super().__init__(*args)

    def set_side(self, newSide):
        self.width = newSide
        self.height = newSide


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))