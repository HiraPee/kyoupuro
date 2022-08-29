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
  def A_list(): return list(map(int,input().split()))
  def Is_s(): return map(int,input().split())

  h_1,w_1 = Is_s()
  a_list = []

  for i in range(h_1):
    a_list.append(A_list())


  h_2,w_2 = Is_s()
  b_list = []

  def check(h,w):
    for i in range(h_2):
      for j in range(w_2):
        if a_list[h[i]][w[j]] != b_list[i][j] :
          return False
    return True

  for i in range(h_2):
    b_list.append(A_list())

  for i in combinations(list(range(h_1)),h_2):
    for j in combinations(list(range(w_1)),w_2):
      if check(i,j) :
        print('Yes')
        exit()
  print('No')

if __name__ == '__main__' :
  main()
