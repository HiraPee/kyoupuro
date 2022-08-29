N = int(input())
A = []
max_num = -1
max_index = []

for i in range(N):
  list_num = str(input())
  nums = []
  for j in range(len(list_num)):
    nums.append(list_num[j])
    if max_num < int(list_num[j]):
      max_num = int(list_num[j])
      max_index = [i,j]
  A.append(nums)


XY = [ [-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
max_num = -1
cand_list = []
'''
for x,y in XY:
  i,j = max_index
  search_num = int(A[i][j])
  for k in range(N-1):
    #print(i+1,j+1)
    i = (i + x) % N
    j = (j + y) % N
    search_num *= 10
    search_num += int(A[i][j])
  cand_list.append(search_num)'''


for i in range(N):
  for j in range(N):
    for x,y in XY:
      search_num = int(A[i][j])
      for k in range(N-1):
        #print(i+1,j+1)
        i = (i + x) % N
        j = (j + y) % N
        search_num *= 10
        search_num += int(A[i][j])
      cand_list.append(search_num)





print(max(cand_list))
