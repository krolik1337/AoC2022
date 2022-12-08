#%%
import numpy as np
lines = open('d8data.txt').read().rstrip().split()
# lines = open('d8test.txt').read().rstrip().split()
lines = [[*line] for line in lines]
grid = np.array(lines, dtype=int)
# %%
visible = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i in [0, len(grid)-1] or j in [0, len(grid[:,i])-1]:
            visible += 1
        else:
            tree = grid[i][j]
            left = all([x < tree for x in grid[i][0:j]])
            right = all([x < tree for x in grid[i][j+1:len(grid[i])]])
            up = all([x < tree for x in grid[:,j][0:i]])
            down = all([x < tree for x in grid[:,j][i+1:len(grid[:,j])]])
            if left or right or up or down:
                visible += 1

print(visible)
# %%

