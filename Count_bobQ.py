n=len(s)
i=0
cnt=0
while i<n-2:
    sub=s[i:i+3]
    if sub == 'bob':
        cnt+=1
    i+=1

print('Number of times bob occurs is:',cnt)
