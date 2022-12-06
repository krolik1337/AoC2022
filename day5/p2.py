#%%
lines = open('d5data.txt').read().rstrip().splitlines()
storage = []

def move(line):
    _, amount, _, source, _ ,dest = line.split()
    amount, source, dest = map(int, [amount, source, dest])
    storage[dest-1] += storage[source-1][-amount:]
    del storage[source-1][-amount:]

for line in lines:
    if '[' in line:
        for i, j in zip(range(len(line)//4 + 1), range(0, len(line), 4)):
            cargo = line[j+1]
            try:
                isinstance(storage[i], list)
            except:
                storage += [[]]
            if cargo != ' ':
                storage[i].insert(0, cargo)
    elif 'move' in line:
        move(line)
    else:
        pass
output = ''
for i in storage:
    output += i[-1]
print(output)


# %%
