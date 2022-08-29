'''sums = []


for i in range(50001):
  if  '3' in str(i) or i % 3==0:
    print(i)
    sums.append(i)


print(sum(sums))'''




'''sums = []
i=0


while sum(sums) < 10:
  i += 1
  sums.append(1/i)
  print(1/i)


print(len(sums))'''

'''
money_list =[]

for i in range(10331):
  money_list.append(0)

biggest = -1


for i in range(31):
  for j in range(41):
    for k in range(31):
      money_list[i*205+j*82+k*30] = 1
      if biggest < i*205+j*82+k*30:
        biggest = i*205+j*82+k*30

#print(biggest)
#print(money_list)
target = 0

print(len([item for item in money_list if item != target]-1))
#print(len(money_list.remove(0)))'''

w = 3
h = 4
i = 1
mylist = [0 for i in range(8193)]
print(mylist)

while (w*h)/2 <= 8192:
  w *= i
  h *= i
  mylist[int(w*h/2)] = 1

  i += 1


print(len(mylist))
