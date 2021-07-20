def solution(cacheSize, cities):
    answer = 0
    cache=[]
    
    for city in cities:
        if city.lower() in cache:
            answer+=1
            cache.remove(city.lower())
            cache.append(city.lower())
        else:
            answer+=5
            if len(cache)<cacheSize:
                cache.append(city.lower())
            elif len(cache)==cacheSize and len(cache) !=0:
                cache.pop(0)
                cache.append(city.lower())
            elif len(cache) ==0:
                continue
    return answer