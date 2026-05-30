from search_algorithms import *


# TEST 1 : FIND WINNING MOVE

print("TEST 1 : FIND WINNING MOVE")

board_game = TicTacToe()

board_game.board = [
    "X", "X", " ",
    "O", "O", " ",
    " ", " ", " "
]

board_game.print_board()

move1 = best_move_minimax(board_game)
move2 = best_move_alpha_beta(board_game)
move3 = best_move_heuristic(board_game)
move4 = monte_carlo_tree_search(board_game)

print("Minimax Selected Move:", move1)
print("Alpha Beta Selected Move:", move2)
print("Heuristic Alpha Beta Selected Move:", move3)
print("Monte Carlo Tree Search Move:", move4)

print("=" * 50)



# TEST 2 : PREVENT OPPONENT WIN

print("TEST 2 : PREVENT OPPONENT WIN")

board_game = TicTacToe()

board_game.board = [
    "O", "O", " ",
    "X", " ", " ",
    " ", "X", " "
]

board_game.print_board()

move1 = best_move_minimax(board_game)
move2 = best_move_alpha_beta(board_game)
move3 = best_move_heuristic(board_game)
move4 = monte_carlo_tree_search(board_game)

print("Minimax Selected Move:", move1)
print("Alpha Beta Selected Move:", move2)
print("Heuristic Alpha Beta Selected Move:", move3)
print("Monte Carlo Tree Search Move:", move4)

print("=" * 50)



# TEST 3 : EMPTY GAME BOARD

print("TEST 3 : EMPTY GAME BOARD")

board_game = TicTacToe()

board_game.print_board()

move1 = best_move_minimax(board_game)
move2 = best_move_alpha_beta(board_game)
move3 = best_move_heuristic(board_game)
move4 = monte_carlo_tree_search(board_game)

print("Minimax Selected Move:", move1)
print("Alpha Beta Selected Move:", move2)
print("Heuristic Alpha Beta Selected Move:", move3)
print("Monte Carlo Tree Search Move:", move4)

print("=" * 50)



# TEST 4 : DRAW CONDITION

print("TEST 4 : DRAW CONDITION")

board_game = TicTacToe()

board_game.board = [
    "X", "O", "X",
    "X", "O", "O",
    "O", "X", " "
]

board_game.print_board()

move1 = best_move_minimax(board_game)
move2 = best_move_alpha_beta(board_game)
move3 = best_move_heuristic(board_game)
move4 = monte_carlo_tree_search(board_game)

print("Minimax Selected Move:", move1)
print("Alpha Beta Selected Move:", move2)
print("Heuristic Alpha Beta Selected Move:", move3)
print("Monte Carlo Tree Search Move:", move4)
