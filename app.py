from flask import Flask, render_template, request, jsonify
import random
import copy

app = Flask(__name__)

# ---------- VALIDATION ----------
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = row - row % 3, col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False
    return True

# ---------- SOLVER ----------
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# ---------- GENERATE ----------
def generate_full_board():
    board = [[0]*9 for _ in range(9)]

    def fill():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if fill():
                                return True
                            board[i][j] = 0
                    return False
        return True

    fill()
    return board

def remove_numbers(board, level):
    levels = {"easy": 30, "medium": 40, "hard": 50}
    attempts = levels[level]

    while attempts > 0:
        r, c = random.randint(0, 8), random.randint(0, 8)
        if board[r][c] != 0:
            board[r][c] = 0
            attempts -= 1
    return board

# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    level = request.json["level"]
    board = generate_full_board()
    solution = copy.deepcopy(board)
    puzzle = remove_numbers(board, level)
    return jsonify({"puzzle": puzzle, "solution": solution})

@app.route("/solve", methods=["POST"])
def solve_route():
    board = request.json["board"]
    solve(board)
    return jsonify({"solution": board})

@app.route("/hint", methods=["POST"])
def hint():
    board = request.json["board"]
    solution = request.json["solution"]

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return jsonify({"row": i, "col": j, "value": solution[i][j]})

    return jsonify({"msg": "No empty cells"})

if __name__ == "__main__":
    app.run(debug=True)