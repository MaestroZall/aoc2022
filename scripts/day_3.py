with open(r'C:\Users\zalon\Downloads\aoc2022\day_3_data.txt', "r") as f:
  data = f.read().splitlines()

def wrong_item(rucksack):
  for l_item in rucksack[(len(rucksack)//2):]:
    for r_item in rucksack[:(len(rucksack)//2)]:
      if l_item == r_item:
        if ord(l_item)>96:
          return(ord(l_item)-96)  
        else:
          return(ord(l_item)-38)

result = 0
for a in data:
  result += wrong_item(a)

print(result)

#return common item between every set of three lines
def return_badge(rucksacks):
  for rucksack_1 in rucksacks[0]:
    for rucksack_2 in rucksacks[1]:
      for rucksack_3 in rucksacks[2]:
        if rucksack_1 == rucksack_2 == rucksack_3:
          if ord(rucksack_1)>96:
            return(ord(rucksack_1)-96)
          else:
            return(ord(rucksack_1)-38)          

result_p2 = 0
for a in range(0,len(data),3):
  result_p2 += return_badge([data[a],data[a+1],data[a+2]])

print(result_p2)
#now this is very unoptimized solution, hashmaps/sets would be optimized solution