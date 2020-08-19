import random
def genList(nbElem, lowestElem, highestElem):
    randomList = []
    for i in range(0,nbElem):
        n = random.randint(lowestElem,highestElem)
        randomList.append(n)
    return randomList

nb = int(input('Number of elements:\n'))
low = int(input('Lowest element:\n'))
high = int(input('Highest element:\n'))

print (genList(nb, low, high))

# 2147483647
# [30, 6, 28, 16, 3, 24, 16, 22, 3, 17, 23, 12, 11, 6, 19, 17, 2, 23, 11, 23, 1, 23, 18, 21, 24, 19, 25, 1, 13, 17, 1, 8, 18, 22, 13, 26, 4, 6, 26, 20, 9, 5, 2, 16, 1, 18, 11, 2, 8, 11, 4, 15, 14, 4, 30, 17, 30, 8, 12, 20, 20, 16, 4, 22, 28, 29, 21, 23, 29, 16, 13, 15, 18, 2, 12, 28, 6, 11, 7, 3, 9, 8, 15, 15, 7, 17, 27, 16, 11, 27, 5, 23, 13, 13, 23, 8, 24, 9, 23, 4, 9]
