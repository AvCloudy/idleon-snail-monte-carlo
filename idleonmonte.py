#!/usr/bin/env python
# Usage: idleonmonte.py <snail level> <encouragement level> <treble notes> 
# <target success rate> <number of sims>
from random import random
import os
import math
import sys

# Current snail level
try:
	currentLevel = int(sys.argv[1])
except:
	currentLevel = 19
# Current snail encouragement level - may need to extract from Idleon Toolbox
try:
	encouragement = int(sys.argv[2])
except:
	encouragement = 13
# Current treble notes from hole - if you don't have snail level up skill, 0
try:
	trebleNotes = int(sys.argv[3])
except:
	trebleNotes = 10920000000
# How many times you want to run each monte carlo simulation
try:
	sims = int(sys.argv[5])
except:
	sims = 1000000
# Calculation for progress bars
simsterm = int(sims/os.get_terminal_size()[0])
# Set success rate at 0 to start, update after first simulation
try:
	target = float(sys.argv[4])
except:
	target = .8
# Set target iterative success rate
print(type(currentLevel), type(encouragement), type(trebleNotes), type(sims), type(target))

successRate = 0
while successRate < target:
	# Calculate chance of one-time success rate
	chanceSuccess = ( (1 - ((currentLevel**0.72)/10)) * 
				  (1+(100*encouragement)/(25+encouragement)/100) * 
				  (1.04**math.log(trebleNotes,10)) ) 
	# Calculate chance of one-time reset rate
	chanceFail = (((currentLevel+1)**0.07) - 1)/(1+(300*encouragement)/(100+encouragement)/100)
	# Create lists to store iterations on success and failure
	successIters = []
	failIters = []
	# Iterate at current encouragement level
	for x in range(sims):
		iterations = 1
		fail = 0
		# Loading bar
		if x % simsterm == 0:
			print(".", end = "")
		if x == (sims-1):
			print("\n", end = "")
		while fail == 0:
			if random() <= chanceSuccess:
				successIters.append(iterations)
				fail = 1
			elif random() > chanceFail:
				iterations += 1
			else: 
				failIters.append(iterations)
				fail = 1
	# Calculate success rate from monte carlo sim
	successRate = len(successIters)/sims
	# Go to start of line - partially overwrite loading bar
	sys.stdout.write("\033[F")
	print("Success rate: {}%".format(successRate*100))
	encouragement += 1
print("Success rate of {}% reached at snail level {} by encouraging it {} times.".format(
	successRate*100, currentLevel, encouragement-1))
print("Did {} sims each round.".format(sims))
