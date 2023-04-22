#Pachete din cursul 3
from my_package.my_module import my_var as var  # importez doar variabila my_var si are alias 'as' ca var
from my_package.my_second_module import *  # cu * importeaza tot

my_var = 10
print(var, my_var)

my_second_function('Andrei')
