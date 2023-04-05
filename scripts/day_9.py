#day9
with open('C:\\Users\\misas\\Desktop\\aoc2022\\day_9_data.txt', "r") as f:
  data = f.read().splitlines()

def transform_move(line):
  return([line[0],int(line[2:])])
instructions = []
for line in data:
  instructions.append(transform_move(line))

head = [200,200]
tail = [200,200]
#visited positions
visited = []
for instruction in instructions:
  for step in range(instruction[1]):
    if instruction[0] == "L":
      head[0] -= 1
    elif instruction[0] == "R":
      head[0] += 1
    elif instruction[0] == "U":
      head[1] += 1
    elif instruction[0] == "D":
      head[1] -= 1
    #check for linear movement
    if tail[0] == head[0] or tail[1]==head[1]:
      if abs(head[0]-tail[0])==2:
        if head[0]>tail[0]:
          tail[0]+=1
        else:
          tail[0]-=1
      elif abs(head[1]-tail[1])==2:
        if head[1]>tail[1]:
          tail[1]+=1
        else:
          tail[1]-=1
    #check for diagonal movement
    elif abs(head[0]-tail[0])==2:
        if head[0]>tail[0]:
          tail[0]+=1
        else:
          tail[0]-=1
        #now move in second direction
        if head[1] > tail[1]:
          tail[1] +=1
        else:
          tail[1] -=1
    elif abs(head[1]-tail[1])==2:
        if head[1]>tail[1]:
          tail[1]+=1
        else:
          tail[1]-=1
        if head[0] > tail[0]:
          tail[0] +=1
        else:
          tail[0] -=1  
    visited.append(tail[:])

unique = 0
unique_list = []
for item in visited:
  if item not in unique_list:
    unique +=1
    unique_list.append(item)
print(unique)

#part2
#input head and tail, returns adjusted tail
def check_move(head,tail):
  if tail[0] == head[0] or tail[1]==head[1]:
    if abs(head[0]-tail[0])==2:
      if head[0]>tail[0]:
        tail[0]+=1
      else:
        tail[0]-=1
    elif abs(head[1]-tail[1])==2:
      if head[1]>tail[1]:
        tail[1]+=1
      else:
        tail[1]-=1
  #check for diagonal movement
  elif abs(head[0]-tail[0])==2:
      if head[0]>tail[0]:
        tail[0]+=1
      else:
        tail[0]-=1
      #now move in second direction
      if head[1] > tail[1]:
        tail[1] +=1
      else:
        tail[1] -=1
  elif abs(head[1]-tail[1])==2:
      if head[1]>tail[1]:
        tail[1]+=1
      else:
        tail[1]-=1
      if head[0] > tail[0]:
        tail[0] +=1
      else:
        tail[0] -=1 
  return(tail)

#movement
visited = []
head = [200,200]
k_1,k_2,k_3,k_4,k_5,k_6,k_7,k_8,k_9 = [200,200],[200,200],[200,200],[200,200],[200,200],[200,200],[200,200],[200,200],[200,200]
#visited positions
visited = []
for instruction in instructions:
  for step in range(instruction[1]):
    if instruction[0] == "L":
      head[0] -= 1
    elif instruction[0] == "R":
      head[0] += 1
    elif instruction[0] == "U":
      head[1] += 1
    elif instruction[0] == "D":
      head[1] -= 1
    k_1 = check_move(head,k_1)
    k_2 = check_move(k_1,k_2)
    k_3 = check_move(k_2,k_3)
    k_4 = check_move(k_3,k_4)
    k_5 = check_move(k_4,k_5)
    k_6 = check_move(k_5,k_6)
    k_7 = check_move(k_6,k_7)
    k_8 = check_move(k_7,k_8)
    k_9 = check_move(k_8,k_9)
    visited.append(k_9[:])

unique = 0
unique_list = []
for item in visited:
  if item not in unique_list:
    unique +=1
    unique_list.append(item)
print(unique)