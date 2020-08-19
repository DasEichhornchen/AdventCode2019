# inputs = open("adventDay3_input.txt")
inputs = open("testInput.txt")

wires = []
wire1 = {'xPos': 0, 'yPos': 0, 'xPosList': [], 'yPosList': [], 'posList': []}
wire2 = {'xPos': 0, 'yPos': 0, 'xPosList': [], 'yPosList': [], 'posList': []}
shortestDistance = None
intersections = []

for line in inputs:
    wires.append(line.strip().split(','))

for movement in wires[0]:
    iterable = 0
    if movement[0] == 'R':
        while iterable < int(movement[1::]):
            wire1['xPos']+=1
            wire1['posList'].append((wire1['xPos'], wire1['yPos']))
            iterable+=1
    if movement[0] == 'L':
        while iterable < int(movement[1::]):
            wire1['xPos']-=1
            wire1['posList'].append((wire1['xPos'], wire1['yPos']))
            iterable+=1
    if movement[0] == 'U':
        while iterable < int(movement[1::]):
            wire1['yPos']+=1
            wire1['posList'].append((wire1['xPos'], wire1['yPos']))
            iterable+=1
    if movement[0] == 'D':
        while iterable < int(movement[1::]):
            wire1['yPos']-=1
            wire1['posList'].append((wire1['xPos'], wire1['yPos']))
            iterable+=1

for movement in wires[1]:
    iterable = 0
    if movement[0] == 'R':
        while iterable < int(movement[1::]):
            wire2['xPos']+=1
            wire2['posList'].append((wire2['xPos'], wire2['yPos']))
            iterable+=1
    if movement[0] == 'L':
        while iterable < int(movement[1::]):
            wire2['xPos']-=1
            wire2['posList'].append((wire2['xPos'], wire2['yPos']))
            iterable+=1
    if movement[0] == 'U':
        while iterable < int(movement[1::]):
            wire2['yPos']+=1
            wire2['posList'].append((wire2['xPos'], wire2['yPos']))
            iterable+=1
    if movement[0] == 'D':
        while iterable < int(movement[1::]):
            wire2['yPos']-=1
            wire2['posList'].append((wire2['xPos'], wire2['yPos']))
            iterable+=1

for (x,y) in wire1['posList']:
    for (i,j) in wire2['posList']:
        if (x,y) == (i,j):
            intersections.append((x,y))

for (x,y) in intersections:
    if shortestDistance == None:
        shortestDistance = abs(x)+abs(y)
    elif shortestDistance > abs(x)+abs(y):
        shortestDistance = abs(x)+abs(y)

print(shortestDistance)
