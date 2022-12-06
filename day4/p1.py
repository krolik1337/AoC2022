#%%
lines = open('d4data.txt').read().strip().split()
sum = 0
#%%
for line in lines:
    first, second = line.split(',')
    fstart, fend = map(int, first.split('-'))
    sstart, send = map(int, second.split('-'))
    if (fstart <= sstart and fend >= send) or (fstart >= sstart and fend <= send):
        sum += 1
print(sum)
# %%
