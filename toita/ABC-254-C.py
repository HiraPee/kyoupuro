n,k = map(int,input().split())
A = list(map(int,input().split()))

sorted_list = sorted(A)
print(sorted_list)
tof = False

if A == sorted_list:
  tof = True
else :
  for i in range(n-k):
    print(A[i],A[i+k])
    if A[i] > A[i+k]:
      A[i],A[i+k] = A[i+k], A[i]

    #print(A)

    if A == sorted_list:
      tof = True
      break


if tof :
  print('Yes')
else :
  print('No')
