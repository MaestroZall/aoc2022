with open('C:\\Users\\misas\\Desktop\\aoc2022\day_8_data.txt', "r", encoding="utf-8") as f:
  data = f.read().splitlines()

forest = []
for line in data:
  tree_line = []
  for tree in line:
    tree_line.append(int(tree))
  forest.append(tree_line)

#p1
def check_visibility(row,column,forest):
  tree_size = forest[row][column]
  #outer check
  if column == 0 or row == 0 or column == len(forest) or row == len(forest):
    return(0)
  #left
  check = 0
  for i in range(0,column):
    if forest[row][i] >= tree_size:
      check = 1
  if check == 0:
    return(0)
  #right
  check = 0
  for i in range(column+1,len(forest)):
    if forest[row][i] >= tree_size:
      check = 1
  if check == 0:
    return(0)
  #top
  check = 0
  for i in range(0,row):
    if forest[i][column] >= tree_size:
      check = 1
  if check == 0:
    return(0)
  #down
  check = 0
  for i in range(row+1,len(forest)):
    if forest[i][column] >= tree_size:
      check = 1
  if check == 0:
    return(0)
  return(1)

result = 0
for column in range(len(forest)):
  for row in range(len(forest)):
    result += check_visibility(row,column,forest)
print((99*99)-result)

#p2
def check_scenic_score(row,column,forest):
  tree_size = forest[row][column]
  c_l,c_r,c_t,c_d = 0,0,0,0
  #left
  if column != 0:
    for i in range(column-1,-1,-1):
      c_l +=1
      if forest[row][i] >= tree_size:
        break
  #right
  if column != len(forest):
    for i in range(column+1,len(forest)):
      c_r +=1
      if forest[row][i] >= tree_size:
        break
  #top
  if row != 0:
    for i in range(row-1,-1,-1):
      c_t +=1
      if forest[i][column] >= tree_size:
        break
  #down
  if row != len(forest):
    for i in range(row+1,len(forest)):
      c_d +=1
      if forest[i][column] >= tree_size:
        break
  return(c_l*c_r*c_t*c_d)

result = []
for column in range(len(forest)):
  for row in range(len(forest)):
    #print(row,column,forest[row][column],check_scenic_score(row,column,forest))
    result.append(check_scenic_score(row,column,forest))
result.sort(reverse=True)
print(result[0])
