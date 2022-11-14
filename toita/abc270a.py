def main():
  import sys, operator, math
  if sys.implementation.name == 'pypy':
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=1')
  from math import gcd, floor, ceil, sqrt, isclose, pi, sin, cos, tan, asin, acos, atan, atan2, hypot, degrees, radians, log, log2, log10
  from array import array
  from collections import deque, Counter as counter, defaultdict as ddict
  from bisect import bisect_left, bisect_right
  from heapq import heappush, heappop, heapify, heappushpop, heapreplace as heappoppush, nlargest, nsmallest
  from functools import lru_cache, reduce
  from itertools import count, cycle, accumulate, chain, groupby, islice, product, permutations, combinations, combinations_with_replacement
  from operator import itemgetter
  import math
  inf = 3074457345618258602
  sys.setrecursionlimit(2147483647)
  readline = sys.stdin.buffer.readline
  cache = lru_cache(None)
  def input(): return readline().rstrip().decode()
  def S(): return readline().rstrip().decode()
  def Ss(): return readline().rstrip().decode().split(' ')
  def I(): return int(readline())
  def I1(): return int(readline()) - 1
  def Is(): return [int(i) for i in readline().rstrip().split(b' ')]
  def I1s(): return [int(i) - 1 for i in readline().rstrip().split(b' ')]
  def F(): return float(readline())
  def Fs(): return [float(i) for i in readline().rstrip().split(b' ')]
  def i_list(): return list(map(int,input().split()))
  def Is_s(): return map(int,input().split())


  a,b = Is_s()

  if a == 6 :
    a = [2,4]
  elif a == 5:
    a = [1,4]

  elif a == 3:
    a = [1,2]

  else :
    a = [a]

  if b == 6 :
    b =  [2,4]
  elif b == 5:
    b = [1,4]

  elif b == 3:
    b = [1,2]

  else :
    b = [b]

  num = {}

  for i in range(len(a)):
    if a[i] in num :
      num[a[i]] += 1
    else :
      if a[i] == 0:
        continue
      num[a[i]] = 1

  for i in range(len(b)):
    if b[i] in num :
      num[b[i]] += 1
    else :
      if b[i] == 0 :
        continue
      num[b[i]] = 1

  #print(num)


  ans = 0

  for value in num.keys():
    ans += int(value)

  print(ans)




if __name__ == '__main__' :
  main()
