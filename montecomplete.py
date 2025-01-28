#!/usr/bin/env python
# Uses monte carlo simulation to simulate the most efficient way to spend snail mail

from random import random
import math
import sys

def chanceSuccess(currentLevel, encouragement):
    return(min(1,((1 - ((currentLevel**0.72)/10)) * (1+(100*encouragement)/(25+encouragement)/100) * 
        (1.04**math.log(trebleNotes,10)))))

def chanceFailure(currentLevel, encouragement):
    return(max(0,(((currentLevel+1)**0.07) - 1)/(1+(300*encouragement)/(100+encouragement)/100)))

try:
    trebleNotes = int(sys.argv[0])
except:
    trebleNotes = 10920000000
# How many times you want to run each monte carlo simulation
try:
    sims = int(sys.argv[1])
except:
    sims = 5

try:
    encouragementRange = int(sys.argv[2])
except:
    encouragementRange = 5

sims05 = []
sims510 = []
sims1015 = []
sims1520 = []
sims2025 = []

minLevel = 1
if chanceSuccess(25,0) == 1:
    sims2025.append(((0,0,0,0,0),0))
    minLevel = 25
elif chanceSuccess(20,0) == 1:
    sims1520.append(((0,0,0,0,0),0))
    minLevel = 20
elif chanceSuccess(15,0) == 1:
    sims1015.append(((0,0,0,0,0),0))
    minLevel = 15
elif chanceSuccess(10,0) == 1:
    sims510.append(((0,0,0,0,0),0))
    minLevel = 10
elif chanceSuccess(5,0) == 1:
    sims05.append(((0,0,0,0,0),0))
    minLevel = 5

# really really slow, obviously. 
# going to try strategy of creating a list of lists, [range(20)] * 25, and iterating over that
# by not bunching simulations, can also just create code that works across any level
# while currentLevel % 5 != 0: currentLevel -= 1 or currentLevel -= currentLevel % 5

for iteration in range(sims):
    for v in range(encouragementRange+1):
        for w in range(encouragementRange+1):
            for x in range(encouragementRange+1):
                for y in range(encouragementRange+1):
                    for z in range(encouragementRange+1):
                        encouragement = (v,w,x,y,z)
                        currentLevel = minLevel
                        mailTaken = 0
                        mailTaken510 = 0
                        mailTaken1015 = 0
                        mailTaken1520 = 0
                        mailTaken2025 = 0
                        while currentLevel < 5:
                            if random() <= chanceSuccess(currentLevel, encouragement[currentLevel-1]):
                                mailTaken = mailTaken + encouragement[currentLevel - 1] + 3
                                currentLevel += 1
                            elif random() < chanceFailure(currentLevel, encouragement[currentLevel-1]):
                                mailTaken = mailTaken + encouragement[currentLevel - 1] + 3
                                currentLevel = 1
                            else:
                                mailTaken += 3
                        while currentLevel < 10:
                            if random() <= chanceSuccess(currentLevel, encouragement[currentLevel % 5 - 1]):
                                mailTaken510 = mailTaken510 + encouragement[currentLevel % 5 - 1] + 3
                                currentLevel += 1
                            elif random() < chanceFailure(currentLevel, encouragement[currentLevel % 5 - 1]):
                                mailTaken510 = mailTaken510 + encouragement[currentLevel % 5 - 1] + 3
                                currentLevel = 5
                            else:
                                mailTaken510 += 3
                        while currentLevel < 15:
                            if random() <= chanceSuccess(currentLevel, encouragement[currentLevel % 5 - 1]):
                                mailTaken1015 = mailTaken1015 + encouragement[currentLevel % 5 - 1] + 3
                                currentLevel += 1
                            elif random() < chanceFailure(currentLevel, encouragement[currentLevel % 5 - 1]):
                                mailTaken1015 = mailTaken510 + encouragement[currentLevel % 5 - 1] + 3
                                currentLevel = 10
                            else:
                                mailTaken1015 += 3
                        while currentLevel < 20:
                            if random() <= chanceSuccess(currentLevel, encouragement[currentLevel % 5 - 1]):
                                mailTaken1520 = mailTaken1520 + encouragement[currentLevel % 5 - 1] + 3
                                currentLevel += 1
                            elif random() < chanceFailure(currentLevel, encouragement[currentLevel % 5 - 1]):
                                mailTaken1520 = mailTaken1520 + encouragement[currentLevel % 5 - 1] + 3
                                currentLevel = 15
                            else:
                                mailTaken1015 += 3
                        while currentLevel < 25:
                            if random() <= chanceSuccess(currentLevel, encouragement[currentLevel % 5 - 1]):
                                mailTaken2025 = mailTaken2025 + encouragement[currentLevel % 5 - 1] + 3
                                currentLevel += 1
                            elif random() < chanceFailure(currentLevel, encouragement[currentLevel % 5 - 1]):
                                mailTaken2025 = mailTaken2025 + encouragement[currentLevel % 5 - 1] + 3
                                currentLevel = 15
                            else:
                                mailTaken1015 += 3
                        sims05.append((encouragement, mailTaken))
                        sims510.append((encouragement, mailTaken510))
                        sims1015.append((encouragement, mailTaken1015))
                        sims1520.append((encouragement, mailTaken1520))
                        sims2025.append((encouragement, mailTaken2025))
        print(".", end = "") 

print("")
fullSequence = []
for sim in [sims05,sims510,sims1015,sims1520,sims2025]:
    uniqueSims = {}
    averageSims = {}
    for x in sim:
        if x[0] in uniqueSims:
            uniqueSims[x[0]].append(x[1])
        else:
            uniqueSims[x[0]] = [x[1]]
    for x in uniqueSims:
        averageSims[x] = sum(uniqueSims[x])/len(uniqueSims[x])
    
    listOfMins = [key for key in averageSims if averageSims[key] == min(averageSims.values())]
    listOfMinsTotalVal = []

    for x in listOfMins:
        listOfMinsTotalVal.append(x[0] + x[1] + x[2] + x[3] + x[4])

    shortestSequence = listOfMins[listOfMinsTotalVal.index((min(listOfMinsTotalVal)))]
    fullSequence.append(shortestSequence)

print("You should encourage the following number of times at each level:\
      \n 1: {} \t6: {} \t11: {} \t16: {}\t21: {}\n 2: {} \t7: {} \t12: {} \t17: {}\t 22: {}\
      \n 3: {} \t8: {} \t13: {} \t18: {}\t23: {}\n 4: {} \t9: {} \t14: {} \t19: {}\t24: {}\
      \n 5: {} \t10: {} \t15: {} \t20: {}\t 25: {}".format(
    fullSequence[0][0],fullSequence[1][0],fullSequence[2][0],fullSequence[3][0], fullSequence[4][0],
    fullSequence[0][1],fullSequence[1][1],fullSequence[2][1],fullSequence[3][1], fullSequence[4][1],
    fullSequence[0][2],fullSequence[1][2],fullSequence[2][2],fullSequence[3][2], fullSequence[4][2],
    fullSequence[0][3],fullSequence[1][3],fullSequence[2][3],fullSequence[3][3], fullSequence[4][3],
    fullSequence[0][4],fullSequence[1][4],fullSequence[2][4],fullSequence[3][4], fullSequence[4][4]
))
