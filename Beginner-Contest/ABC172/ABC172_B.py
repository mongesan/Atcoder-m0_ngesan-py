S=str(input())
T=str(input())
cnt=0
for i in range(len(S)):
    if S[i]!=T[i]:
        cnt+=1
print(cnt)