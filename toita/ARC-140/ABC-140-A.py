N ,K = map(int,input().split())
S = [a for a in str(input())]






if K >= N-1 :
  print(1)
elif K == 0 :
  S = list(set(S))
  print(len(S))

else:

  syurui = list(set(S))
  minNum = len(syurui)

  for k in range(K):



  S = list(set(S))
  print(len(S))
