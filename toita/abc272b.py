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

  n,m = Is_s()

  budoukai = []

  for i in range(m):
    km = i_list()
    m = km[1:]

    budoukai.append(m)

    num_list = []

    for i in range(n):
      num_list.append([])
      for j in range(n):
        if i==j :
          num_list[i].append(True)
        else :
          num_list[i].append(False)

  for i in range(len(budoukai)):
    for j in range(len(budoukai[i])-1):
      for k in range(j+1,len(budoukai[i])):
        num_list[budoukai[i][j]-1][budoukai[i][k]-1] = True
        num_list[budoukai[i][k]-1][budoukai[i][j]-1] = True

  for i in range(n):
    if False in num_list[i] :
      print('No')
      exit()


  print('Yes')

if __name__ == '__main__' :
  main()
