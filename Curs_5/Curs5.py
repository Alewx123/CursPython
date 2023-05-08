# import copy
print("Hello - Curs 5: 2023")
#
#
 Exemplu gresit(nu asignam lambda niciodata pt ca ocupa memorie degeaba)
my_lambda = lambda x, y:x + y
my_sum = my_lambda(2,3)
print (f"my_sum = {my_sum}")
#
# players = [{
#     "first_name": "John",
#     "last_name": "Doe",
#     "rank": 3
# },
#     {
#         "first_name": "Kevin",
#         "last_name": "McDonald",
#         "rank": 1
#     },
#     {
#         "first_name": "Brad",
#         "last_name": "Kelvin",
#         "rank": 5
#     },
# ]
#
#
# # print(sorted(players, key = lambda player: player["rank"]))
# # print(sorted(players, key = lambda player: player["rank"], reverse=True))
#
# def check_top_3_player(player):
#     updated_player = copy.deepcopy(player)
#     # updated_player["is_top_3"] = True if updated_player["rank"] <= 3 else False
#     updated_player["is_top_3"] = updated_player["rank"] <= 3
#     return updated_player
#
# players_with_top_3_value = map(check_top_3_player, players)
# print(list(players_with_top_3_value))
#
# all_mcdonalds = filter(lambda player: player["last_name"] == "McDonald", players)
# print("All McDonalds ",list(all_mcdonalds))

# list_1 = [1, 2, 3]
# list_2 = [10, 20, 30]
# list_3 = [100, 200, 300]
#
# z = zip(list_1, list_2, list_3)
#
# print(list(z))


# names = ["Ion", "Elena", "Andreea"]
# ages = [20, 18, 35]
# jobs = ["engineer", "consultant", "teacher"]
#
# z = zip(names, ages, jobs)
#
# for name, age, job in z:
#     print(f"{name} is {job} and has {age} years")


my_numbers = list(range(1,11))
print(my_numbers)

#
# #Varianta C
# squared = []
# for i in my_numbers:
#     squared.append(i ** 2)
#
# print(squared)

#Varianta cu list comprehantion

squared = [i ** 2 for i in my_numbers]
print(squared)

squared_even_nr = [i ** 2 for i in my_numbers if i % 2 == 0]
print(squared_even_nr)