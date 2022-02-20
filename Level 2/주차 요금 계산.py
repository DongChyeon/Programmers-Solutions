import math

def solution(fees, records):
    # entry_list[number] = [시간, IN/OUT, 캐시메모리]
    entry_list = dict()
    for x in records:
        time, number, info = x.split()
        if info == "IN":
            # 이전에 들어온 기록이 없는 경우
            if number not in entry_list:
                a, b = map(int, time.split(':'))
                time = a * 60 + b
                entry_list[number] = [time, "IN", -1]
            # 이미 기록된 주차 시간이 있다면 3번째 인덱스에 입차 시간 기록
            else:
                a, b = map(int, time.split(':'))
                time = a * 60 + b
                entry_list[number][2] = time
                entry_list[number][1] = "IN"
        else:
            # 이전에 나온 기록이 없는 경우
            if entry_list[number][1] == "IN" and entry_list[number][2] == -1:
                a, b = map(int, time.split(':'))
                time = a * 60 + b
                entry_list[number][0] = time - entry_list[number][0]
                entry_list[number][1] = "OUT"
                entry_list[number][2] = -1
            # 3번째 인덱스에 기록된 입차 시간이 있을 경우 계산해서 1번째 인덱스에 누적
            else:
                a, b = map(int, time.split(':'))
                time = a * 60 + b
                entry_list[number][0] = entry_list[number][0] + (time - entry_list[number][2])
                entry_list[number][1] = "OUT"
                entry_list[number][2] = -1
    
    # OUT 기록이 없는 차량은 23:59에 출차한 것으로 처리
    for x in records:
        time, number, info = x.split()
        if entry_list[number][1] == "IN":
            if entry_list[number][2] != -1:
                entry_list[number][0] = entry_list[number][0] + (1439 - entry_list[number][2])
            else:
                entry_list[number][0] = 1439 - entry_list[number][0]
            entry_list[number][1] = "OUT"
            entry_list[number][2] = -1
    
    # 차량 번호가 작은 자동차부터 정렬
    entry_list = sorted(entry_list.items())
    
    answer = []
    for key, value in entry_list:
        if value[0] > fees[0]:
            answer.append(fees[1] + math.ceil((value[0] - fees[0]) / fees[2]) * fees[3])
        else:
            answer.append(fees[1])
    
    return answer
