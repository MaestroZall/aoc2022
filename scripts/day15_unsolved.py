
#x,y

#calculate distance between sensor and beacon

#calculate closest point in row 2000000
#distance - distance to closest point
#remaining distance +- y are the scanned points

#do this for each sensor
#sum of calculated points + beacons and sensors on 2000000


#combine result
test_r = [[15,25],[10,18],[27,80],[10,500]]
#desired outcome 10 + 5 + 53 = 68 

#convert to ranges, check if result if not append?
#might be too slow
'''
def calc_uniq_fields(list)-> int:
  result = []
  for item in list:
    for a in range(item[0],item[1]+1):
      if a not in result:
        result.append(a)
  print(result)
  return(len(result))

calc_uniq_fields(test_r)
'''

import re
with open(r'C:\Users\zalon\Downloads\aoc2022\day_15_data.txt', "r") as f:
  data = f.read().split("\n")
  for count,line in enumerate(data):
    data[count] = [int(x) for x in re.findall(pattern="\d+",string=line)]

def calc_checked_square(positions,line) ->list:
  #dist between beacon and sensor
  dist = abs(positions[0]-positions[2])+abs(positions[1]-positions[3])
  #make the dist smaller by dist between line and sensor
  #dist - Y of desired line - Y of sensor
  dist = dist-abs(line-positions[1])
  #the sensor does not reach desired row
  #print("Set of beacon and sensor {} scanned through coordinates {}".format(line,[positions[0]-dist,positions[0]+dist]))
  if dist<=0:
    return(None)
  print("Set of beacon and sensor {} scanned through coordinates {}".format(positions,[positions[0]-dist,positions[0]+dist]))
  #print([positions[0]-dist,positions[0]+dist])
  return([positions[0]-dist,positions[0]+dist])

result_ranges = []
for i in data:
  temp = calc_checked_square(i,2000000)
  if temp != None:
    result_ranges.append(temp)


#there is one beacon that we know of on 31358, 2000000

#create new list with ranges
#append 1st range
#from 2nd check for each range if it is either
# completely inside, smaller left, higher right
# skip, change left, change right
#if the range is completely separated
# add the new range

#expands upon first range
def create_ranges(range_list) -> list:
  #add first one
  final_ranges =[range_list[0]]
  for range in range_list[:-1]:
    inside_check = 0
    for count,f_range in enumerate(final_ranges):
      if range[0] <= f_range[0]:
        final_ranges[count][0] = range[0]
      if range[1] >= f_range[1]:
        final_ranges[count][1] = range[1]
      if range[0] > f_range[0] and range[1] < f_range[1]:
        inside_check = 1
    if inside_check == 0:
      final_ranges.append(range)
  return(final_ranges)

test = create_ranges(result_ranges)

#answer is too low
#[-106, 4424172]



#too low
#4424278
#too high
#4483204
#too low 
#4261288
#
result_temp = [[31358, 1930390],
 [2875490, 2957044],
 [2957044, 3652528],
 [31358, 60580],
 [2360568, 2934416],
 [-100, 31358],
 [31358, 485278],
 [624034, 2607242],
 [348822, 461044],
 [3235430, 4424172],
 [-106, 31358]]


res_str = ""
for item in result_temp:
  res_str = res_str+str(item[0])+"-"+str(item[1])+" "

test_str = "31358-1930390 2875490-2957044 2957044-3652528 31358-60580 2360568-2934416 0-31358 31358-485278 624034-2607242 348822-461044 3235430-4424172 0-31358"

def reduce(range_text):
  parts = range_text.split()
  if parts == []:
      return ''
  ranges = [ tuple(map(int, part.split('-'))) for part in parts ]
  ranges.sort()
  new_ranges = []
  left, right = ranges[0]
  for range in ranges[1:]:
      next_left, next_right = range
      if right + 1 < next_left:             # Is the next range to the right?
          new_ranges.append((left, right))  # Close the current range.
          left, right = range               # Start a new range.
      else:
          right = max(right, next_right)  # Extend the current range.
  new_ranges.append((left, right))  # Close the last range.
  return ' '.join([ '-'.join(map(str, range)) for range in new_ranges ])
print(reduce(test_str))