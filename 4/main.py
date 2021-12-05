def get_bingo(boards, numbers):
    boards_ = boards[:]
    for i in range(6, len(numbers)+1):
        for board in boards_:
            if is_bingo(board, numbers[:i]):
                boards_.remove(board)
                yield board, i

def is_bingo(board, numbers):
    for row in board:
        if all(number in numbers for number in row):
            return True
    for i in range(len(board)):
        column = [row[i] for row in board]
        if all(number in numbers for number in column):
            return True

with open("input.txt", 'r') as f:
    input = f.read().split('\n\n')
    numbers = list(map(int, input[0].split(',')))
    boards = [[list(map(int, line.split()))  for line in board.split('\n')] for board in input[1:]]
    
    winning_boards = get_bingo(boards, numbers)
    for board, i in winning_boards:
        print(numbers[i-1] * sum([number for line in board for number in line if number not in numbers[:i]]))

