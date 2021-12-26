# LoadingCargoA.py
import random

cargo = []
while sum(cargo) < 28:
    crate = random.randint(1, 28)
    cargo.append(crate)

cargo.sort()
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
