A,B,C = map(int,input().split())

abc_list =[A,B,C]


ab = abs(A-B)
bc = abs(B-C)
ca = abs(C-A)

abc = ab + bc + ca


if abc % 2 == 0 or abc == 0:
  print(max(abc_list))

else :
  print(-1)
