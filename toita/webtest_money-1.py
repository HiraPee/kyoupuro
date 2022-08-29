import sys
S = str(input())

#Black -1  White 1
reverci = [-1,1]
turn = -1

for i in range(len(S)):
    #追加方向
    if S[i] == 'R':
        reverci.append(turn)

        if reverci[0] ==turn and reverci[len(reverci)-1]== turn:
            for j in range(len(reverci)):
                reverci[j] = turn

        turn *= -1
    else :
        reverci.insert(0,turn)

        if reverci[0] ==turn and reverci[len(reverci)-1]== turn:
            for j in range(len(reverci)):
                reverci[j] = turn
        turn *= -1
print(reverci.count(-1),reverci.count(1))
