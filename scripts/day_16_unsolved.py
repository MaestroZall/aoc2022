import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#day 16
#day 12
import random
import re 
with open(r'C:\Users\zalon\Downloads\aoc2022day_16_data.txt', "r", encoding="utf-8") as f:
        # with open(Path(dirname(file)) / f"test_input.txt", "r", encoding="utf-8") as f:
    data = f.read().split('\n')
    #name of node, flow rate, list of adjacencies

#create graph
G = nx.MultiDiGraph()
for row in data:
  row_flow_rate = int(re.search(pattern="\d+",string=row)[0])
  row_name = re.findall(pattern=".*?([A-Z]{2})",string=row)[0]
  row_adj = []
  for item in re.findall(pattern=".*?([A-Z]{2})",string=row)[1:]:
    row_adj.append(item)
  G.add_node(row_name,flow_rate=row_flow_rate)
  for edge in row_adj:
    G.add_edge(row_name,edge)
labels = nx.get_node_attributes(G, 'flow_rate')     
nx.draw(G,labels=labels)
#vzdy hledame cesty z pozice kde zrovna jsme 
#do vsech pozic kde jeste neni otevreny valve
# (zbyvajici cas - cesta)*flow rate je priority func
# tohle asi nepocita uplne s otviranim shitu po ceste
# mozna to ale je dostacujici podminka

##declares
remaining_time = 30
current_flow_rate = 0
water_extracted = 0
current_position = "AA"
unopened_valves = nx.get_node_attributes(G,"flow_rate")
#for loop add all unopened valves with flow rate bigger than 0
for k in list(unopened_valves.keys()):
  if unopened_valves[k] == 0:
    del unopened_valves[k]
#check distance to all valves from current position 
distances = {}
if len(unopened_valves)>0:
  for key in unopened_valves:
    distances[key] =len(nx.shortest_path(G,current_position,key))-1
#calculate priority
priorities = {}
if len(unopened_valves)>0:
  for key in unopened_valves:
    priorities[key]= unopened_valves[key]*((remaining_time-distances[key])+1)
#the above +1 -1 is unneeded but logical, distance is one higher because it uses len and shows starting pos

#the logic above is kind of working but only with big enough depth
#calculate for example at least 3 moves at once
#this will result in 15*14*13 possible first moves
#p2 is impossible though