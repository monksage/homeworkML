k = int(input())

combidict = dict()
for i in range(1,k+1):
    curnum = int(input())
    combidict[i] = dict()
    j = i
    while j <= k:
        combidict[i][j] = 0
        for d in combidict.values():
            d[j] += curnum
        j+=1

p = int(input())
q = int(input())

print(combidict[p][q])

# не понял что от меня требуется


    

