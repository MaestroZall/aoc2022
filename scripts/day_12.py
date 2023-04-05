#day 12
import random
import numpy as np
import networkx as nx
import matplotlib as plt
with open(r'C:\Users\zalon\Downloads\aoc2022\day_12_data.txt', "r", encoding="utf-8") as f:
        # with open(Path(dirname(file)) / f"test_input.txt", "r", encoding="utf-8") as f:
    data = f.read().split('\n')
    grid = np.array([list(map(ord, d)) for d in data])

#start position
grid[20][0] = 97
#get end position
grid[20][112] = 122

def array_to_adj(hill_array):
  size = len(hill_array)*len(hill_array[0])
  adj_array = np.zeros([size,size])
  for row,row_value in enumerate(hill_array):
    for column,column_value in enumerate(row_value):
      #left
      if column>0:
        #left is space that we are moving to, 1 is our max climb
        if hill_array[row][column-1] <= (hill_array[row][column])+1:
          #rada*delka radku + sloupec
          adj_array[row*(len(grid[0]))+column][row*(len(grid[0]))+column-1] = 1
      #right
      if column<(len(grid[0])-1):
        if hill_array[row][column+1] <= hill_array[row][column]+1:
          adj_array[row*(len(grid[0]))+column][row*(len(grid[0]))+column+1] = 1
      #down
      if row<(len(hill_array)-1):
        if hill_array[row+1][column] <= hill_array[row][column]+1:
          adj_array[row*(len(grid[0]))+column][(row+1)*(len(grid[0]))+column] = 1
      #up
      if row>0:
        if hill_array[row-1][column] <= hill_array[row][column]+1:
          adj_array[row*(len(grid[0]))+column][(row-1)*(len(grid[0]))+column] = 1
  return(adj_array)

test = array_to_adj(grid)

#node numbers of start and end
start = (20*136)+0
end = (20*136)+112

G = nx.from_numpy_array(test,create_using=nx.MultiDiGraph)
G.edges(data=True)
#nx.draw(G)

#p1
print(len(nx.shortest_path(G,start,end))-1)
#p2
#find all node numbers of "a"
starts = []
for row,row_value in enumerate(grid):
  for column,column_value in enumerate(row_value):
    if grid[row][column] == 97:
      starts.append((row*136)+column)
lens = []
for start_pos in starts:
  try:
    lens.append(len(nx.shortest_path(G,start_pos,end)))
  except:
    print("No path for node {}".format(start_pos))
lens.sort()
print(lens[0]-1)