#day 7
import re
with open("C:\\Users\\zalon\\Desktop\\advent_of_code\\day_7_data.txt") as f:
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


#last key - list(my_dict)[-1]
#kdyz cd zmena key
#
#declare
tree = {}
key = 'tree[\'a\']'
for line in data:
  if line[5] ==".":
    #tady se regexem umaze posledni cast z key
    continue
  if line[0] == "$":
    if line[0][2] =="l":
      continue
    #pak to musi byt cd na dir
    else:
      key = key+"['"+line[4:]+"']"
  #pak to musi byt soubor, nebo slozka
  else:
    if line[0] == "d":
      #prida slozku
      temp = line.split(" ")
      temp_command = '[\'{}\'] = {}'.format(temp[1])
      #snad to neodmrda content ty puvodni slozky
      exec(key+temp_command)
    else:
      #soubor
      temp = line.split(" ")
      temp_command = '[\'{}\'] = ({})'.format(temp[1],temp[0])
      exec(key+temp_command)
#somewhat skoro funkcni, ale ne

test_tree["a"]["b"]



#logika
tree = {}
key = "tree"
#kdyz bude line $ cd abc
line = "$ cd /"
key = key+"['"+line[5:]+"']"
#kdyz bude line $ cd ..
line = "$ cd .."
key = re.search(pattern="(.*)(\[.*\])",string=key)[1]
#kdyz bude line slozka
#je treba zjistit jestli existuje na tehle urovni
#pokud ne tak se prida
key = "test_tree['a']"
line = "dir b"
exists = 0
dir_name = line[4:]
for key_name in eval(key+".keys()"):
  if key_name == dir_name:
    exists = 1
    break
#pokud neexistuje pridej
if exists == 0:
  key+"['"+line[4:]+"']={}"
#kdyz je line soubor
line = "63532 mwvbpw.mmg"
temp = line.split(" ")
temp_command = '[\'{}\'] = {}'.format(temp[1],temp[0])
#exec
exec(key+temp_command)

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