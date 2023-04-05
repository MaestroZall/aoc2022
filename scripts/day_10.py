#day10
with open(r'C:\Users\zalon\Downloads\aoc2022\day_10_data.txt', "r") as f:
  data = f.read().splitlines()

#[cycle len, value added]
def transform_move(line):
  if line[0] =="n":
    return([1,0])
  else:
    return([2,int(line.split()[1])])

instructions = []
for line in data:
  instructions.append(transform_move(line))

important_cicles = [20,60,100,140,180,220]
power = []
cycle = 1
value = 1
for instruction in instructions:
  for lenght in range(instruction[0]-1):
    cycle +=1
    if cycle in important_cicles:
      power.append(cycle*value)
    #print(cycle,value)
  cycle += 1
  value += instruction[1]
  #print(cycle,value)
  if cycle in important_cicles:
    power.append(cycle*value)

result = 0
for number in power:
  result += number
print(result)

#p2
screen = ""
cycle = 1
#fuckery with indexes
value = 2
for instruction in instructions:
  for lenght in range(instruction[0]-1):
    if abs(cycle-value)<=1:
      screen +=("#")
    else:
      screen +=(".")
    cycle +=1
  if abs(cycle-value)<=1:
    screen +=("#")
  else:
    screen +=(".")
  cycle += 1
  value += instruction[1]
  #return to start of row
  if cycle>39:
    cycle = cycle-40


print(screen[0:40])
print(screen[40:80])
print(screen[80:120])
print(screen[120:160])
print(screen[160:200])
print(screen[200:240])