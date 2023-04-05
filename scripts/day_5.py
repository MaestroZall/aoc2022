#day 5 better
#day5
import re 
with open(r'C:\Users\zalon\Downloads\aoc2022\day_5_data.txt', "r") as f:
  data = f.read().splitlines()

#warehouse
warehouse_data = data[0:8]
warehouse = {}
for i in range(1,10):
  warehouse[i] = []
for row in warehouse_data:
  stack = 1
  for i in range(1,35,4):
    if row[i] != " ":
      warehouse[stack].append(row[i])
    stack +=1
#reverse stacks
for i in warehouse.values():
  i.reverse()
#instrukce
instructions_data = data[10:]
instructions = []
for row in instructions_data:
  temp_row = row.split()
  instructions.append([int(temp_row[1]),int(temp_row[3]),int(temp_row[5])])

#p1
def crane(warehouse_f,instructions_f):
  for n_crates,f_from,f_to in instructions_f:
    for i in range(n_crates):
      warehouse_f[f_to].append(warehouse_f[f_from].pop())
  for i in range(1,10):
    print(warehouse_f[i][0],end="")

crane(warehouse,instructions)
#to separate both parts
print("")

#p2
def crane9001(warehouse_f,instructions_f):
  for n_crates,f_from,f_to in instructions_f:
    warehouse_f[f_to] += warehouse_f[f_from][-n_crates:]
    del warehouse_f[f_from][-n_crates:]
  for i in range(1,10):
    print(warehouse_f[i][0],end="")

crane9001(warehouse,instructions)