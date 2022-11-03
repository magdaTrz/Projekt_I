import time
import os
import random

# Wymiary planszy
BOARD_COLS = 7
BOARD_ROWS = 6


class Board():

    def __init__(self):  # funkcja wywoływana w trakcie tworzenia obiektu
        self.board = [[' ' for _ in range(BOARD_COLS)]
                      for _ in range(BOARD_ROWS)]
        self.turns = 0  # licznik tur
        self.last_move = [-1, -1]

    def print_start_view(self):  # funkcja z animacją
        filenames = ["ascii_3.txt", "ascii_4.txt",
                     "ascii_2.txt", "ascii_1.txt"]
        frames = []
        os.system("cls")
        for name in filenames:
            with open(name, "r", encoding="utf8") as f:
                frames.append(f.readlines())
        for frame in frames:
            print("".join(frame))
            time.sleep(0.5)
            os.system("cls")

    def print_logo(self):
        print("""
   __________  _   ___   ____________________   __ __
  / ____/ __ \/ | / / | / / ____/ ____/_  __/  / // /
 / /   / / / /  |/ /  |/ / __/ / /     / /    / // /_
/ /___/ /_/ / /|  / /|  / /___/ /___  / /    /__  __/
\____/\____/_/ |_/_/ |_/_____/\____/ /_/       /_/   
                                                     

        """, end="")
        time.sleep(0)

        print("-------- Witaj w grze  -------- \n ")

    def print_board(self):  # funkcja wyświetlająca aktualna plansze
        print("\n")
        for r in range(BOARD_COLS):
            print(f"  [{r+1}] ", end="")  # numerowanie kolumn
        print("\n")

        for r in range(BOARD_ROWS):  # wyświetnalnie planszy
            print('|', end="")
            for c in range(BOARD_COLS):
                print(f"  {self.board[r][c]}  |", end="")
            print("\n ------------------------------------------")

        print(f"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

    def which_turn(self):  # funkcja sprawdzająca czyja jest aktualnie tura
        players = ['X', 'O']
        return players[self.turns % 2]

    def in_bounds(self, r, c):  # sprawdza czy jest w granicach planszy
        # oczekujemy True gdy to jest prawdą
        return (r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLS)

    def turn(self, column):
        # sprawdzamy od dołu do góry kolumnę
        for i in range(BOARD_ROWS-1, -1, -1):
            if self.board[i][column] == ' ':  # sprawdzamy czy jest puste
                self.board[i][column] = self.which_turn()
                self.last_move = [i, column]

                self.turns += 1
                return True

        return False  # nie znaleziono żadnego wolnego rzedu

    def check_whoPlaying(self, letter):
        letter = letter.upper()
        if (letter == 'K' or letter == 'G'):
            return True
        else:
            return False

    def check_winner(self, game):
        chip = game.which_turn()

        for r in range(BOARD_ROWS):  # sprawdzanie w POZIOMIE
            for c in range(BOARD_COLS - 3):
                if self.board[c][r] == chip and self.board[c+1][r] == chip and self.board[c+2][r] == chip and self.board[c+3][r] == chip:
                    print("       ******************************")
                    print(
                        f"      *** Koniec gry, {game.which_turn()} zwycieżył! ***")
                    print("       ******************************")
                    return True

        for r in range(BOARD_ROWS):  # sprawdzanie w PIONIE
            for c in range(BOARD_COLS - 3):
                if self.board[r][c] == chip and self.board[r][c+1] == chip and self.board[r][c+2] == chip and self.board[r][c+3] == chip:
                    print("       ******************************")
                    print(
                        f"      *** Koniec gry, {game.which_turn()} zwycieżył! ***")
                    print("       ******************************")
                    return True

        for r in range(BOARD_ROWS - 3):  # sprawdzanie od góra prawo do dół lewo
            for c in range(3, BOARD_COLS):
                if self.board[r][c] == chip and self.board[r+1][c-1] == chip and self.board[r+2][c-2] == chip and self.board[r+3][c-3] == chip:
                    print("       ******************************")
                    print(
                        f"      *** Koniec gry, {game.which_turn()} zwycieżył! ***")
                    print("       ******************************")
                    return True

        for r in range(BOARD_ROWS - 3):  # sprawdzanie od góra lewo do dół prawo
            for c in range(BOARD_COLS - 3):
                if self.board[r][c] == chip and self.board[r+1][c+1] == chip and self.board[r+2][c+2] == chip and self.board[r+3][c+3] == chip:
                    print("       ******************************")
                    print(
                        f"      *** Koniec gry, {game.which_turn()} zwycieżył! ***")
                    print("       ******************************")
                    return True

        return False


def play():
    # Inicjalizacja gry
    game = Board()
    game.print_start_view()

    valid_choose_whoPlays = False
    while not valid_choose_whoPlays:
        whoPlays = input(
            "Z kim chcesz grać? Wpisz: \n 'K' - z komputerem  'G' - z drugim graczem \n")
        try:
            valid_choose_whoPlays = game.check_whoPlaying(whoPlays)
        except:
            print(f"Wybrano niepoprawną opcję")

    game_over = False
    while not game_over:
        game.print_logo()
        game.print_board()

        valid_move = False
        while not valid_move:
            # pytanie gracza o wybranie kolumny
            if (whoPlays == "G" or whoPlays == "g"):
                user_move = input(
                    f"Teraz tura: {game.which_turn()}- wybierz kolumnę (1-7): ")
                try:
                    valid_move = game.turn(int(user_move)-1)
                except:
                    print(f"\rWybierz numer od 1 do 7", end="")

            if (whoPlays == "K" or whoPlays == "k"):
                if (game.which_turn() == "X"):  # ruch człowieka
                    user_move = input(
                        f"Teraz tura: {game.which_turn()}- wybierz kolumnę (1-7): ")
                try:
                    valid_move = game.turn(int(user_move)-1)
                except:
                    print(f"\rWybierz numer od 1 do 7", end="")

                if (game.which_turn() == "O"):  # ruch komputera
                    cpu_move = random.randint(1, 7)
                    print(
                        f"Teraz tura: {game.which_turn()} komputer wybrał: {cpu_move}")
                    try:
                        valid_move = game.turn(cpu_move-1)
                    except:
                        print(f"\rKomputer zle wybrał ", end="")

        # gdy game.check_winner() stanie się prawdą gra się kończy
        game_over = game.check_winner(game)
        print("\n")
        game.print_board()

        # gdy jest remis
        if not any(' ' in x for x in game.board):
            print("Brak zwycięzcy! Remis")
            return


if __name__ == '__main__':
    play()
