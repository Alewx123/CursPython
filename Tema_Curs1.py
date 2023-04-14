L = [7,8,9,2,3,1,4,10,5,6]

print(f"Lista initiala este {L}")
ordonata = sorted(L)
print(f"Lista ordonata ascendent este {ordonata}")
print(f"Lista ordonata descendent este {ordonata[::-1]}")
print(f"Lista numerelor cu indici pari este {L[::2]}")
print(f"Lista numerelor cu indici impari este {L[1::2]}")

print(f"Elementele multiple ale lui 3 sunt ", end="")
for i in L:
    if i % 3 == 0:
        print(i, end=" ")