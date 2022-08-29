N = int(input())
S = str(input())
W = list(map(int,input().split()))



heavy = max(W)


max_count = -1

for X in range(0,heavy*2,5):
  moji = ''
  for i in range(N):
    if W[i] < X :
      moji += '0'
    else :
      moji += '1'

  count = 0
  for i in range(len(S)):
    if moji[i] == S[i]:
      count += 1
  if max_count < count:
    max_count = count


print(max_count)
