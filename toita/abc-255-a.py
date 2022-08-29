r ,c = map(int,input().split())

a_1_1, a_1_2 = input().split()
a_2_1, a_2_2 = input().split()

if r == 1 :
  if c == 1:
    print(a_1_1)

  else :
    print(a_1_2)

else :
  if c == 1:
    print(a_2_1)

  else :
    print(a_2_2)
