#%%
lines = open('d7data.txt').read().rstrip().split('\n')
class Node():
    def __init__(self, name:str, content:list, parent=None, weight = 0):
        self.name = name
        self.content = content
        if parent is not None:
            self.parent = parent
        self.weight = weight

    def setWeight(self):
        total = 0
        for i in self.content:
            if isinstance(i, int):
                total += i
            else:
                if i.weight == 0:
                    i.setWeight()
                total += i.weight
        self.weight = total

    def part1(self, result:list):
        if self.weight <=100_000:
            result += [self.weight]
        for i in self.content:
            if isinstance(i, Node):
                i.part1(result)
        return result

    def part2(self, target:int, min=0):
        if self.weight > target and self.weight < min:
            min = self.weight
        for i in self.content:
            if isinstance(i, Node):
                min = i.part2(target, min)
        return min

#%%
tree = Node(name='/', content=[])
currentNode = tree

for line in lines:
    if line[0] == '$':
        try:
            _, _, destination = line.split()
            if destination == '..':
                currentNode = currentNode.parent
            else:
                currentNode = next(node for node in currentNode.content if isinstance(node, Node) and node.name == destination)
        except:
            pass
    else:
        content, name = line.split()
        if content == 'dir':
            newNode = Node(name=name, content=[], parent=currentNode)
            currentNode.content += [newNode]
        else:
            currentNode.content += [int(content)]
#%%
tree.setWeight()
result = tree.part1([])
usedSpace = tree.weight
minimalDir = usedSpace
totalSpace = 70_000_000
freeSpace = totalSpace - usedSpace
requiredSpace = 30_000_000
missingSpace = requiredSpace - freeSpace
print(sum(result))
print(tree.part2(missingSpace, usedSpace))
# %%
