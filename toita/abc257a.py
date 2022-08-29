
N ,X = map(int,input().split())

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

new_abc = ''

for i in range(len(abc)):
  for j in range(N):
    new_abc += abc[i]

print(new_abc[int(X-1)])
