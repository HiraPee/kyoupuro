X ,A,D,N = map(int,input().split())

S =[]
count = 0

import math

def x_1plus(X ,count) :
  X += 1
  count += 1
  return X ,count

def x_1mainus(X ,count) :
  X -= 1
  count += 1
  return X ,count



for i in range(N):
  S.append(A)
  A += D

min_len = 999

while True :
  for s in S:
    if min_len > abs(X-s) :
      min_len = X-s

  print(X,X-min_len)
  if min_len == 0:
    break

  if min_len < 0 :
    min_len , count = x_1plus(min_len,count)
    if min_len == 0:
      break

  else :
    min_len , count = x_1mainus(min_len,count)
    if min_len == 0:
      break


print(count)
