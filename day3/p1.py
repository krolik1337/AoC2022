#%%
with open('d3data.txt') as f:
    lines = f.readlines()
sum = 0
# %%
def getPriority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27
#%%
for rucksack in lines:
    rucksack = rucksack.rstrip()
    l = len(rucksack)
    first = rucksack[slice(0, l//2)]
    second = rucksack[slice(l//2, l)]
    common = ''
    for j in first:
        if j in second:
            common = j
            break
    sum += getPriority(common)
print(sum)
# %%
