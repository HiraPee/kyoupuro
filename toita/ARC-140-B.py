N  = int(input())
S = str(input())
count = 0
for i in range(1,int(N/2)) :
  if 'AARCC' in S and i % 2 ==1 :
    num = S.count('AARCC')
    S = S.replace('ARC', '',)
    count = 2 * num
  elif 'ARC' in S :
    if i % 2 == 0:
      S = S.replace('ARC', 'AC',1)
      count += 1
    else :
      S = S.replace('ARC', 'R',1)
      count += 1
  else :
    break
print(count)
