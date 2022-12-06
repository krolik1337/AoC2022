#%%
with open('d1data.txt') as f:
    lines = f.readlines()
max = 0
current = 0
for i in lines:
    if i=="\n":
        if current > max:
            max = current
        current = 0
    else:
        current += int(i)
print(max)
# %%
