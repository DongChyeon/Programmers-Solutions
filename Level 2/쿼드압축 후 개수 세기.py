quad_tree = ''

# 해당 영역이 같은 숫자인지 체크
def is_same_arr(arr, x, y, size):
    num = arr[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if num != arr[i][j]:
                return False
                
    return True
            
def div_arr(arr, x, y, size):
    global quad_tree
    
    # 같은 숫자일 경우 quad_tree 문자열에 추가
    if is_same_arr(arr, x, y, size):
        quad_tree += str(arr[y][x])
    else:
        size = size // 2
        # 해당 영역이 같은 숫자가 아닐 경우 4분할
        for i in range(2):
            for j in range(2):
                div_arr(arr, x + size * i, y + size * j, size)

def solution(arr):
    global quad_tree
    
    div_arr(arr, 0, 0, len(arr))
    quad_tree = list(quad_tree)
    
    return [quad_tree.count('0'), quad_tree.count('1')]
