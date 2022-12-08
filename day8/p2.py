#%%
import numpy as np
lines = open('d8data.txt').read().rstrip().split()
lines = [[*line] for line in lines]
grid = np.array(lines, dtype=int)

def countScore(tree: int, l:list):
    scenic = 0
    for i in l:
        if i < tree:
            scenic += 1
        else: 
            return scenic+1
    return scenic
# %%
maxScenic = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        tree = grid[i][j]
        left = countScore(tree, grid[i][0:j][::-1])
        right = countScore(tree, grid[i][j+1:len(grid[i])])
        up = countScore(tree, grid[:,j][0:i][::-1])
        down = countScore(tree, grid[:,j][i+1:len(grid[:,j])])
        currentScenic = left * right * up * down
        if currentScenic > maxScenic:
            maxScenic = currentScenic

print(maxScenic)
# %%
