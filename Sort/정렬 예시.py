def selection_sort(array):
    for i in range(len(array)):
        min_index = i    # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i] # 스왑
    
    print(array)

# 거의 정렬되어 있는 상태라면 효율이 좋음
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, - 1):  # 인덱스 i부터 1까지 감소하며 반복하는 문법
            if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    
    print(array)

def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    print(array)

'''
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:    # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:   # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
'''

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# 데이터의 범위가 작을 때 사용
def count_sort(array):
    # 모든 원소의 값이 0보다 크거나 같을 때 동작함
    # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
    count = [0] * (max(array) + 1)

    for i in range(len(array)):
        count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

    for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
        for _ in range(count[i]):
            print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

selection_sort(array)
insertion_sort(array)
bubble_sort(array)
print(quick_sort(array))
count_sort(array)