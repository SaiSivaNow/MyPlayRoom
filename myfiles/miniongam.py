def minion_game(string):
    # your code goes here
    lenstr = len(string)
    score_o = [0]
    score_c = [0]
    a = []
    for x in range(0,lenstr):
        for y in range(x+1,lenstr+1):
            sub = string[x:y]
            if sub not in a:
                find_score(string,y,x,lenstr,sub,score_o,score_c)
                a.append(sub)

    if score_c[0] > score_o[0]:
        print('Stuart',score_c[0])
    elif socre_c[0] < score_o[0]:
        print('Kevin',score_o[0])
    else:
        print('Draw')
            
def find_score(full,y,x,full_len,sub,score_o,score_c):
    sublen=y-x
    count = 0
    for x in range(0,full_len-sublen+1):
        if sub == full[x:x+sublen]:
            count+=1
    if sub[0] in 'AEIOU':
        score_o[0]+=count
    else:
        score_c[0]+=count

minion_game('BAANANAS')
