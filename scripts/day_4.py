import functools
with open('C:\\Users\\zalon\\Desktop\\advent_of_code\\day_4_data.txt', "r") as f:
  data = f.read().splitlines()
  for i,e in enumerate(data):
    temp = [e.split('-') for e in e.split(',')]
    data[i] = {"a":int(temp[0][0]),"b":int(temp[0][1]),"c":int(temp[1][0]),"d":int(temp[1][1])}
#p1
def check_pair(row):
  if row["a"] <= row["c"] and row["b"] >= row["d"]:
    return(1)
  elif row["a"] >= row["c"] and row["b"] <= row["d"]:
    return(1)
  else:
    return(0)

result = 0
for row in data:
  result += check_pair(row)
print(result)

#p2
def check_pair_p2(row):
  if row["a"] <= row["c"] and row["b"] >= row["c"]:
    return(1)
  elif row["c"] <= row["a"] and row["d"] >= row["a"]:
    return(1)
  else:
    return(0)

result = 0
for row in data:
  result += check_pair_p2(row)
print(result)