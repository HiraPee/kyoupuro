s =  str(input())
t =  str(input())

import numpy as np

def rle(s):
    tmp, count, ans = s[0], 1, []
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans.append([tmp,count])
            tmp = s[i]
            count = 1
    ans.append([tmp,count])
    return ans



s_num = rle(s)
t_num = rle(t)

#print(s_num)
#print(len(t_num))


if len(s_num) != len(t_num):
  print('No')

else :
  for i in range(len(t_num)):
    if s_num[i][0] != t_num[i][0]:
      print('No')
      exit()
    if s_num[i][1] > t_num[i][1]:
      print('No')
      exit()
    if s_num[i][1] == 1 and t_num[i][1] > 1 :
      print('No')
      exit()


  print('Yes')
