import random

# Define the categories
stats = ['STR', 'FORT', 'AGL', 'INT', 'WILL', 'CH']
attunements = ['FLAME', 'FROST', 'GALE', 'THDR', 'IRON', 'SHDW', 'NO ATTUNEMENT']
weapons = ['MED', 'LGHT', 'HVY']

# Initialize the build
build = {stat: 0 for stat in stats}
build['ATTUNEMENT'] = random.choice(attunements)
if build['ATTUNEMENT'] != 'NO ATTUNEMENT':
    build[build['ATTUNEMENT']] = random.randint(1, 99)
build['WEAPON'] = random.choice(weapons)
build[build['WEAPON']] = random.randint(1, 99)

# Distribute the points
points = 323 - build[build['ATTUNEMENT']] - build[build['WEAPON']]
while points > 0:
    stat = random.choice(stats)
    if build[stat] < 100:
        allocation = min(random.randint(1, points), 99 - build[stat])
        build[stat] += allocation
        points -= allocation

# Ensure no more than one category has 100 points
categories_with_100 = [k for k, v in build.items() if v == 100]
while len(categories_with_100) > 1:
    category_to_reduce = random.choice(categories_with_100)
    reduction = random.randint(1, build[category_to_reduce] - 1)
    build[category_to_reduce] -= reduction
    points += reduction
    categories_with_100 = [k for k, v in build.items() if v == 100]

# Print the build
for key, value in build.items():
    if key in stats or key == build['ATTUNEMENT'] or key == build['WEAPON']:
        print(f'{key}: {value}')
print(f'Points allocated (Just to make sure it used 323): {sum([v for k, v in build.items() if k in stats or k == build["ATTUNEMENT"] or k == build["WEAPON"]])}')
