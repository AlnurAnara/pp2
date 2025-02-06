class Shape:
    class Square:
        def __init__(self,length):
            super().__init__()
            self.length=length

        def area(self):
            return self.length ** 2
 
    length=Square(10)
    print ("the area of the square is:",length.area())