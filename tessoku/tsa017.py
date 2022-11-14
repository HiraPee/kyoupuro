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


  n = I()
  A = i_list()
  B = i_list()

  dp = [0] * (n+1)

  dp[1] = 0
  dp[2] = A[0]

  for i in range(3,n+1):
    dp[i] = min(dp[i-1]+ A[i-2] ,dp[i-2]+B[i-3])

  #print(dp)

  place = n
  ans = []

  while True :
    ans.append(place)

    if place == 1 :
      break

    if dp[place -1] + A[place -2] == dp[place] :
      place -= 1
    else :
      place -= 2


  ans.reverse()

  print(len(ans))

  for a in ans :
    print(a,end=" ")



if __name__ == '__main__' :
  main()
