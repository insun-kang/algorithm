def solution(bridge_length, weight, truck_weights):
    bridge=[0]*bridge_length
    time=0
    while True:
        
        time+=1
        bridge.pop(0)
        
        if len(truck_weights) !=0:
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

        if len(bridge)==0:
            return time