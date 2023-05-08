# Curs 4 Clase in clase

class Animal(object):
    """ O coordonata e compusa din x si y """

    def __init__(self, age):
        """" Setam valorile x si y """
        self.years = age
        self.name = None

    def get_age(self):
        return self.years

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.years = newage

    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return f"animal: {self.name} , {self.years}"


class Cat(Animal):
    def speak(self):
        print("Miau")

    def __str__(self):
        return f"cat: {self.name} , {self.years}"

a = Animal(7)
a.set_name("Jerry")
a.set_age(3)
a.set_age(2)
print(a)


cat = Cat(5)
cat.set_name("Tom")
print(cat)
cat.speak()
