#%%
with open('d1data.txt') as f:
    lines = f.readlines()
x = []
current = 0
for i in lines:
    if i=="\n":
        x += [current]
        current = 0
    else:
        current += int(i)
print(sum(sorted(x, reverse=True)[:3]))
# %%
