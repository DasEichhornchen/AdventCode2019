inputs = open("adventDay3_input.txt")
# inputs = open("testInput.txt")

wires = []
wire1 = {'xPos': 0, 'yPos': 0, 'posList': []}
wire2 = {'xPos': 0, 'yPos': 0, 'posList': []}
# shortestDistance = None
shortestSteps = None
intersections = []

# function that check if specific coordinates are present in a specific list
def isIntersection(posList, x, y):
    if (x,y) in posList:
        intersections.append((x,y))
        return True
    else:
        return False

# Here I make two lists, one per wire, where I strip the spaces and split on the commas
for line in inputs:
    wires.append(line.strip().split(','))

# For each movement in the first list we just created (wire 1)
for movement in wires[0]:
    iterable = 1
    while iterable < int(movement[1::]) + 1:
        if movement[0] == 'R':
            wire1['xPos']+=1
        if movement[0] == 'L':
            wire1['xPos']-=1
        if movement[0] == 'U':
            wire1['yPos']+=1
        if movement[0] == 'D':
            wire1['yPos']-=1
        # Here we log every position on the wire to compare them later with wire 2
        wire1['posList'].append((wire1['xPos'], wire1['yPos']))
        iterable+=1

# For each movement in the second list we created (wire 2)
for movement in wires[1]:
    iterable = 1
    while iterable < int(movement[1::]) + 1:
        if movement[0] == 'R':
            wire2['xPos']+=1
        if movement[0] == 'L':
            wire2['xPos']-=1
        if movement[0] == 'U':
            wire2['yPos']+=1
        if movement[0] == 'D':
            wire2['yPos']-=1
        # Here we log every position on the wire to compare them later with wire 2
        wire2['posList'].append((wire2['xPos'], wire2['yPos']))
        # We check if the current position of the wire2 matchs a position of the wire1.
        isIntersection(wire1['posList'], wire2['xPos'], wire2['yPos'])
        iterable+=1

for intersection in intersections:
    stepsW1 = wire1['posList'].index(intersection) + 1
    stepsW2 = wire2['posList'].index(intersection) + 1
    if shortestSteps == None:
        shortestSteps = stepsW1 + stepsW2
    elif shortestSteps > stepsW1 + stepsW2:
        shortestSteps = stepsW1 + stepsW2

print (shortestSteps)


#     if shortestDistance == None:
#         shortestDistance = abs(intersection[0])+abs(intersection[1])
#     elif shortestDistance > abs(intersection[0])+abs(intersection[1]):
#         shortestDistance = abs(intersection[0])+abs(intersection[1])
# print (shortestDistance)
