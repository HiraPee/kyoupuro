n ,k = map(int,input().split())
A = list(map(int,input().split()))

xy = []
for i in range(n):
  x, y = map(int,input().split())
  xy.append([x,y])

ans_list = []

for i in range(n):
  z = []
  for j in A :
    j -= 1
    dis = ((xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2 )
    z.append(dis)

  ans_list.append(min(z))

print(max(ans_list)**0.5)
