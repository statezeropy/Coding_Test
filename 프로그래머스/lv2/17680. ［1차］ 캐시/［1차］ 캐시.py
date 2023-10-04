import collections

def solution(cacheSize, cities):
    answer = 0
    cache = collections.deque([])
    if cacheSize == 0:
        return 5*len(cities)
    
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            answer += 1
        else:
            if len(cache) >= cacheSize and len(cache) > 0:
                cache.pop()
            answer += 5
        cache.appendleft(city)
        
    return answer