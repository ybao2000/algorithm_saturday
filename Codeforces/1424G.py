# G. Years
n = int(input())
years = []  # we need to list to store the tuples
for i in range(n):
  vals = input().split()
  years.append((int(vals[0], 1))) # 1 means birth
  years.append((int(vals[1], -1)))  # -1 means death
# we need to sort
# years.sort(key=lambda t: (t[0], t[1]))
years.sort()
max_population =0
population = 0
for year in years:
  if year[1] == -1: # -1 means death
    population -= 1
  else: # 1 means birth
    population += 1
    if population > max_population:
      max_population = population
      max_year = year[0]
print(max_year, max_population)
