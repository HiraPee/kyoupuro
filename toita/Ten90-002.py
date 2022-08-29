N = int(input())

zentori = 2**N


def check(S):
  dep =0

  for i in range(len(S)):
    if S[i] == '(':
      dep += 1
    else : #S[i] == ')':
      dep -= 1
    if dep < 0:
      return False

  if dep == 0 :
    return True
  else :
    return False

for j in range(zentori,-1,-1):
  s = format(j,'b')
  #s = str(bin(j,'b'))
  #print(s)
  s = s.replace('1', '(').replace('0',')')
  if check(s) and len(s)== N:
    print(s)
