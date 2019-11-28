

def get_layer(matrix,n,a,b,c,d):
    layer=[]
    
    #column advance
    for x in matrix[a][a:b+1]:
        layer.append(x)

    #row advance
    for x in matrix[c+1:d]:
        layer.append(x[b])
        
    #column retrace
    for x in matrix[d-1][b-1:a:-1]:
        layer.append(x)

    #row retrace
    for x in matrix[d-1:c:-1]:
        layer.append(x[a])
    return layer

def set_layer(matrix,layer,a,b,c,d):
    y=0
    for x in range(a,b+1):
        matrix[a][x]=layer[y]
        y+=1
    for x in range(c+1,d):
        matrix[x][b]=layer[y]
        y+=1
    for x in range(b-1,a,-1):
        matrix[d-1][x]=layer[y]
        y+=1
    for x in range(d-1,a,-1):
        matrix[x][a]=layer[y]
        y+=1


def matrixRotation(matrix):

    x=len(matrix)
    y=len(matrix[0])
    if x%2==0:
        x/=2
    else:
        x=x//2+1
    if y%2==0:
        y/=2
    else:
        y=y//2+1

    print(x,y)
    
    layer_count=min(int(x),int(y))

    layers=[]
    a,b,c,d=0,len(matrix[0])-1,0,len(matrix)
    for x in matrix:
        print(x,'\n')

    print('-----------------------------')
    for x in range(1,layer_count+1):
        layer=get_layer(matrix,x,a,b,c,d)
        layers.append(layer)
        a+=1
        b-=1
        c+=1
        d-=1
    for x in range(0,3):
        for layer in layers:
            layer.append(layer.pop(0))

    l,m,n,o=0,len(matrix[0])-1,0,len(matrix)
    for x in layers:
        set_layer(matrix,x,l,m,n,o)
        l+=1
        m-=1
        n+=1
        o-=1    

