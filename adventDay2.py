def resetList():
    inputs = open("adventDay2_input.txt")
    for input in inputs:
        inpList = input.strip().split(',')
    inputs.close()
    inpList = list(map(int, inpList))
    return inpList


noun = None
verb = None

for i in range(0,101):
    for j in range (0,101):
        inpList = resetList()
        inpList[1] = i
        inpList[2] = j
        # print(inpList)
        for x in range (0, len(inpList)+1, 4):
            if inpList[x] == 1:
                inpList[inpList[x+3]] = inpList[inpList[x+1]] + inpList[inpList[x+2]]
            elif inpList[x] == 2:
                inpList[inpList[x+3]] = inpList[inpList[x+1]] * inpList[inpList[x+2]]
            elif inpList[x] == 99:
                break
            else:
                print("Wrong value")

        if inpList[0] == 19690720:
            (noun,verb) = (i,j)
            break
    if inpList[0] == 19690720:
        break


print ((noun,verb))
print (inpList[0])
print (100*noun+verb)
