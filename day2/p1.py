#%%
with open('d2data.txt') as f:
    lines = f.readlines()
points = {'X':1, 'Y': 2, 'Z':3}
draw = {'X':'A', 'Y': 'B', 'Z':'C'}
win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
score = 0
for i in lines:
    i = i.rstrip()
    op = i.split(' ')[0]
    me = i.split(' ')[1]
    if op == win[me]:
        score += 6
    elif op == draw[me]:
        score += 3
    score += points[me]
print(score)

# %%
