inp = open("day2input.txt").read().split("\n")

valid_passwords = 0
for i in inp:
    password = list(i.split(": ")[1])
    first_position = int(i.split(": ")[0].split()[0].split("-")[0]) - 1
    second_position = int(i.split(": ")[0].split()[0].split("-")[1]) - 1
    letter = i.split(": ")[0].split()[1]

    if (password[first_position] == letter) ^ (password[second_position] == letter):
        valid_passwords += 1

print(valid_passwords)
