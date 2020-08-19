from math import floor
inputs = open("adventDay1_input.txt")

def extraFuel(mass):
    fuel = int(mass) / 3
    floor (fuel)
    fuel -= 2
    return int(fuel)

totalFuel = 0
for input in inputs:
    extraMass = extraFuel(input)
    totalFuel += extraMass

    while extraMass > 0:
        extraMass = extraFuel(extraMass)
        if extraMass > 0:
            totalFuel += extraMass

print (totalFuel)
inputs.close()
