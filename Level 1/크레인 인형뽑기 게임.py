def solution(board, moves):
    answer = 0

    screen = []
    basket = []
    
    for col in range(0, len(board[0])):
        temp = []
        for row in range(len(board) - 1, -1, -1):
            if (board[row][col] == 0):
                continue
            else:
                temp.append(board[row][col])
        screen.append(temp)
    
    for move in moves:
        if len(screen[move - 1]) != 0:
            doll = screen[move - 1].pop()
            if len(basket) > 0 and doll == basket[-1]:
                basket.pop()
                answer += 2
            else:
                basket.append(doll)
                        
    return answer