def solution(cacheSize, cities):
    answer = 0
    
    # 캐시 (오래전에 사용 -> 가장 최근에 사용) 으로 정렬
    cache = []
    for i in range(len(cities)):
        if cities[i].lower() not in cache:
            # 캐시가 꽉 찼을때 가장 오래 전에 사용한 메모리를 비움
            if len(cache) >= cacheSize and cacheSize > 0:
                cache.pop(0)
            if cacheSize > 0:
                cache.append(cities[i].lower())
            answer += 5
        else:
            # 캐시에 있는 도시 이름일 경우 캐시의 순서를 갱신
            cache.remove(cities[i].lower())
            cache.append(cities[i].lower())
            answer += 1
    
    return answer
