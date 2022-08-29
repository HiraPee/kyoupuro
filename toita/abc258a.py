k = int(input())


hour  =int(21 + k/60)

minitues = k%60
print(str(hour)+':'+str(minitues).zfill(2))
