# LoadingCargoA.py
from itertools import combinations

# one possible heuristic solution
cargo = [9, 7, 3, 4, 5]

for n in range(len(cargo)//2 + 1, 1, -1):
    combinations_crate = list(combinations(cargo, n))
    print(combinations_crate)
print(cargo, 'has a sum of ', sum(cargo))
truck1 = []
truck2 = []
for crate in cargo:
    print(crate)
    if crate + sum(truck1) <= 14:
        truck1.append(crate)
    else:
        if crate + sum(truck2) <= 14:
            truck2.append(crate)

print(truck1, 'has a sum of', sum(truck1))
print(truck2, 'has a sum of', sum(truck2))
