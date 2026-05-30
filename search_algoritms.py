import math
import random
from copy import deepcopy


# TIC TAC TOE GAME

class TicTacToe:

    def __init__(self):
        self.grid = [" "] * 9

    def display(self):
        print()

        for row in range(3):
            start = row * 3
            print(
                self.grid[start],
                "|",
                self.grid[start + 1],
                "|",
                self.grid[start + 2]
            )

        print()

    def empty_positions(self):

        free_cells = []

        for index, value in enumerate(self.grid):
            if value == " ":
                free_cells.append(index)

        return free_cells

    def place_symbol(self, index, symbol):
        self.grid[index] = symbol

    def clear_position(self, index):
        self.grid[index] = " "

    def check_winner(self, symbol):

        patterns = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in patterns:

            if (
                self.grid[a] == symbol and
                self.grid[b] == symbol and
                self.grid[c] == symbol
            ):
                return True

        return False

    def board_full(self):
        return all(cell != " " for cell in self.grid)

    def finished(self):

        return (
            self.check_winner("X") or
            self.check_winner("O") or
            self.board_full()
        )


# MINIMAX SEARCH

def minimax_search(board, is_max_turn):

    if board.check_winner("X"):
        return 1

    if board.check_winner("O"):
        return -1

    if board.board_full():
        return 0

    if is_max_turn:

        optimal = -math.inf

        for move in board.empty_positions():

            board.place_symbol(move, "X")

            score = minimax_search(board, False)

            board.clear_position(move)

            optimal = max(optimal, score)

        return optimal

    else:

        optimal = math.inf

        for move in board.empty_positions():

            board.place_symbol(move, "O")

            score = minimax_search(board, True)

            board.clear_position(move)

            optimal = min(optimal, score)

        return optimal


def minimax_best_move(board):

    highest = -math.inf
    best_choice = None

    for move in board.empty_positions():

        board.place_symbol(move, "X")

        current_score = minimax_search(board, False)

        board.clear_position(move)

        if current_score > highest:
            highest = current_score
            best_choice = move

    return best_choice


# ALPHA BETA SEARCH

def alpha_beta_search(board, alpha, beta, is_max_turn):

    if board.check_winner("X"):
        return 1

    if board.check_winner("O"):
        return -1

    if board.board_full():
        return 0

    if is_max_turn:

        value = -math.inf

        for move in board.empty_positions():

            board.place_symbol(move, "X")

            result = alpha_beta_search(
                board,
                alpha,
                beta,
                False
            )

            board.clear_position(move)

            value = max(value, result)

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:

        value = math.inf

        for move in board.empty_positions():

            board.place_symbol(move, "O")

            result = alpha_beta_search(
                board,
                alpha,
                beta,
                True
            )

            board.clear_position(move)

            value = min(value, result)

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


def alpha_beta_best_move(board):

    top_score = -math.inf
    best_choice = None

    for move in board.empty_positions():

        board.place_symbol(move, "X")

        current = alpha_beta_search(
            board,
            -math.inf,
            math.inf,
            False
        )

        board.clear_position(move)

        if current > top_score:
            top_score = current
            best_choice = move

    return best_choice


# HEURISTIC EVALUATION

def heuristic_score(board):

    if board.check_winner("X"):
        return 100

    if board.check_winner("O"):
        return -100

    total = 0

    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for x, y, z in lines:

        values = [
            board.grid[x],
            board.grid[y],
            board.grid[z]
        ]

        if values.count("X") == 2 and values.count(" ") == 1:
            total += 10

        if values.count("O") == 2 and values.count(" ") == 1:
            total -= 10

    return total


# HEURISTIC ALPHA BETA SEARCH

def heuristic_alpha_beta(
        board,
        depth,
        alpha,
        beta,
        is_max_turn,
        limit=3):

    if depth >= limit or board.finished():
        return heuristic_score(board)

    if is_max_turn:

        answer = -math.inf

        for move in board.empty_positions():

            board.place_symbol(move, "X")

            value = heuristic_alpha_beta(
                board,
                depth + 1,
                alpha,
                beta,
                False,
                limit
            )

            board.clear_position(move)

            answer = max(answer, value)

            alpha = max(alpha, answer)

            if alpha >= beta:
                break

        return answer

    else:

        answer = math.inf

        for move in board.empty_positions():

            board.place_symbol(move, "O")

            value = heuristic_alpha_beta(
                board,
                depth + 1,
                alpha,
                beta,
                True,
                limit
            )

            board.clear_position(move)

            answer = min(answer, value)

            beta = min(beta, answer)

            if alpha >= beta:
                break

        return answer


def heuristic_best_move(board):

    best_value = -math.inf
    selected = None

    for move in board.empty_positions():

        board.place_symbol(move, "X")

        value = heuristic_alpha_beta(
            board,
            0,
            -math.inf,
            math.inf,
            False
        )

        board.clear_position(move)

        if value > best_value:
            best_value = value
            selected = move

    return selected


# MONTE CARLO TREE SEARCH

def simulation(board, player):

    cloned_board = deepcopy(board)

    while not cloned_board.finished():

        move = random.choice(
            cloned_board.empty_positions()
        )

        cloned_board.place_symbol(move, player)

        player = "O" if player == "X" else "X"

    if cloned_board.check_winner("X"):
        return 1

    if cloned_board.check_winner("O"):
        return -1

    return 0


def monte_carlo_search(board, rounds=300):

    score_map = {}

    for move in board.empty_positions():

        total_points = 0

        for _ in range(rounds):

            cloned_board = deepcopy(board)

            cloned_board.place_symbol(move, "X")

            result = simulation(
                cloned_board,
                "O"
            )

            total_points += result

        score_map[move] = total_points

    return max(score_map, key=score_map.get)
