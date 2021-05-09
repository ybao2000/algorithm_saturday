# Winner
n = int(input())
rounds = []
dict_player = {}
for i in range(n):
  vals = input().split()
  player = vals[0]
  score = int(vals[1])
  rounds.append((player, score))
  if player not in dict_player:
    dict_player[player] = score
  else:
    dict_player[player] += score
  # dict_player[player] = score if player not in dict_player else dict_player[player] + score

# we need to find the max score, list winner
score_max = max(dict_player.values())
list_winner = [p for p, s in dict_player.items() if s == score_max ]

if len(list_winner) == 1:
  print(list_winner[0])
else:
  dict_player = {}
  for round in rounds:
    player = round[0]
    score = round[1]
    if player not in list_winner:
      continue
    if player not in dict_player:
      score_total = score
    else:
      score_total = dict_player[player] + score
    if score_total >= score_max:
      print(player)
      break
    dict_player[player] = score_total
  
