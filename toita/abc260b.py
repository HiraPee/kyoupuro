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


  n,x,y,z = Is_s()
  students = []
  a = A_list()
  b = A_list()

  for i in range(n):
    students.append([i+1,a[i],b[i],a[i]+b[i]] )

  ans = []



  students = sorted(students, reverse=True, key=lambda x: x[1])
  for i in range(x):
    ans.append(students[i])
  students = students[x:]
  students = sorted(students, reverse=False, key=lambda x: x[0])


  students = sorted(students, reverse=True, key=lambda x: x[2])
  for i in range(y):
    ans.append(students[i])

  students = students[y:]
  students = sorted(students, reverse=False, key=lambda x: x[0])

  #print(students)

  students = sorted(students, reverse=True, key=lambda x: x[3])
  #print(students)
  for i in range(z):
    ans.append(students[i])
  students = students[z:]

  ans = sorted(ans, reverse=False, key=lambda x: x[0])

  for i in range(len(ans)):
    print(ans[i][0])

if __name__ == '__main__' :
  main()
