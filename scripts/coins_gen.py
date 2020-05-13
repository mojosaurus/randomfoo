from itertools import combinations
import pprint
import svgutils.transform as sg
import sys
from svgutils.compose import *
pp = pprint.PrettyPrinter(indent=4)


# Load svg files
imgScale = 0.05 # Scale the image this factor

heads = sg.fromfile("res/svg/rupee-heads.svg")
headsRoot  = heads.getroot()

# This is the number of coins. Input
numCoins = 6

# Spits out the various arragments to get numTails scenario. Input
z=0
for numTails in range(0,numCoins+1):
    arr = range(0,numCoins)
    combos = list(combinations(arr,numTails))

    # TODO: This does not take care of the condition 5 heads, 5 tails is different from 5 tails 5 heads.
    # Need to incorporate that
    if (numCoins % 2) ==0 and  (numCoins/2 == numTails):
        print ("Win condition. Reversing")
        #combos.extend(combos[::-1])
    # Now execute the various scenarios, and print outcomes
    outcomes = []

    for i in combos:
        thiscome = ["Heads" for x in range(0, numCoins)]

        for j in range(0, numTails):
            thiscome[i[j]] = "Tails"
        outcomes.append(thiscome)

    x=0
    for outcome in outcomes:
        y=0
        for flip in outcome:
            item = sg.fromfile("res/svg/rupee-heads.svg").getroot() if flip == "Heads" else sg.fromfile("res/svg/rupee-tails.svg").getroot()
            item.moveto(y*25, z*25, scale=imgScale)
            heads.append(item)
            y += 1
        z += 1
        x += 1

heads.save("tmp/tmp.svg")