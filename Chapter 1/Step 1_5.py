#1.5.8

class MoneyBox:
    def __init__(self, capacity, money = 0):
        self.capacity = capacity
        self.money = money
# конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        if self.capacity-self.money >= v:
            return True
        else:
            return False
# True, если можно добавить v монет, False иначе

    def add(self, v):
        self.money += v
		
#1.5.9

class Buffer:
    def __init__(self):
        self.lst = []
# конструктор без аргументов

    def add(self, *a):
        for elem in a:
            self.lst.append(elem)
            if len(self.lst) == 5:
                print(sum(self.lst))
                self.lst = []
# добавить следующую часть последовательности

    def get_current_part(self):
        return self.lst
# вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были     
# добавлены