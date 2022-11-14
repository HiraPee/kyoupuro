def main():
  import sys, operator, math
  if sys.implementation.name == 'pypy':
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=1')
  import math
  inf = 3074457345618258602
  sys.setrecursionlimit(2147483647)
  readline = sys.stdin.buffer.readline
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

  d = I()
  n = I()
  event = [0 ] *(d+1)

  for i in range(n):
    l,r = Is()
    event[l-1] += 1
    event[r] -= 1

  dp = [0]
  #print(event)

  for i in range(d+1):
    dp.append(event[i] + dp[i])

  #print(dp)

  for i in range(1,d+1):
    print(dp[i])


if __name__ == '__main__' :
  main()
