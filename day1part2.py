inp = open("day1input.txt").read()
inp = inp.split("\n")
for i in range(len(inp)):
    inp[i] = int(inp[i])



for i in range(len(inp)):
    for j in range(i, len(inp)):
        for k in range(j, len(inp)):
            if inp[i] + inp[j] + inp[k] == 2020:
                print(inp[i] * inp[j] * inp[k])
        
