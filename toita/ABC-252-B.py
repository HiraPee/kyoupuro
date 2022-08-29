n,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ToF_list = []

ToF = False

max_num = max(A)

for i in range(len(B)):
  if max_num == A[B[i]-1]:
    ToF = True

if ToF :
  print('Yes')
else :
  print('No')
