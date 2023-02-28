with open('26.txt')as f:
    s=[int(x) for x in f]
    s=sorted(s[1:], reverse=True)
    k=1,mini=s[0]


    for i in range(1,len(s)):
        if S[i]+3<=mini:
            mini=S[i]
            k+=1
print(k,mini)
