# import random

print("Curs 3")


# #Structuri repetitive
# all_choises = [i for i in range(10)]
#
# # - While -
# while True:
#     random_choise = random.choice([i for i in range(10)])
#     if random_choise % 3 == 0:
#         break
#
#     print(f'Selected choise was {random_choise}')
# print(f'Exit choise was {random_choise}')
#
# # - For -
# for i in all_choises:
#     if i % 2 != 0:
#         continue
#     print(f" Numar par {i}")
#
# if True:
#     pass
# else:
#     print('This is False')

# - Functions -

# def my_function(a, b):
#     c = a + b
#     #print(c)
#
#     return c
#
# suma = my_function(1, 2)
#
# print(suma)

# def my_function(list_param):
#     list_param = list(list_param)
#     list_param.append(4)
#
# my_list = [1, 2, 3]
#
# my_function(my_list)
#
# print(my_list)

# def my_function(nume, prenume, varsta = 18, inaltime=171):
#     print(f'Nume: {nume} Prenume: {prenume}, Varsta: {varsta}, Inaltime: {inaltime}cm')
#
# nume = 'Stoica'
# prenume = 'Andrei'
#
# my_function(nume, prenume,inaltime=171,varsta=22)

# def my_function(param_1, param_2, *args, name, age,**kwargs):
#     print('param1', param_1)
#     print('param2', param_2)
#     for p in args:
#         print(p)
#
#     print('Name:', name)
#     print('Age:', age)
#     print(kwargs)
#     for key,value in kwargs.items():
#         print(key, '->' ,value)
#
#
# my_function(1, 2, 3, 4, 5,
#             'some_string',
#             name='Andrei',
#             age=21,
#             job='developer',
#             city='Bucharest')

# - Exceptions -

# my_var = input('introduceti un nr:')
# try:
#     my_int = int(my_var)
#     print(my_var)
# except ValueError as e:
#     print('Va rugam sa introduceti un int! Urmatoare erroare s-a produs:', e)
# except NameError as e:
#     print('Ati folosit o variabila nedeclarata in cod: ', e)
# else:
#     print('We are here because no exception was fired!')
# finally:
#     print('We are execute this block no matter what!')

# - Namespaces -

# print(dir(__builtins__))


# def my_function():
#     global msg
#     msg = 'Salut'
#     print(msg)
#
#
# my_function()
# print(msg)

def my_function():
    
    def my_second_funtions():
        msg = 'lolo'
        print(f'my_second_function: {msg}')

    msg = 'Hello World!'
    my_second_funtions()
    print(f'my_function: {msg}')

my_function()
