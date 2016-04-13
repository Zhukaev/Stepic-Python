#1.6.8

class ExtendedStack(list):
    def sum(self):
        a = self.pop()
        b = self.pop()
        self.append(a + b)
# операция сложения

    def sub(self):
        a = self.pop()
        b = self.pop()
        self.append(a - b)
# операция вычитания

    def mul(self):
        a = self.pop()
        b = self.pop()
        self.append(a * b)
        
# операция умножения

    def div(self):
        a = self.pop()
        b = self.pop()
        self.append(a // b)
		
#1.6.9

class LoggableList (list, Loggable):
    def append(self, a):
        self.log(a)