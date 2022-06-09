def minimax(node, depth, isMaximizerPlayer):
    return alphabeta(node, depth, -1000, 1000, isMaximizerPlayer)


def alphabeta(node, depth, a, b, isMaximizerPlayer):
    if isGameOver(node) or depth == 0:
        return value(node)

    if isMaximizerPlayer:
        for i, j in getMoves(node):
            node[i][j] = 'X'
            a = max(a, alphabeta(node, depth-1, a, b, False))
            node[i][j] = '_'
            if a >= b:
                break
        return a
    else:
        for i, j in getMoves(node):
            node[i][j] = 'O'
            b = min(b, alphabeta(node, depth-1, a, b, True))
            node[i][j] = '_'
            if a >= b:
                break
        return b


def getBestMove():
    bestScore = -1000
    bestMove = (0, 0)
    for i, j in getMoves(board):
        board[i][j] = 'X'
        score = minimax(board, depth-1, False)
        board[i][j] = '_'
        if score > bestScore:
            bestScore = score
            bestMove = (i, j)
    return bestMove


def value(node):
    winner = isGameOver(node)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    return 0


def getMoves(node):
    for i in range(3):
        for j in range(3):
            if node[i][j] == '_':
                yield i, j


def isGameOver(node):
    for line in getAllLine(node):
        if line.count('X') == 3:
            return 'X'
        elif line.count('O') == 3:
            return 'O'
    if all('_' not in row for row in node):
        return 'Draw'
    return None


def getAllLine(node):
    for row in node:
        yield row
    for col in range(3):
        yield (node[0][col], node[1][col], node[2][col])
    yield (node[0][0], node[1][1], node[2][2])
    yield (node[0][2], node[1][1], node[2][0])


def printBoard():
    print('Lượt của', ('O', 'X')[isMaximizerPlayer])
    UIBoard = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for i in range(3):
        for j in range(3):
            if board[i][j] != '_':
                UIBoard[i][j] = board[i][j]
    for row in UIBoard:
        print(*row)
    print()


if __name__ == '__main__':
    board = [['_']*3 for _ in range(3)]
    depth = 9
    isMaximizerPlayer = True

    printBoard()

    while True:
        isgameover = isGameOver(board)
        if isgameover:
            print('Hoà' if isgameover == 'Draw' else f'{isgameover} thắng !')
            break
        if isMaximizerPlayer:
            i, j = getBestMove()
            board[i][j] = 'X'
        else:
            index = int(input('Input position (0-8): ').strip())
            board[index//3][index % 3] = 'O'
        printBoard()
        isMaximizerPlayer = not isMaximizerPlayer
