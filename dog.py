cn=int(input())
daa=list(map(int,input().split(" ")))
daa=[bin(i) for i in daa]
daa.sort(reverse=True)
daa=[int(cn,2) for cn in daa]
for i in range(0,cn):
     print(daa[i])
