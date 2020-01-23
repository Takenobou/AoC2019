import math

fuel = []
total_fuel = 0

with open('fcuinput.txt') as f:
    mass = f.read().splitlines()
    mass = list(map(int, mass))

for x in range(len(mass)): 
    cmass = mass[x] / 3 
    cmass = math.floor(cmass)
    cmass = cmass - 2  
    fuel.append(cmass)
    
fuel = list(map(int, fuel))

for x in fuel:
    total_fuel += x

print(total_fuel)