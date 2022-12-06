#%%
lines = open('d4data.txt').read().strip().split()
sum = 0
#%%
for line in lines:
    first, second = line.split(',')
    fstart, fend = map(int, first.split('-'))
    sstart, send = map(int, second.split('-'))
    if len(set(range(fstart, fend+1)).intersection(set(range(sstart, send+1)))) > 0:
        sum+=1
print(sum)
# %%
