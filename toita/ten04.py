h ,w = map(int,input().split())
a ,b, c ,ans= [],[],[],[]
for i in range(h):
  a_append =list(map(int,input().split()))
  a.append(a_append)


#print(a)

for i in range(h):
  b.append(sum(a[i]))

for i in range(w):
  c.append(sum(c[0][i]))


print(a)
print()
print(b)
print()
print(c)

for i in range(h):
  ans.append(b[i]+c[0]-a[i])



for i in range(h):
  for j in range(w):
    print(ans[i][j], end=' ')
  print()
