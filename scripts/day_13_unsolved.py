#day 13
with open('C:\\Users\\misas\\Desktop\\aoc2022\\day_13_test.txt', "r") as f:
  data = f.read().split("\n\n")
  for count,pair in enumerate(data):
    #this could be list compr oneliner propably
    data[count] = pair.split('\n')
    data[count][0] = eval(data[count][0])
    data[count][1] = eval(data[count][1])


#bud rovnou ano, rovnou ne, nebo je potreba dalsi
#1 correct, 0 incorrect, -1 potreba zavolat znovu
def comparer(l_item,r_item):
  if l_item.__class__ == int and r_item.__class__ == int:
    if l_item < r_item:
      return(1)
    elif l_item==r_item:
      return(-1)
    else:
      return(0)
  #if one is int and other list
  elif l_item.__class__ == int and r_item.__class__ == list:
    l_item = [l_item]
  elif l_item.__class__ == list and r_item.__class__ == int:
    r_item = [r_item]
  #this should be true all the time
  if l_item.__class__ == list and r_item.__class__ == list:
    for count,i in enumerate(l_item):
      if i==r_item[count]:
        continue
      elif i<r_item[count]:
        return(1)
      elif i>r_item[count]:
        return(0)
      elif count > len(r_item):
        return(1)
    return(-1)

#weird loop
for slice,pair in enumerate(data):
  for count,item in enumerate(pair[0]):
    #print("we are at slice: {} and {}".format(slice,count))
    step_result = comparer(item,pair[1][count])
    #print("Step result was {}".format(step_result))
    if step_result == 1:
      print(1)
      break
    elif step_result == 0:
      print(0)
      break
    #if we got at this point -1, right ran out before left
    elif step_result == -1 and count==(len(pair[0])-1):
      print(1)
      break
    elif step_result == -1 and count==(len(pair[1])-1):
      print(0)
      break


#basically everything ends at int vs int or right/left side runout

#if it is int vs do compare
#if it is list vs list do int vs int for each pair of items
#end once a!=b
#kdyz jen jedno je list, z druheho se udela taky list



a = [[[]]]
b = [[]]


a = [1,2,3,4]
b = [1,2,3,4,5]


#if (l_item.__class__==list and l_item[0].__class__==list) or
#(r_item.__class__==list and r_item[0].__class__==list):

#then we have empy list inside empty list