
total = 0

with open('data4.txt') as f:
    lines = f.readlines()

    for line in lines:

        pair = line.rstrip().split(',')
        (a, b) = list(map(int, pair[0].split('-')))
        (c, d) = list(map(int, pair[1].split('-')))

        if (a > c) or (a == c and d > b):
            a, b, c, d = c, d, a, b
        
        if b >= c:
            total += 1

print(total)