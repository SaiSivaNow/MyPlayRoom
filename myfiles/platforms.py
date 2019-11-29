


def count_platforms(arrival, depart):

    arrival.sort()
    depart.sort()
    a,b=0,0
    platforms = 0
    station = []
    while a<len(arrival) and b < len(depart):

        if arrival[a]<depart[b]:
            a+=1
            station.append(arrival)
        else:
            b+=1
            station.pop(len(station)-1)
        if platforms < len(station):
            platforms = len(stations)
            
            
        
