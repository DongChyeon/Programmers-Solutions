def solution(n, lost, reserve):
    answer = 0
    
    # 첫 인덱스와 마지막 인덱스의 1은 쓰레기값
    students = [1] * (n + 2)
    
    # 읽어버린 사람과 여분을 가진 사람을 표시
    for student in lost:
        students[student] -= 1
    for studnet in reserve:
        students[studnet] += 1
        
    # 여분을 가진 사람 양옆에 체육복이 없는 사람이 없다면 빌려줌
    for i in range (1, len(students) - 1):
        if students[i] == 2:
            if students[i - 1] == 0:
                students[i] -= 1
                students[i - 1] += 1
            elif students[i + 1] == 0:
                students[i] -= 1
                students[i + 1] += 1
                
    for i in range(1, len(students) - 1):
        if students[i] > 0:
            answer += 1
          
    return answer