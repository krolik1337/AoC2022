#%%
with open('d2data.txt') as f:
    lines = f.readlines()
p = [1,2,3]
points = {'A':0, 'B': 1, 'C':2}
score = 0
for i in lines:
    i = i.rstrip()
    op = i.split(' ')[0]
    result = i.split(' ')[1]
    if result == 'Z':
        index = points[op] + 1
        if index > 2: index = 0
        score += 6 + p[index]
    elif result == 'Y':
        index = points[op]
        score += 3 + p[index]
    else:
        index = points[op] - 1
        score += p[index]
print(score)
# %%
