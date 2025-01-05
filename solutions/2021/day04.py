from collections import defaultdict
def solve_board(board, balls):
    lines = defaultdict(int)
    for ball_count, ball in enumerate(balls):
        if ball in board:
            i, j = board.pop(ball)
            lines[f"r{i}"] += 1
            lines[f"c{j}"] += 1
            if lines[f"r{i}"] == 5 or lines[f"c{j}"] == 5:
                return (ball_count, ball * sum(board.keys()))

def main(data):
    balls, *games = data.split("\n\n")
    balls = [int(x) for x in balls.split(",")]
    results = []
    for bingo in games:
        board = {}
        for j, row in enumerate(bingo.split("\n")):
            for i, val in enumerate(row.split()): 
                board[int(val)] = (i, j)
        results.append(solve_board(board, balls))

    return min(results, key=lambda x: x[0])[1], max(results, key=lambda x: x[0])[1]