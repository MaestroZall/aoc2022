#day 7
import re
with open(r"C:\Users\zalon\Downloads\aoc2022\day_7_data.txt") as f:
  data = f.read().splitlines()

#test structure
test_tree = {
              "a":{
                "file.txt":500,
                "b":{
                  "image.png":250,
                  "c":{
                    "text.txt":125},
                  "image2.pnm":250}}}

#is not capable of saving results for every folder
def folder_size(folder):
  suma = 0
  for name,file in folder.items():
    if file.__class__ == dict:
      suma += folder_size(file)
    else:
      suma += file
  return(suma)
def tree_size(tree,folder_sizes):
  for name,file in tree.items():
    if file.__class__ == dict:
      folder_sizes[name] = folder_size(file)
      tree_size(file,folder_sizes)
  return(folder_sizes)

folder_sizes = {}
tree_size(test_tree,folder_sizes)

test_tree["a"]["b"]

#crazy loop
tree = {"/":{}}
key = "tree"
for line in data:
  if line[0] == "$":
    if line[2] == "l":
      continue
    #go back one step
    if line[5] ==".":
      key = re.search(pattern="(.*)(\[.*\])",string=key)[1]
    else:
      #check if dir exists in tree
      exists = 0
      dir_name = line[5:]
      for key_name in eval(key+".keys()"):
        if key_name == dir_name:
          exists = 1
          break
      if exists == 0:
        exec(key+"['"+line[4:]+"']={}")
      #change dir
      key = key+"['"+line[5:]+"']"
  #ls does nothing with this logic
  elif line[0] == "d":
    #directory, check if already exists, if not add it
    exists = 0
    dir_name = line[4:]
    for key_name in eval(key+".keys()"):
      if key_name == dir_name:
        exists = 1
        break
    if exists == 0:
      exec(key+"['"+line[4:]+"']={}")
  else:
    #this should be file
    temp = line.split(" ")
    temp_command = '[\'{}\'] = {}'.format(temp[1],temp[0])
    #exec
    exec(key+temp_command)


folder_sizes = {}
tree_size(tree,folder_sizes)

count = 0
for folder_size in folder_sizes.values():
  if folder_size < 100000:
    count += folder_size
print(count)
