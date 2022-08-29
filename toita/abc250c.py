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


  n,q = map(int,input().split())

  val = [x for x in range(n)]

  p = [x for x in range(n)]

  for i in range(q):
    query = I()

    p0 = p[query-1]
    p1 = p0

    if p0 != n-1 : p1 += 1
    else : p1 -= 1

    v0 = val[p0]
    v1 = val[p1]

    tv = val[p0]
    val[p0] = val[p1]
    val[p1] = tv

    tp = p[v0]
    p[v0] = p[v1]
    p[v1] = tp


  for i in val :
    print(i+1,end=" ")

  print()




if __name__ == '__main__' :
  main()
