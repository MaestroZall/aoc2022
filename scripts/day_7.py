#day 7


#asi dicty v dictech
#slozka item v dictu, soubor taky item v dictu 
#value souboru je velikost
#value dictu jsou dalsi soubory

#a obsahuje dict b ktery obsahuje soubor ls.txt o velikosti 500
test_d = {"a":{"b":{"ls.txt":500,"c":{"image.png":1000}},"document.txt":250}}
#jak dostat velikosti slozek?
#

#udelame dalsi list
#key jmeno slozky value hodnota vsech souboru uvnitr
#jde pres celej strom, kdy
for value in test_d[].values():

  print(value)

#funkce co spocita obsah slozky
#kdyz najde slozku zavola zas sebe rekurze
check_content(folder):
  size = {folder.key():0}
  for folder_name,file in folder.items():
    if file.__class__ == dict:
      sub_folder = check_content([folder_name])
      size[folder.key()] += sub_folder.value()
    else:
      size[folder.key()] += file

