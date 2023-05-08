import csv

new_cars = [
    ["Dacia", "Logan", 2005 , 75],
    ["Renault", "Cilio", 2005 , 75]
]

with open("cars.csv", "a", newline="") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ",")
    for new_car in new_cars:
        csv_writer.writerow(new_car)