import math

def read_input():
    with open("input.txt") as f:
        return [int(line) for line in f]
    return


masses = read_input()

def mass_to_fuel(mass):
    return math.floor(mass / 3) - 2 

def mass_to_fuel_recurse(mass):
    current_fuel = math.floor(mass / 3) - 2 
    if current_fuel > 0:
        return current_fuel + mass_to_fuel_recurse(current_fuel)
    else:
        return 0

fuel_sum = 0

for mass in masses:
    fuel_sum += mass_to_fuel(mass)

print("The sum of the fuel requirements for all of the modules on your spacecraft is %d"%fuel_sum)

fuel_sum = 0

for mass in masses:
    fuel_sum += mass_to_fuel_recurse(mass)
print("The sum of the fuel requirements for all of the modules on your spacecraft\nwhen also taking into account the mass of the added fuel is %d"%fuel_sum)