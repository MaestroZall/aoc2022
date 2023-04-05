#day6
with open('C:\\Users\\misas\\Desktop\\aoc2022\day_6_data.txt', "r") as f:
  data = f.read()
#fun
def check_string(string):
  unique = []
  for x in [*string]:
    if x not in unique:
      unique.append(x)
  return(len(unique))
#p1
for i in range(4,len(data)):
  if check_string(data[i-4:i])==4:
    print(i)
    break
#p2
for i in range(14,len(data)):
  if check_string(data[i-14:i])==14:
    print(i)
    break
