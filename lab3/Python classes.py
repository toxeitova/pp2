class Text():
    def __init__(self):
        self.s = ""   #переменная для хранения строки

    def getString(self):
        self.s = input("Введите строку: ")

    def printString(self):
        print(self.s.upper())

s = Text()
s.getString()
s.printString()
