import copy

class Board:
    def __init__(self, position=None):
        if position is None:
            self.position = [[" " for _ in range(3)] for _ in range(3)]  
        else:
            self.position = position

    def __str__(self):
        # D'une manière générale on aime bien avoir d'abord les méthodes
        # spéciales comme __init__, __str__, __repr__ etc. puis les propriétés,
        # les méthodes statiques et de classe et pour finir les méthodes
        # "normales". Ce n'est pas une règle absolue mais aide à rester cohérent.
        rows = [" | ".join(self.position[row]) for row in range(3)]
        return "\n--+---+---\n".join(rows)

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

    # On peut aussi utiliser une propriété pour rendre la méthode plus lisible.
    # Ce sont des préférences personnelles pour que le code appelant donne
    # l'impression de faire appel à un attribut plutôt qu'une méthode.
    # Ce n'est pas forcément une bonne idée si la méthode est coûteuse en temps ou
    # en ressources car justement le code appelant aura tendance à l'utiliser comme
    # un attribut enregistré en mémoire et non calculé à chaque appel : board.is_full
    @property
    def is_full(self):
        return all(cell != " " for row in self.position for cell in row)

    def get_empty_cells(self):
        return [(row, col) for row in range(3) for col in range(3) if self.position[row][col] == " "]

    @property
    # Idem board.empty_cells est peut être plus lisible que board.get_empty_cells()
    # mais la seconde option est plus claire dans le fait qu'il y a un calcul à effectuer.
    # Questions de préférences et de temps de calcul.
    def empty_cells(self):
        return [(row, col) for row in range(3) for col in range(3) if self.position[row][col] == " "]

    def make_move(self, row, col, player):
        new_board = copy.deepcopy(self)
        new_board.position[row][col] = player
        return new_board


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"  

    # On aura tendance à utiliser l'injection de dépendance afin de découpler
    # au maximum les classes. Ici ce n'est pas forcément justifié mais cela
    # peut le devenir dans des cas plus complexes ou encore pour les tests.
    def __init__(self, board: Board):
        self.board = board
        self.current_player = "X" 

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def minimax(self, board, depth, is_maximizing):
        # if board.is_won("X"):
        #     return -10 + depth
        # if board.is_won("O"):
        #     return 10 - depth
        # if board.is_full():
        #     return 0

        # if is_maximizing:
        #     best_score = -float('inf')
        #     for row, col in board.get_empty_cells():
        #         result = self.minimax(board.make_move(row, col, "O"), depth + 1, False)
        #         best_score = max(best_score, result)
        #     return best_score
        # else:
        #     best_score = float('inf')
        #     for row, col in board.get_empty_cells():
        #         result = self.minimax(board.make_move(row, col, "X"), depth + 1, True)
        #         best_score = min(best_score, result)
        #     return best_score

        # Repérez le code répétitif et essayez de le factoriser. Ne perdez pas
        # trop de temps à le faire en début de projet car le code évolue et ce
        # qui semble répétitif peut en réalité servir à autre chose plus tard.
        # Mais dès que vous avez une idée de comment factoriser n'hésitez pas.
        # Ici cela n'ajoute pas vraiment de lisibilité (je trouve même cela
        # plus compliqué à suivre) mais je met quand même un exemple :
        if is_maximizing:
            best_score = -float('inf')
            next_player = "O"
            min_or_max = max

        else:
            best_score = float('inf')
            next_player = "X"
            min_or_max = min

        # Python permet aussi une syntaxe "1 liner" pour les conditions :
        # best_score = -float('inf') if is_maximizing else float('inf')
        # Ici étant donné que plusieurs variables dépendent de la même condition
        # cela ne semble pas très adapté mais cela peut l'être dans certains cas.

        result = self.minimax(board.make_move(row, col, next_player), depth + 1, not is_maximizing)
        best_score = min_or_max(best_score, result)
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

    # On peut encapsuler et simplifier la condition utilisée dans la fonction suivante
    def _is_finished(self):
        return self.board.is_full() or self.board.is_won("X") or self.board.is_won("O")

    def play_game(self):
        # while not self.board.is_full() and not self.board.is_won("X") and not self.board.is_won("O"):
        # La condition se lit comme de l'anglais, puis les détails sont dans _is_finished
        while not self._is_finished():
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
    # Injéction des dépendances.
    board = Board()
    game = Game(board=board)
    game.play_game()
