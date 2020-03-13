def tower_builder(n_floors):
    floors = []
    max_on_lvl = (n_floors * 2) - 1 if (n_floors * 2) - 1 else 1

    for floor in range(n_floors):
        if max_on_lvl == 1:
            stars_on_lvl = 1
        else:
            stars_on_lvl = floor * 2 + 1
        whitespaces = (max_on_lvl - stars_on_lvl) // 2
        floors.append(" " * whitespaces + "*" * stars_on_lvl + " " * whitespaces)

    return floors


for line in tower_builder(1): print(f'{line} \n')
for line in tower_builder(2): print(f'{line} \n')
for line in tower_builder(3): print(f'{line} \n')
for line in tower_builder(4): print(f'{line} \n')
for line in tower_builder(5): print(f'{line} \n')