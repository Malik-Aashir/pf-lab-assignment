# QUESTION 5
n = int(input('Enter number of teams : '))
scores = {}
for i in range(n):
    name = input('Enter team name : ')
    w = int(input('Enter wins : '))
    l = int(input('Enter losses : '))
    scores[name] = [w, l]

# A
t = input('Enter team name : ')
print('winning percentage of', t, 'is', (scores[t][0]/sum(scores[t]))*100)

# B
w_team = [i[0] for i in scores.values()]
print(w_team)

# C
w_rec = []
for i in scores:
    if scores[i][0] > 0:
        w_rec.append(i)
        print(w_rec)