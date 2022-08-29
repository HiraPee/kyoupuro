N ,K,Q = map(int,input().split())
A = list(map(int,input().split()))

L = list(map(int,input().split()))


masu = [0 for i in range(N)]


for a in A:
  masu[a-1] = 1


for l in L:
  count = 0
  for i in range(N):
    if masu[i] == 1:
      count += 1
      if count == l:
        if i == N-1:
          continue
        else :
          if masu[i+1] == 1:
            continue
          else :
            masu[i] = 0
            masu[i+1] = 1

ans = ''

for i in range(N):
  if masu[i] == 1:
    ans += str(i+1) +' '


print(ans)
