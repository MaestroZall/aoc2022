with open(r'C:\Users\zalon\Downloads\aoc2022\day_11_data.txt', "r") as f:
  data = f.read().splitlines()
import re

Monkeys = []
for i in range(1,len(data),7):
  Monkeys.append({
    "Items":[int(x) for x in re.findall(string=data[i],pattern="\d+")],
    "Formula":re.findall(string=data[i+1],pattern="=.*")[0],
    "Test":int(re.findall(string=data[i+2],pattern="\d+")[0]),
    "True":int(re.findall(string=data[i+3],pattern="\d+")[0]),
    "False":int(re.findall(string=data[i+4],pattern="\d+")[0]),
    "Inspection_count":0})
#game loop
for i in range(20):
  for j in range(len(Monkeys)):
    for count,old in enumerate(Monkeys[j]["Items"]):
      exec("Monkeys[j]['Items'][count]{}".format(Monkeys[j]["Formula"]))
      Monkeys[j]['Items'][count]=Monkeys[j]['Items'][count]//3
      if (Monkeys[j]['Items'][count]%Monkeys[j]["Test"])==0:
        Monkeys[Monkeys[j]["True"]]["Items"].append(Monkeys[j]['Items'][count])
      else:
        Monkeys[Monkeys[j]["False"]]["Items"].append(Monkeys[j]['Items'][count])
      Monkeys[j]["Inspection_count"] += 1
    Monkeys[j]["Items"] = []

Monkey_power= []
for monkey in Monkeys:
  Monkey_power.append(monkey["Inspection_count"])
Monkey_power.sort(reverse=True)
print(Monkey_power[0]*Monkey_power[1])

#magic number
magic_number = 1
for monkey in Monkeys:
  magic_number = magic_number*monkey["Test"]
#p2
for i in range(10000):
  for j in range(len(Monkeys)):
    for count,old in enumerate(Monkeys[j]["Items"]):
      exec("Monkeys[j]['Items'][count]{}".format(Monkeys[j]["Formula"]))
      if (Monkeys[j]['Items'][count]%Monkeys[j]["Test"])==0:
        if Monkeys[j]['Items'][count]-magic_number>0:
          Monkeys[j]['Items'][count] = Monkeys[j]['Items'][count]%magic_number
        Monkeys[Monkeys[j]["True"]]["Items"].append(Monkeys[j]['Items'][count])
      else:
        if Monkeys[j]['Items'][count]-magic_number>0:
          Monkeys[j]['Items'][count] = Monkeys[j]['Items'][count]%magic_number
        Monkeys[Monkeys[j]["False"]]["Items"].append(Monkeys[j]['Items'][count])
      #new worry system, divide by test criterion then
      Monkeys[j]["Inspection_count"] += 1
    #pop all monkey items
    #popping them during loop could create issue with count
    Monkeys[j]["Items"] = []

for monkey in Monkeys:
  print(monkey["Inspection_count"]) 