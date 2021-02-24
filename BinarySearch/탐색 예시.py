# 순차 탐색 소스코드 구현
def sequential_search(target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(len(array)):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)

''' 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간값의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)
'''

# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

print("찾을 값 입력하세요.")
target = input() # 찾고자 하는 문자열

print("원하는 원소 개수만큼 값을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행 결과 출력
# print(sequential_search(target, array))

# 이진 탐색 수행 결과 출력
print(binary_search(array, target))