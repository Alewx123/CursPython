# Sa se scrie o clasa Fractie(numarator,numitor) care sa implementeze urmatoarele metode:
import math


class Fractie(object):
    """ O fractie este compusa din numarator si numitor """

    # - __init__ : instantiem numaratorul si numitorul
    def __init__(self, numarator, numitor):
        """" Setam valorile numarator si numitor """
        self.numarator = numarator
        self.numitor = numitor

    # - __str__ : afisam "numarator/numitor"
    def __str__(self):
        """ Returnam self ca si string """
        if self.numitor == 1:
            return f"{self.numarator}"
        else:
            return f"{self.numarator}/{self.numitor}"

    # - __add__ : returnam o noua functie care reprezinta adunarea
    def __add__(self, other):
        numarator = self.numarator * other.numitor + self.numitor * other.numarator
        numitor = self.numitor * other.numitor
        divizor = math.gcd(numarator, numitor)
        if numitor // divizor == 1:
            return numarator // divizor
        else:
            return Fractie(numarator // divizor, numitor // divizor)

    # - __sub__ : returnam o noua functie care reprezinta scaderea
    def __sub__(self, other):
        numarator = self.numarator * other.numitor - self.numitor * other.numarator
        numitor = self.numitor * other.numitor
        divizor = math.gcd(numarator, numitor)
        if numitor // divizor == 1:
            return numarator // divizor
        else:
            return Fractie(numarator // divizor, numitor // divizor)

    # inverse : returneaza o noua fractie (inversa fractiei)
    def inverse(self):
        return Fractie(self.numitor, self.numarator)


a = Fractie(1, 2)
b = Fractie(3, 2)
c = Fractie(3, 5)
d = Fractie(6, 4)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")

print()

print(f"a + b = {a.__add__(b)}")
print(f"a + c = {a.__add__(c)}")
print(f"b + c = {b.__add__(c)}")
print(f"a + d = {a.__add__(d)}")

print()

print(f"a - b = {a.__sub__(b)}")
print(f"a - c = {a.__sub__(c)}")
print(f"b - c = {b.__sub__(c)}")
print(f"a - d = {a.__sub__(d)}")

print()

print(f"inversul lui a = {a.inverse()}")
print(f"inversul lui b = {b.inverse()}")
print(f"inversul lui c = {c.inverse()}")
print(f"inversul lui d = {d.inverse()}")
