#want to pick a shirt and pants that go together
# User enters occasion (class, rehearsal), output is 2-3 components of an outfit

import random

CPants = ['Dark Wash Flare Jeans', 'Blue Yoga Pants', 'Berry Leggings', 'Purple Sweats']
CTops = ['Blue/White Striped Shirt', 'Penn State Shirt', 'Penn State Sweatshirt']
RPants = ['Black Tulip Shorts', 'Purple Shorts', 'Berry Leggings']
RTops = ['Floral Longline Sports Bra', 'Blue Tank']

occasion = input("Rehearsal (R) or Class (C)? ")
if occasion == 'R':
  P = random.choice(RPants)
  T = random.choice(RTops)
  print(T, '+', P)

"""DarkWideJns = {"class"}
BluYoga = {"class"}
BrryLeg = {"class", "rehearsal"}
PrplSweats = {"class"}

PantsList = [DarkWideJns, BluYoga, BrryLeg, PrplSweats]

for pants in PantsList:
  if ("rehearsal" in pants):
    i = PantsList.index(pants)
    # print """


