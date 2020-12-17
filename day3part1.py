inp = open("day3input.txt").read().split("\n")

for i in range(len(inp)):
    inp[i] = list(inp[i])

columns = len(inp[0])
rows = len(inp)

#wow!!!! a flexible code
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
            print(str(position[0] % columns) + ", " + str(position[1]) + "!!!")
            
        else:
            print(str(position[0] % columns) + ", " + str(position[1]))

print(trees)
