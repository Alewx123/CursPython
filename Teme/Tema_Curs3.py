# Sa se scrie o functie care primeste un numar nedefinit de parametrii si sa se calculeze suma parametrilor care
# reprezinta numere intregi sau reale

# def your_funtion(*args, **kwargs):
#     suma = 0
#     for s in args:
#         if isinstance(s, int) or isinstance(s, float):
#             suma = suma + s
#
#     return suma
#
#
# print(your_funtion(1, 5, -3, 'abc', [12, 56, 'cad']))
#
# print(your_funtion())
#
# print(your_funtion(2, 4, 'abc', param_1=2))

# Sa se scrie of functie recursiva care primeste ca parametru o lista cu numere intregi si returneaza:
# - suma totala a numerelor (Eu am facut suma sumelor numerelor pare si impare)
# - suma numerelor pare
# - suma numerelor impare


# def suma_lista(lista, i=0):
#     if i == len(lista):
#         return 0, 0
#
#     suma_nr_pare, suma_nr_impare = suma_lista(lista, i + 1)
#
#     nr = lista[i]
#
#     if nr % 2 == 0:
#         suma_nr_pare += nr
#     else:
#         suma_nr_impare += nr
#
#     return suma_nr_pare, suma_nr_impare
#
# numere = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# suma_nr_pare , suma_nr_impare = suma_lista(numere)
#
# print(f"Suma totala a numerelor din lista este: {suma_nr_pare + suma_nr_impare}")
# print(f"Suma totala a numerelor par din lista este: {suma_nr_pare}")
# print(f"Suma totala a numerelor impare din lista este: {suma_nr_impare}")


# Sa se scrie o functie care citeste de la tastatura si returneaza valoarea daca aceasta este un numar intreg
# altfel returneaza valoare 0

# def numar_intreg():
#     while True:
#
#         a = input()
#
#         if a.isdigit():
#             return a
#
#         else:
#             return 0
#
# print(numar_intreg())