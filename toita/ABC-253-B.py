H ,W = map(int,input().split())
S = []
for i in range(H):
  s = input()
  S.append(s)

f_count_H , f_count_W = -1,-1
l_count_H , l_count_W =  -1,-1
ans = None
f_frag = False

moji = 'o'

for i in range(len(S)):
  if moji in S[i]:

    #print(S[i].count(moji))
    if S[i].count(moji) == 2 :
      first,second = -1,-1
      target = S[i]
      for j in range(len(target)):
        if target[j] == moji and first >= 0:
          second = j

        if target[j] == moji and first < 0 :
          first = j
      #print(first,second)
      ans = second - first

    if (l_count_H <= 0 and l_count_W <= 0 ) and f_count_H >= 0 and f_count_W >= 0 :
       l_count_H = S[i].find(moji)
       l_count_W = i

    if f_count_H <= 0 and f_count_W <= 0 :
      f_count_H = S[i].find(moji)
      f_count_W = i

#print(f_count_H,f_count_W)
#print(l_count_H,l_count_W)

if ans == None:
  print(  abs(f_count_H - l_count_H) + abs(f_count_W - l_count_W) )
else :
  print(ans)
