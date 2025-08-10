def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for i in range (len(board)):
            if board[i][m-1]!=0: #해당 칸에 인형이 있으면
                if stack and stack[-1]==board[i][m-1]:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(board[i][m-1])
                board[i][m-1]=0 #뽑았으니까 0으로
                break
    return answer