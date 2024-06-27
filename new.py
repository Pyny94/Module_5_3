class HOUSE:
    def __init__(self, name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def to_go(self,new_floor):
        self.new_floor = new_floor
        if 1 > new_floor or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor+1):
                print(i)

    def __eq__(self,other):
         return self.number_of_floors == other.number_of_floors

    def __lt__(self,other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self,other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self,other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self,other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self,other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self



h1 = HOUSE('ЖК Эльбрус', 10)
h2 = HOUSE('ЖК Акация', 20)

print(f"Название: {h1.name}, кол-во этажей: {h1.number_of_floors}")
print(f"Название: {h2.name}, кол-во этажей: {h2.number_of_floors}")

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(f"Название: {h1.name}, кол-во этажей: {h1.number_of_floors}")
print(h1 == h2)

h1 += 10 # __iadd__
print(f"Название: {h1.name}, кол-во этажей: {h1.number_of_floors}")

h2 = 10 + h2 # __radd__
print(f"Название: {h2.name}, кол-во этажей: {h2.number_of_floors}")

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__