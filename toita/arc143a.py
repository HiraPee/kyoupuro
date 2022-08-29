A,B,C = map(int,input().split())


abc_list = [A,B,C]
k = max(abc_list)

k_a = k - A
k_b = k - B
k_c = k - C



if k_a + k_b + k_c <= k:
  print(max(abc_list))

else :
  print(-1)
