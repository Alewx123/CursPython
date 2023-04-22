L = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

print(f"Lista initiala este {L}")

ordonata = sorted(L)

print(f"Lista ordonata ascendent este {ordonata}")

print(f"Lista ordonata descendent este {ordonata[::-1]}")

print(f"Lista numerelor cu indici pari este {L[::2]}")

print(f"Lista numerelor cu indici impari este {L[1::2]}")

Multiplii_3 = [i for i in L if (i % 3 == 0)]

print(f"Elementele multiple ale lui 3 sunt {Multiplii_3} ", end="")
