#part 1
with open(r"C:\Users\zalon\Downloads\aoc2022\day_2_data.txt", "r") as f:
  data = f.read().splitlines()
#data[i][0] is oponnent data[i][2] is us

# A rock, B paper, C scissors
# X rock, Y paper, Z scissors
#1,2,3 points for type
#0,3,6 for win cond

#def function to calculate score of round
def rps_score(strategy):
  result = 0
  #return score according to type
  if strategy[2]=="X":
    result = result+1
  elif strategy[2]=="Y":
    result = result+2
  else:
    result = result+3
  #return score according to win/lose
  if (strategy[2]=="X" and strategy[0]=="A") or (strategy[2]=="Y" and strategy[0]=="B") or (strategy[2]=="Z" and strategy[0]=="C"):
    return(result+3)
  elif (strategy[2]=="X" and strategy[0]=="C") or (strategy[2]=="Y" and strategy[0]=="A") or (strategy[2]=="Z" and strategy[0]=="B"):
    return(result+6)
  else:
    return(result)

#loop it over data and sum the result
final_points = 0
for i in data:
  final_points = final_points+rps_score(i)
print("Part one {}.".format(final_points))

#part 2
# A rock, B paper, C scissors
# X is lose, Y is draw, Z is win
point_dict = {"A X": 3, "B X": 1, "C X":2,
              "A Y":4, "B Y":5, "C Y":6,
              "A Z":8, "B Z":9, "C Z":7}
result_p2 = 0 
for i in data:
  result_p2 = result_p2+point_dict[i]
print("Part two {}.".format(result_p2))
#in retrospective the first part could have been defined as dict as well

