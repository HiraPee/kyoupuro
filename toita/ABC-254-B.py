N = int(input())

pre_List = []
for i in range(N+1):
  pre_List.append(0)
#now_List = []


for i in range(1,N+1):
  now_List = []
  #print(now_List)

  for j in range(i):
    if j==0 or j == i :
      now_List.append(1)
    else :
      ans = pre_List[j-1] + pre_List[j]
      now_List.append(ans)

  L=[str(a) for a in now_List]
  L=' '.join(L)
  print(L)
  #print(now_List)

  for k in range(i):
    pre_List[k] = now_List[k]
