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

def isIntersection(posList, x, y):
    if (x,y) in posList:
        # intersections.append((x,y))
        print ("Intersection at {}".format((x,y)))
        return True
    else:
        return False

for line in inputs:
    wires.append(line.strip().split(','))

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
        wire1['posList'].append((wire1['xPos'], wire1['yPos']))
        iterable+=1

for movement in wires[1]:
    if intersectFound:
        print ("Intersection has been found, moving on to the next step")
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
        stepsW2 += 1
        if isIntersection(wire1['posList'], wire2['xPos'], wire2['yPos']):
            intersectFound = 1
            firstIntersect = (wire2['xPos'], wire2['yPos'])
            print ("{} steps for wire2".format(stepsW2))
            break
        iterable+=1

if intersectFound:
    print("Entering check steps for wire 1")
    # print (firstIntersect)
    stepsW1 = wire1['posList'].index(firstIntersect) + 1
    print (stepsW1)
    print ("{} steps in total".format(stepsW1+stepsW2))


# for intersection in intersections:
#     if shortestDistance == None:
#         shortestDistance = abs(intersection[0])+abs(intersection[1])
#     elif shortestDistance > abs(intersection[0])+abs(intersection[1]):
#         shortestDistance = abs(intersection[0])+abs(intersection[1])
# print (shortestDistance)
