N ,A,B = map(int,input().split())

souwa = []

for i in range(N):
  souwa.append(i+1)

#print(souwa)

for i in range(N):
    if souwa[i] % A == 0 or souwa[i] % B == 0:
      souwa[i] = 0

#print(souwa)

print(sum(souwa))
