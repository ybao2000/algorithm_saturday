# Choose your own path
N = int(input())
tree = {} # this is a dictionary, key is the node, values are the children
for i in range(N):
  vals = input().split()
  # the first value is Mi, the number of the children
  # others are the children
  if int(vals[0]) > 0:  # make sure this is greater than 0
    tree[i+1] = [int(val) for index, val in enumerate(vals) if index > 0]

# we need 2 answer, 1 is whether all pages are included, 2 is short level
minLevel = 20000  # we will put min level in this minLevel
# using BFS (guarantee to get the shortest path)
queue = [(1, 1)]  # we use tuple as element of the queue
# first one is the page number, second one is the level
visited = {1} # visited is a set, containing all visited pages
while queue:
  page, level = queue.pop(0)  # BFS, always pops the top one
  if page not in tree:  # end
    if level < minLevel:  # compare your level with minLevel
      minLevel = level
  else:
    for nextPage in tree[page]:
      if nextPage not in visited:
        queue.append((nextPage, level+1))
        visited.add(nextPage)

if len(visited) < N:
  print("N")
else: 
  print("Y")
print(minLevel)