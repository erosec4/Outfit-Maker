# Picks a shirt, pants, and jacket for class or rehearsal

import random

CPants = ['Dark Wash Flare Jeans', 
          'Medium Wash Flare Jeans', 
          'Green Corduroy Jeans', 
          'Charcoal Jeans', 
          'Gray Yoga Pants',
          'Blue Yoga Pants', 
          'Green Leggings', 
          'Blue Pocket Leggings', 
          'Blue Striped Leggings', 
          'Berry Leggings', 
          'Navy Joggers', 
          'Purple Sweats',
          'Brown Shorts',
          'Gray Champion Shorts',
          'White Tennis Skirt'
         ]


CTops = ['Blue White Striped Shirt', 
         'Brown Blue Floral Tank', 
         'Floral Marshalls Short Sleeve', 
         'Ribbed Black Tank', 
         'Fitted Blue Short Sleeve Crop', 
         'Academia Sweater', 
         'Fluffy Pink Sweater', 
         'Navy Sweater', 
         'Black Collared Long Sleeve', 
         'Blue Mock Neck Sweater', 
         'Blue Floral Long Sleeve', 
         'Purple Floral Long Sleeve', 
         'Hard Rock Short Sleeve', 
         'PSU Short Sleeve', 
         'PSU Sweatshirt', 
         'Pink Vans Short Sleeve', 
         'Green Puff Sleeve Crop Top', 
         'Blue Tillys Crop'
        ]

RPants = ['Blue Fabric Shorts',
          'Olive Fabric Shorts',
          'Gray Fabric Shorts',
          'Black Tulip Shorts',
          'Purple Target Shorts',
          'Black Target Shorts',
          'Pink Nike Shorts',
          'Gray Champion Shorts'
         ]

RTops = ['Black Longline Sports Bra',
         'Floral Longline Sports Bra',
         'Blue White Longline Sports Bra',
         'Blue Swirl Long Sports Bra',
         'Blue Tank',
         'Gray Tank',
         'White Tank',
         'Black Tank'
        ]

Outerwear = ['Brown Plaid Button Up', 
             'Green Button Up', 
             'Blue Velvet Button Up', 
             'Light Blue Button Up',
             'Deep Blue Windbreaker', 
             'Black Windbreaker',
             'Track Jacket',
             'Mid Sleeve Light Blue Jacket'
            ]

occasion = input("Rehearsal (R) or Class (C)? ")
fits = int(input("How many outfits? "))
#while fits >= 1:
if occasion == 'C':
  T = random.sample(CTops, k=fits)
  P = random.sample(CPants, k=fits)    
if occasion == 'R':
  T = random.sample(RTops, k=fits)
  P = random.sample(RPants, k=fits)
O = random.choices(Outerwear, k=fits)
while fits >= 1:
  print(T[fits-1], '+', P[fits-1], '+', O[fits-1])
  fits -= 1


''' 
Additions: 
  __ outfits with no repeat items (DONE)
  try again input vs have a nice day
  based on weather (class/object)
  no button ups with sweaters, etc.
'''