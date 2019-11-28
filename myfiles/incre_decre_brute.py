def total_inc_dec(y):
    #your code here
    is_prev_incre = False

    is_prev_decre = False

    is_prev_bouncy = True

    prev_incre_digit = 11

    prev_decre_digit = 11

    count = [0]

    total = 10**5

    bounce_count = 0
    for x in range(200,300):

        if is_prev_bouncy:            
            is_prev_incre,is_prev_decre,is_prev_bouncy = find_order(str(x),count)
            if x == 201:
                print(is_prev_incre,is_prev_decre,is_prev_bouncy)
            if is_prev_incre or is_prev_decre:
                print(x)
                count[0]+=1
        elif is_prev_incre:
            number = str(x)
            curr_dig = int(number[len(number)-1])
            if curr_dig >= prev_incre_digit:
                prev_incre_digit = curr_dig
                print(x)
                count[0]+=1
            else:
                is_prev_incre,is_prev_decre,is_prev_bouncy = find_order(str(x),count)
                if is_prev_incre or is_prev_decre:
                    print(x)
                    count[0]+=1
        else:
            number = str(x)
            curr_dig = int(number[len(number)-1])
            if curr_dig <= prev_decre_digit:
                if len(number) < 2:
                    prev_decre_digit = curr_dig
                else:
                    prev_decre_digit = int(number[len(number)-2])
                print(x)
                count[0]+=1
            else:
                is_prev_incre,is_prev_decre,is_prev_bouncy = find_order(str(x),count)
                if is_prev_incre or is_prev_decre:
                    print(x)
                    count[0]+=1
    return count[0]
        
    
def find_order(number,count):    
    prev = number[len(number)-1]

    incre = True
    decre =  True
    bouncy = True

    for x in range(len(number)-2,-1,-1):
         
        curr = int(number[x])
        if curr < int(prev) and incre:
            incre = True
            decre = False
            bouncy = False
            prev = curr
        elif curr > int(prev) and decre:
            decre = True
            incre = False
            bouncy = False
            prev = curr
        elif curr == int(prev):
            decre = decre
            incre = incre
            bouncy = False
            prev = curr
        else:
            bouncy = True
            incre = False
            decre = False
            return [incre,decre,bouncy]
        
    if len(number) ==1:
        incre = True
        decre = False
        bouncy = False
    return [incre,decre,bouncy]
print(total_inc_dec(35))
