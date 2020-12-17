inp = open("day2input.txt").read().split("\n")

valid_passwords = 0
for i in inp:
    password = list(i.split(": ")[1])
    lower_bound = int(i.split(": ")[0].split()[0].split("-")[0])
    upper_bound = int(i.split(": ")[0].split()[0].split("-")[1])
    letter = i.split(": ")[0].split()[1]

    if password.count(letter) >= lower_bound and password.count(letter) <= upper_bound:
        valid_passwords += 1

print(valid_passwords)
