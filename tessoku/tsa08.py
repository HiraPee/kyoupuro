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

  h,w = Is_s()
  x = []

  for i in range(h):
    x.append(i_list())

  ruiseki = [[0 for _ in range(w+1)] for _ in range(h+1)]

  for i in range(h):
    res_sum = 0
    for j in range(w):
      res_sum += x[i][j]
      ruiseki[i][j] = res_sum

  for i in range(w):
    res_sum = 0
    for j in range(h):
      res_sum += ruiseki[j][i]
      ruiseki[j][i] = res_sum

  #print(ruiseki)

  q = I()

  for i in range(q):
    a,b,c,d = Is_s()
    a,b,c,d = a-1,b-1,c-1,d-1
    #print(a,b,c,d)
    #print(ruiseki[c][d],ruiseki[a][b],ruiseki[a][d],ruiseki[c][b])
    print(ruiseki[c][d]+ruiseki[a-1][b-1]-ruiseki[a-1][d]-ruiseki[c][b-1])


if __name__ == '__main__' :
  main()
