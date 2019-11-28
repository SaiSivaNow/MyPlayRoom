def total_inc_dec(y):
    #your code here

    val_incre = {0:10,1:9,2:8,3:7,4:6,5:5,6:4,7:3,8:2,9:1}
    val_decre = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
    count = 10
    count = count_n_digit(count,val_incre,val_decre,2,y)
    print(count)


def count_n_digit(count,val_incre,val_decre,digits,total):
    const = int('1'*digits)
    prev_const = int('1'*(digits-1))
    curr_val_incre = [0]
    curr_val_decre = [0]
    print("Incre",val_incre)
    print("Decre",val_decre)
    for x in range(1,10):
        curr = const * x
        curr_div = prev_const*x
        curr_incre = val_incre[curr_div]
        curr_val_incre.append(curr_incre)
        count+=curr_incre
        curr_decre  = val_decre[curr_div]
        curr_val_decre.append(curr_decre)
        count+=curr_decre
    if digits == total:
        return count

    for x in range(1,10):
        curr = const * x
        total_decre = 0
        for i in range(1,x+1):
            total_decre+=curr_val_decre[i]
        val_decre[curr] = total_decre+x
        total_incre = 0
        for i in range(x,10):
            total_incre+=curr_val_incre[i]

        val_incre[curr] = total_incre        
    
    digits+=1
    return count_n_digit(count,val_incre,val_decre,digits,total)

        
    
total_inc_dec(4)
