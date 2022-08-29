n = int(input())
A = list(map(int,input().split()))

hantei_list =[]

count = 0



def has_duplicates(seq):
    return len(seq) != len(set(seq))


for i in range(len(A)-2):
  j = i +1
  for j in range(j,len(A)-1):
    k = j + 1
    for k in range(k,len(A)):
      hantei_list =[A[i],A[j],A[k]]
      if not has_duplicates(hantei_list):
        count += 1


print(count)
