#A ,B,C = map(int,input().split())
A = list(map(int,input().split()))

tof = False


medi = A[1]

A.sort()

if medi == A[1]:
  tof = True


if tof :
  print('Yes')

else :
  print('No')
