def buildPalindrome(a, b):
    #
    # Write your code here.
    #
    
    lena = len(a)
    lenb = len(b)
    
    pal = {}
    
    maxlen = max(lena,lenb)
    
    for x in range(0,maxlen):
        
        if x < lena:
            if a[x] in pal.keys():
                pal[a[x]]+=1
            else:
                pal[a[x]]=1
        if x < lenb:
            if b[x] in pal.keys():
                pal[b[x]]+=1
            else:
                pal[b[x]]=1

    countdouble = 0;
    count = 0
    order = sorted(pal.keys())
    final = []
    minmiddle = 0
    y=0
    for x in order:
        y = pal[x]
        z = y//2
        for a in range(0,z):
            final.append(x)
        
        if y==1 and ord(x)<minmiddle:
            minmiddle = ord(pal[x])
    
    if len(final)==0:
        return "-1"
    
    finalstr = ''.join(final)
    finalstrrev = ''.join(reversed(final))

    print(minmiddle)
    
    return finalstr+chr(minmiddle)+finalstrrev


print(buildPalindrome('bac','bac'))
