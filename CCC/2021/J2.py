# Silent Auction
N = int(input())
max_bid = -1  # intialize the answer, make sure this is small enough
for i in range(N):
  person = input()
  bid = int(input())
  if bid > max_bid:
    max_bid = bid
    max_person = person

print(max_person)
