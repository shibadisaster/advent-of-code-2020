#to anyone else who looks at this, im sorry
inp = open("day3input.txt").read().split("\n")

for i in range(len(inp)):
    inp[i] = list(inp[i])

columns = len(inp[0])
rows = len(inp)
trees_product = 1

#(1, 1)
horizontal_movement = 1
vertical_movement = 1
position = [0, 0]

trees = 0
for _ in range(len(inp) - 1):
    if position[1] % vertical_movement == 0:
        position[0] += horizontal_movement
        position[1] += vertical_movement

        if inp[position[1]][position[0] % columns] == "#":
            trees += 1

print(trees)
trees_product *= trees





#(3, 1)
horizontal_movement = 3
vertical_movement = 1
position = [0, 0]

trees = 0
for _ in range(len(inp) - 1):
    if position[1] % vertical_movement == 0:
        position[0] += horizontal_movement
        position[1] += vertical_movement

        if inp[position[1]][position[0] % columns] == "#":
            trees += 1

print(trees)
trees_product *= trees






#(5, 1)
horizontal_movement = 5
vertical_movement = 1
position = [0, 0]

trees = 0
for _ in range(len(inp) - 1):
    if position[1] % vertical_movement == 0:
        position[0] += horizontal_movement
        position[1] += vertical_movement

        if inp[position[1]][position[0] % columns] == "#":
            trees += 1

print(trees)
trees_product *= trees








#(7, 1)
horizontal_movement = 7
vertical_movement = 1
position = [0, 0]

trees = 0
for _ in range(len(inp) - 1):
    if position[1] % vertical_movement == 0:
        position[0] += horizontal_movement
        position[1] += vertical_movement

        if inp[position[1]][position[0] % columns] == "#":
            trees += 1

print(trees)
trees_product *= trees








#(1, 2)
horizontal_movement = 1
vertical_movement = 2
position = [0, 0]

trees = 0
for row in range(len(inp) - 1):
    if row % vertical_movement == 0:
        position[0] += horizontal_movement
        position[1] += vertical_movement

        if inp[position[1]][position[0] % columns] == "#":
            trees += 1

print(trees)
trees_product *= trees






print(trees_product)
