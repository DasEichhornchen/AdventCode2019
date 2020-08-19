# inputs = open("adventDay3_input.txt")
inputs = open("testInput.txt")

wires = []
wire1 = {'xPos': 0, 'yPos': 0, 'posList': []}
wire2 = {'xPos': 0, 'yPos': 0}
# shortestDistance = None
# intersections = []
stepsW1 = 0
stepsW2 = 0
firstIntersect = None
intersectFound = 0

# function that check if specific coordinates are present in a specific list
def isIntersection(posList, x, y):
    if (x,y) in posList:
        # intersections.append((x,y))
        print ("Intersection at {}".format((x,y)))
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
        wire1['posList'].append((wire1['xPos'], wire1['yPos'])) # Here we log every position on the wire to compare them later with wire 2
        iterable+=1

# For each movement in the second list we created (wire 2)
for movement in wires[1]:
    if intersectFound:
        print ("Intersection has been found, moving on to the next step") # In case an intersection has been found, we get out of the loop and move on to the next step
        break
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
        stepsW2 += 1 # For every movement we make, we increase the number of steps by 1
        if isIntersection(wire1['posList'], wire2['xPos'], wire2['yPos']): # We check if the current position of the wire2 matchs a position of the wire1.
            intersectFound = 1 # In case it does match, we set this flag to 1 to get out of the bigger "for" loop
            firstIntersect = (wire2['xPos'], wire2['yPos']) # As the first intersection of wire 2 with wire 1 is the closest to the origin, "number-of-step" speak, we register the current position as the first intersection
            print ("{} steps for wire2".format(stepsW2))
            break
        iterable+=1

if intersectFound:
    # print (firstIntersect)
    stepsW1 = wire1['posList'].index(firstIntersect) + 1 # As we know the position where the 2 wires are intersecting for the 1st time, we look for that specific position in the wire1 position list. Index + 1 = the number of steps it took us to go there.
    print (stepsW1)
    print ("{} steps in total".format(stepsW1+stepsW2))


# for intersection in intersections:
#     if shortestDistance == None:
#         shortestDistance = abs(intersection[0])+abs(intersection[1])
#     elif shortestDistance > abs(intersection[0])+abs(intersection[1]):
#         shortestDistance = abs(intersection[0])+abs(intersection[1])
# print (shortestDistance)
