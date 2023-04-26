with open('data.txt') as f:
    lines = f.readlines()

one, two, three = 0, 0, 0
zero = 0

for calo in lines:
    if calo != '\n':
        zero += int(calo)
    else:
        if zero > three:
            if zero < two:
                three = zero
            elif zero < one:
                two, three = zero, two
            else:
                one, two, three = zero, one, two
        zero = 0

print(sum([one, two, three]))