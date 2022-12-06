#%%
with open('d3data.txt') as f:
    lines = f.readlines()
sum = 0
group = []
# %%
def getPriority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27
#%%
for rucksack in lines:
    rucksack = rucksack.rstrip()
    group += [rucksack]
    if len(group) == 3:
        common = ''
        for j in group[0]:
            if j in group[1] and j in group[2]:
                common = j
                break
        sum += getPriority(common)
        group = []
print(sum)
# %%
