#%%
line = open('d6data.txt').read().rstrip()
for output in range(4, len(line)):
    if len(set(line[output-4: output])) == 4:
        print(output)
        break

for i in range(4, len(open('d6data.txt').read().rstrip())):
    if len(set(line[i-4: i])) == 4:print(i);break
# %%
