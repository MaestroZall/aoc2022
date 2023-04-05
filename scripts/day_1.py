#part 1
with open(r'C:\Users\zalon\Downloads\aoc2022\day_1_data.txt', "r") as f:
  data = f.read().splitlines()

#initial values
elves = {}
num = 1
cal = 0
#get cal sums
for i in data:
  if i == '':
    elves[num] = cal
    num = num+1
    cal = 0
  else:
    cal = cal+int(i)
#return largest elf
#returns list of tuples
print(sorted(elves.items(), key=lambda item: item[1],reverse=True)[0][1])


#part two
print(sorted(elves.items(), key=lambda item: item[1],reverse=True)[0][1]+ 
sorted(elves.items(), key=lambda item: item[1],reverse=True)[1][1] +
sorted(elves.items(), key=lambda item: item[1],reverse=True)[2][1])
#the sorted method here is kind of too complicated
#i misread the task and thought initially that the solution was the number of elf
#not the calorie sum so thats why the "solution print" is so heavy weight