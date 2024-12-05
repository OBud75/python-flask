import copy

class Board:
    def __init__(self, position=None):
        if position is None:
            self.position = [[" " for _ in range(3)] for _ in range(3)]  
        else:
            self.position = position

    def is_won(self, player):
        winning_combinations = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]]  
        ]

        return any(all(self.position[row][col] == player for row, col in combination)
                   for combination in winning_combinations)

    def is_full(self):
        return all(cell != " " for row in self.position for cell in row)

    def get_empty_cells(self):
        return [(row, col) for row in range(3) for col in range(3) if self.position[row][col] == " "]

    def make_move(self, row, col, player):
        new_board = copy.deepcopy(self)
        new_board.position[row][col] = player
        return new_board

    def __str__(self):
        rows = [" | ".join(self.position[row]) for row in range(3)]
        return "\n--+---+---\n".join(rows)

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"  

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def minimax(self, board, depth, is_maximizing):
        if board.is_won("X"):
            return -10 + depth
        if board.is_won("O"):
            return 10 - depth
        if board.is_full():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for row, col in board.get_empty_cells():
                result = self.minimax(board.make_move(row, col, "O"), depth + 1, False)
                best_score = max(best_score, result)
            return best_score
        else:
            best_score = float('inf')
            for row, col in board.get_empty_cells():
                result = self.minimax(board.make_move(row, col, "X"), depth + 1, True)
                best_score = min(best_score, result)
            return best_score

    def play_computer_move(self):
        best_score = -float('inf')
        best_move = None
        for row, col in self.board.get_empty_cells():
            score = self.minimax(self.board.make_move(row, col, "O"), 0, False)
            if score > best_score:
                best_score = score
                best_move = (row, col)
        if best_move:
            self.board = self.board.make_move(best_move[0], best_move[1], "O")


    def play_game(self):
        while not self.board.is_full() and not self.board.is_won("X") and not self.board.is_won("O"):
            print(self.board)
            if self.current_player == "O":
                self.play_computer_move()
            else:
                move = self.get_player_move()
                self.board = self.board.make_move(move[0], move[1], self.current_player)
            if self.board.is_won(self.current_player):
                print(self.board)
                print(f"{self.current_player} a gagné !")
                return
            self.switch_player()
        print(self.board)
        print("Match nul !")

    def get_player_move(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.play_game()
