N ,W = map(int,input().split())
A = list(map(int,input().split()))

flag = []
for _ in range(1, W+1):
    flag.append(0)


for i in range(N):
  if A[i] <= W:
    flag[A[i]-1] = 1
  if N > 1:
    for j in range(i+1,N):
      if A[i] + A[j] <= W:
        flag[A[i]+A[j]-1] = 1
      if N > 2:
        for k in range(j+1,N):
          if A[i] + A[j] + A[k] <= W:
            flag[A[i]+A[j]+A[k]-1] = 1

print(sum(flag))
