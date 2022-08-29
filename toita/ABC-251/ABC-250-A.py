H ,W = map(int,input().split())
R ,C = map(int,input().split())

ans = 0

if  (R == 1) or (R == H) or (C ==1) or (C == W) :
  if (R==1) or (R ==H):
    if C == 1 or C == W :
      ans = 2
    else :
      ans = 3
  else:
    ans = 3
  if H == 1 or W == 1:
    ans = 1
  if H==1 and W ==1:
    ans =0

else :
  ans = 4

print(ans)
