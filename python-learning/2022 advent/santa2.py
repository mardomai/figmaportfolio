with open('data2.txt') as f:
    lines = list(filter(None, f.read().split('\n')))

#A = Rock  = 1
#X = Rock = 1
#Y = Paper = 2
#B = Paper = 2
#C = Scissors = 3
#Z = Scissors = 3

combos, score = ['BX', 'CX', 'AX', 'AY', 'BY', 'CY', 'CZ', 'AZ', 'BZ'], 0 


for game_round in lines: 
    score +=combos.index(game_round.replace(" ", "")) +1 

print(str(score))
