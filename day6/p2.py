#%%
line = open('d6data.txt').read().rstrip()
for output in range(14, len(line)):
    if len(set(line[output-14: output])) == 14:
        print(output)
        break
# %%
