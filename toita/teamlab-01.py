toribonatti =[1,0,5]



for i in range(3,29):
  toribonatti.append(toribonatti[i-3]+toribonatti[i-2]+toribonatti[i-1])

print(len(toribonatti))

print(toribonatti[27])

sums =[]
yakusare = 1234567890


for i in range(1,yakusare+1):
  if  yakusare % i ==0:
    if i > 20000000 :
      break
    sums.append(i)

print(sum(sums))
