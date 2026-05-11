🎯 Sudoku Solver
A web-based Sudoku puzzle application built using Python Flask and HTML, CSS, JavaScript. Users can generate puzzles, solve them automatically, and get hints — all in the browser.

🚀 Features

🎲 Generate Sudoku puzzles at 3 difficulty levels
✅ Auto-solve any puzzle using backtracking algorithm
💡 Hint system to reveal one correct cell at a time
🎮 Interactive 9x9 grid with real-time input
📊 Easy, Medium, and Hard difficulty modes


🛠️ Tech Stack
LayerTechnologyBackendPython + FlaskFrontendHTML, CSS, JavaScriptAlgorithmRecursive BacktrackingAPIFlask REST Routes

📁 Project Structure
sudoku-solver/
├── app.py
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js

⚙️ How to Run
bashgit clone https://github.com/yourusername/sudoku-solver.git
cd sudoku-solver
pip install flask
python app.py
Open browser at http://localhost:5000

🔌 API Endpoints
MethodEndpointDescriptionPOST/generateGenerate puzzle by difficultyPOST/solveSolve the current boardPOST/hintGet hint for first empty cell

🧠 Algorithm — Recursive Backtracking
pythondef solve(board):
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

🎯 Difficulty Levels
LevelCells RemovedEasy30 cellsMedium40 cellsHard50 cells

👨‍💻 Developer
Made with ❤️ by Deva
Department of Computer Science & Engineering
ANITS — Anil Neerukonda Institute of Technology & Sciences

📄 License
This project is open source and free to use for educational purposes.
