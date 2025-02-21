class Str:
    def __init__(self):
        self.str = ""

    def getString(self):
        self.string = input("Enter a string: ")
    
    def printString(self):
        print(self.string.upper())

output=Str()
output.getString()
output.printString()