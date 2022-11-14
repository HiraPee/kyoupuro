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
  from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
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

  masu = []

  for i in range(9):
    s = S()
    masu.append(s)

  ten = []

  for i in range(9):
    for j in range(9):
      if masu[i][j] == "#":
        ten.append([i+1,j+1])

  if len(ten) < 4:
    print(0)
    exit()

  #print(ten)

  ans = 0

  for i in range(len(ten)-3):
    for j in range(i+1,len(ten)-2):
      for k in range(j+1,len(ten)-1):
        for l in range(k+1,len(ten)):
          #print(i,j,k,l)
          d_i_j = (ten[i][0]-ten[j][0])**2 + (ten[i][1]-ten[j][1])**2
          d_i_k = (ten[i][0]-ten[k][0])**2 + (ten[i][1]-ten[k][1])**2
          d_i_l = (ten[i][0]-ten[l][0])**2 + (ten[i][1]-ten[l][1])**2
          d_j_k = (ten[j][0]-ten[k][0])**2 + (ten[j][1]-ten[k][1])**2
          d_j_l = (ten[j][0]-ten[l][0])**2 + (ten[j][1]-ten[l][1])**2
          d_k_l = (ten[k][0]-ten[l][0])**2 + (ten[k][1]-ten[l][1])**2

          kyori = set([d_i_j,d_i_k,d_i_l,d_j_k,d_j_l,d_k_l])
          if len(kyori) == 2 :
            kyori = sorted(list(kyori))
            if kyori[0] *2 == kyori[1]:
              ans += 1
  print(ans)


if __name__ == '__main__' :
  main()
