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

  s = S()

  pins = [[[7,False]],[[4,False]],[[2,False],[8,False]],[[1,False],[5,False]],[[3,False],[9,False]],[[6,False]],[[10,False]]]
  split = [False for i in range(len(pins))]

  if s[0] == '0':
    for i in range(10):
      if s[i] == '0':
        for j in range(len(pins)):
          for k in range(len(pins[j])):
            if pins[j][k][0] == i+1:
              split[j] = True
              pins[j][k][1] = True

    #print(pins)
    #print(split)
    for i in range(len(pins)):
      for j in range(i+1,len(pins)):
        if ( i+1 != j) and not (True in pins[i+1:j])  and split[i] == False and split[j] == False:
          for k in range(len(pins[i+1:j])):
            for l in range(len(pins[i+1:j][k])):
              if pins[i+1:j][k][l][1] == False:
                break
              elif len(pins[i+1:j][k]) == l+1 :
                print('Yes')
                exit()

    print('No')

  else :
    print('No')





if __name__ == '__main__' :
  main()
