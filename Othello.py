# Author: Patrick Lim
# GitHub username: limpa95
# Date: 6/3/2023
# Description:
# This program creates a class called Othello that allows two people to play text-based Othello. It uses a 2D list
# to represent the game board, provides a list of available moves for players, and determines who wins the game.

class GameBoard:
    """Represents an 8x8 Othello game board using a 10x10 grid. Used by the Othello class to make the game board."""

    def __init__(self):
        """Creates the start of the game board using a 2D list. All parameters are private.
        Edge: * (star)
        Black piece: X
        White piece: O
        Empty space: . (dot)"""

        self._board = [
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],      # starting board
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", "O", "X", ".", ".", ".", "*"],
            ["*", ".", ".", ".", "X", "O", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
        ]

    def get_board(self):
       """Returns self._board to get the current state of the game_board."""

       return self._board

class Player:
    """Represents a player in the game. Used by Othello class to create a player for the game.
    All data members are private."""

    def __init__(self, player_name, color):
        """Creates the player using player name and color(either black or white) as parameters.
        player_name - represents the player's name
        color - represents which color piece the player is using.
        Parameters are received from the create_player method in the Othello class.
        All data members are private."""

        self._player_name = player_name
        self._color = color

    def get_player_name(self):
        """Returns the value for player_name. Used by Othello class to get the player's name."""

        return self._player_name

    def get_color(self):
        """Returns the value for color. Used by Othello class to get the player's color."""

        return self._color

class Othello:
    """This class represents the Othello game with information about the two players (black or white) and the board.
    The player with the color black starts first. Uses GameBoard class to obtain information about the game board
    and uses the Player class to create the two players for the Othello game."""

    def __init__(self):
        """Creates the Othello game. It takes no parameters. It calls the GameBoard class to create the game board
        with the starting positions for the players. It also creates an empty list to keep track of player objects,
        creates an empty list of player positions to keep track of,
        sets get_board return value to variable called board, and finally sets the number of white and black pieces
        to 0 to keep track of who wins the game.
        All data members are private"""

        self._player_list = []
        self._position_list_b = []
        self._position_list_w = []
        board_class = GameBoard()
        self._board = board_class.get_board()
        self._white_count = 0
        self._black_count = 0

    def print_board(self):
        """Prints out the current board, including the boundaries by calling the get_board method. Returns the board
        in rows and columns like figure 2 in the readme.
        Keeps Game_board's parameters private."""

        for row in self._board:
            for column in row:
                print(column + " ", end ='')
            print("\n")

    def create_player(self, player_name, color):
        """ Takes name and color as parameters.
        player_name - represents the player's name
        color - represents which color piece the player is using.
        Creates a player object with the given name and color (black or white) and adds it to a player list that
        was initialized for the Othello class.
        Uses Player class to create the player object."""

        player = Player(player_name, color)
        self._player_list.append(player)

    def return_winner(self):
        """Returns "Winner is white player: player’s name" when white player wins the game,
        returns "Winner is black player: player’s name" when black player wins the game, and
        returns "It's a tie" if black and white player has the same number of pieces on the board when the game ends.
        Used by play_game to determine who wins the game."""

        for index_r, row in enumerate(self._board):
            for index_c, column in enumerate(row):
                if self._board[index_r][index_c] == "O":
                    self._white_count += 1
                if self._board[index_r][index_c] == "X":
                    self._black_count += 1

        if self._white_count > self._black_count:
            for player in self._player_list:
                if player.get_color() == "white":
                    return "Winner is white player: " + player.get_player_name()
        if self._black_count > self._white_count:
            for player in self._player_list:
                if player.get_color() == "black":
                    return "Winner is black player: " + player.get_player_name()
        if self._white_count == self._black_count:
            return "It's a tie"

    def check_up(self, color):
        """Takes color as a parameter.
        color - represents which color piece the player is using.
        Used by return_available_positions method to determine if spaces adjacent
        and up is a valid move. If not, this method returns nothing. If yes, adds position to list of available
        positions."""

        index_r_check = 0

        for index_r, row in enumerate(self._board):
            for index_c, column in enumerate(row):
                if color == "black":
                    index_r_check += index_r
                    if self._board[index_r_check][index_c] == "X":
                        while self._board[index_r_check - 1][index_c] == "O":
                            index_r_check -= 1
                        if self._board[index_r_check - 1][index_c] == "." \
                                and self._board[index_r_check][index_c] != "X":
                            position = (index_r_check - 1, index_c)
                            self._position_list_b.append(position)
                    index_r_check = 0
                if color == "white":
                    index_r_check += index_r
                    if self._board[index_r_check][index_c] == "O":
                        while self._board[index_r_check - 1][index_c] == "X":
                            index_r_check -= 1
                        if self._board[index_r_check - 1][index_c] == "." \
                                and self._board[index_r_check][index_c] != "O":
                            position = (index_r_check - 1, index_c)
                            self._position_list_w.append(position)
                    index_r_check = 0

    def check_right(self, color):
        """Takes color as a parameter.
        color - represents which color piece the player is using.
        Used by return_available_positions method to determine if spaces adjacent
        and right is a valid move. If not, this method returns nothing. If yes, adds position to list of available
        positions."""

        index_c_check = 0

        for index_r, row in enumerate(self._board):
            for index_c, column in enumerate(row):
                if color == "black":
                    index_c_check += index_c
                    if self._board[index_r][index_c_check] == "X":
                        while self._board[index_r][index_c_check + 1] == "O":
                            index_c_check += 1
                        if self._board[index_r][index_c_check + 1] == "." \
                                and self._board[index_r][index_c_check] != "X":
                            position = (index_r, index_c_check + 1)
                            self._position_list_b.append(position)
                    index_c_check = 0
                if color == "white":
                    index_c_check += index_c
                    if self._board[index_r][index_c_check] == "O":
                        while self._board[index_r][index_c_check + 1] == "X":
                            index_c_check += 1
                        if self._board[index_r][index_c_check + 1] == "." \
                                and self._board[index_r][index_c_check] != "O":
                            position = (index_r, index_c_check + 1)
                            self._position_list_w.append(position)
                    index_c_check = 0

    def check_down(self, color):
        """Takes color as a parameter.
        color - represents which color piece the player is using.
        Used by return_available_positions method to determine if spaces adjacent
        and down is a valid move. If not, this method returns nothing. If yes, adds position to list of available
        positions."""

        index_r_check = 0

        for index_r, row in enumerate(self._board):
            for index_c, column in enumerate(row):
                if color == "black":
                    index_r_check += index_r
                    if self._board[index_r_check][index_c] == "X":
                        while self._board[index_r_check + 1][index_c] == "O":
                            index_r_check += 1
                        if self._board[index_r_check + 1][index_c] == "." \
                                and self._board[index_r_check][index_c] != "X":
                            position = (index_r_check + 1, index_c)
                            self._position_list_b.append(position)
                    index_r_check = 0
                if color == "white":
                    index_r_check += index_r
                    if self._board[index_r_check][index_c] == "O":
                        while self._board[index_r_check + 1][index_c] == "X":
                            index_r_check += 1
                        if self._board[index_r_check + 1][index_c] == "." \
                                and self._board[index_r_check][index_c] != "O":
                            position = (index_r_check + 1, index_c)
                            self._position_list_w.append(position)
                    index_r_check = 0

    def check_left(self, color):
        """Takes color as a parameter.
        color - represents which color piece the player is using.
        Used by return_available_positions method to determine if spaces adjacent
        and left is a valid move. If not, this method returns nothing. If yes, adds position to list of available
        positions."""

        index_c_check = 0

        for index_r, row in enumerate(self._board):
            for index_c, column in enumerate(row):
                if color == "black":
                    index_c_check += index_c
                    if self._board[index_r][index_c_check] == "X":
                        while self._board[index_r][index_c_check - 1] == "O":
                            index_c_check -= 1
                        if self._board[index_r][index_c_check - 1] == "." \
                                and self._board[index_r][index_c_check] != "X":
                            position = (index_r, index_c_check - 1)
                            self._position_list_b.append(position)
                    index_c_check = 0
                if color == "white":
                    index_c_check += index_c
                    if self._board[index_r][index_c_check] == "O":
                        while self._board[index_r][index_c_check - 1] == "X":
                            index_c_check -= 1
                        if self._board[index_r][index_c_check - 1] == "." \
                                and self._board[index_r][index_c_check] != "O":
                            position = (index_r, index_c_check - 1)
                            self._position_list_w.append(position)
                    index_c_check = 0

    def check_diagonal_up_right(self, color):
        """Takes color as a parameter.
        color - represents which color piece the player is using.
        Used by return_available_positions method to determine if spaces adjacent
        and diagonal up right is a valid move. If not, this method returns nothing. If yes, adds position to
        list of available positions."""

        index_r_check = 0
        index_c_check = 0

        for index_r, row in enumerate(self._board):
            for index_c, column in enumerate(row):
                if color == "black":
                    index_r_check += index_r
                    index_c_check += index_c
                    if self._board[index_r_check][index_c_check] == "X":
                        while self._board[index_r_check - 1][index_c_check + 1] == "O":
                            index_r_check -= 1
                            index_c_check += 1
                        if self._board[index_r_check - 1][index_c_check + 1] == "." \
                                and self._board[index_r_check][index_c_check] != "X":
                            position = (index_r_check - 1, index_c_check + 1)
                            self._position_list_b.append(position)
                    index_r_check = 0
                    index_c_check = 0
                if color == "white":
                    index_r_check += index_r
                    index_c_check += index_c
                    if self._board[index_r_check][index_c_check] == "O":
                        while self._board[index_r_check - 1][index_c_check + 1] == "X":
                            index_r_check -= 1
                            index_c_check += 1
                        if self._board[index_r_check - 1][index_c_check + 1] == "." \
                                and self._board[index_r_check][index_c_check] != "O":
                            position = (index_r_check - 1, index_c_check + 1)
                            self._position_list_w.append(position)
                    index_r_check = 0
                    index_c_check = 0

    def check_diagonal_down_right(self, color):
        """Takes color as a parameter.
        color - represents which color piece the player is using.
        Used by return_available_positions method to determine if spaces adjacent
        and diagonal down right is a valid move. If not, this method returns nothing. If yes, adds position to
        list of available positions."""

        index_r_check = 0
        index_c_check = 0

        for index_r, row in enumerate(self._board):
            for index_c, column in enumerate(row):
                if color == "black":
                    index_r_check += index_r
                    index_c_check += index_c
                    if self._board[index_r_check][index_c_check] == "X":
                        while self._board[index_r_check + 1][index_c_check + 1] == "O":
                            index_r_check += 1
                            index_c_check += 1
                        if self._board[index_r_check + 1][index_c_check + 1] == "." \
                                and self._board[index_r_check][index_c_check] != "X":
                            position = (index_r_check + 1, index_c_check + 1)
                            self._position_list_b.append(position)
                    index_r_check = 0
                    index_c_check = 0
                if color == "white":
                    index_r_check += index_r
                    index_c_check += index_c
                    if self._board[index_r_check][index_c_check] == "O":
                        while self._board[index_r_check + 1][index_c_check + 1] == "X":
                            index_r_check += 1
                            index_c_check += 1
                        if self._board[index_r_check + 1][index_c_check + 1] == "." \
                                and self._board[index_r_check][index_c_check] != "O":
                            position = (index_r_check + 1, index_c_check + 1)
                            self._position_list_w.append(position)
                    index_r_check = 0
                    index_c_check = 0

    def check_diagonal_up_left(self, color):
        """Takes color as a parameter.
        color - represents which color piece the player is using.
        Used by return_available_positions method to determine if spaces adjacent
        and diagonal up left is a valid move. If not, this method returns nothing. If yes, adds position to
        list of available positions."""

        index_r_check = 0
        index_c_check = 0

        for index_r, row in enumerate(self._board):
            for index_c, column in enumerate(row):
                if color == "black":
                    index_r_check += index_r
                    index_c_check += index_c
                    if self._board[index_r_check][index_c_check] == "X":
                        while self._board[index_r_check - 1][index_c_check - 1] == "O":
                            index_r_check -= 1
                            index_c_check -= 1
                        if self._board[index_r_check - 1][index_c_check - 1] == "." \
                                and self._board[index_r_check][index_c_check] != "X":
                            position = (index_r_check - 1, index_c_check - 1)
                            self._position_list_b.append(position)
                    index_r_check = 0
                    index_c_check = 0
                if color == "white":
                    index_r_check += index_r
                    index_c_check += index_c
                    if self._board[index_r_check][index_c_check] == "O":
                        while self._board[index_r_check - 1][index_c_check - 1] == "X":
                            index_r_check -= 1
                            index_c_check -= 1
                        if self._board[index_r_check - 1][index_c_check - 1] == "." \
                                and self._board[index_r_check][index_c_check] != "O":
                            position = (index_r_check - 1, index_c_check - 1)
                            self._position_list_w.append(position)
                    index_r_check = 0
                    index_c_check = 0

    def check_diagonal_down_left(self, color):
        """Takes color as a parameter.
        color - represents which color piece the player is using.
        Used by return_available_positions method to determine if spaces adjacent
        and diagonal down left is a valid move. If not, this method returns nothing. If yes, adds position to
        list of available positions."""

        index_r_check = 0
        index_c_check = 0

        for index_r, row in enumerate(self._board):
            for index_c, column in enumerate(row):
                if color == "black":
                    index_r_check += index_r
                    index_c_check += index_c
                    if self._board[index_r_check][index_c_check] == "X":
                        while self._board[index_r_check + 1][index_c_check - 1] == "O":
                            index_r_check += 1
                            index_c_check -= 1
                        if self._board[index_r_check + 1][index_c_check - 1] == "." \
                                and self._board[index_r_check][index_c_check] != "X":
                            position = (index_r_check + 1, index_c_check - 1)
                            self._position_list_b.append(position)
                    index_r_check = 0
                    index_c_check = 0
                if color == "white":
                    index_r_check += index_r
                    index_c_check += index_c
                    if self._board[index_r_check][index_c_check] == "O":
                        while self._board[index_r_check + 1][index_c_check - 1] == "X":
                            index_r_check += 1
                            index_c_check -= 1
                        if self._board[index_r_check + 1][index_c_check - 1] == "." \
                                and self._board[index_r_check][index_c_check] != "O":
                            position = (index_r_check + 1, index_c_check - 1)
                            self._position_list_w.append(position)
                    index_r_check = 0
                    index_c_check = 0

    def return_available_positions(self, color):
        """ Takes color as a parameter.
        color - represents which color piece the player is using.
        Depending on which color player, this function adds available positions to their respective position list.
        Returns the list of possible positions for the player with the given color to move on the current board."""

        if color == "black":
            self._position_list_b = []
            self.check_up(color)
            self.check_right(color)
            self.check_down(color)
            self.check_left(color)
            self.check_diagonal_up_right(color)
            self.check_diagonal_down_right(color)
            self.check_diagonal_up_left(color)
            self.check_diagonal_down_left(color)
            return self._position_list_b

        if color == "white":
            self._position_list_w = []
            self.check_up(color)
            self.check_right(color)
            self.check_down(color)
            self.check_left(color)
            self.check_diagonal_up_right(color)
            self.check_diagonal_down_right(color)
            self.check_diagonal_up_left(color)
            self.check_diagonal_down_left(color)
            return self._position_list_w

    def make_move(self, color, piece_position):
        """ Takes color and piece position as parameters.
        color - represents which color piece the player is using.
        piece_position - a tuple that represents the position of the player's piece.
        Puts a piece of the specified color at the given position and updates the board accordingly,
        then returns the current board(as a 2d list). Used by play_game method but can also be used alone for testing."""

        row, column = piece_position

        r_check = 0
        c_check = 0

        if color == "black":
            self._board[row][column] = "X"
            r_check += row
            c_check += column

            while self._board[r_check - 1][column] == "O":  # checks up
                self._board[r_check - 1][column] = "X"
                r_check -= 1
            r_check = 0
            r_check += row

            while self._board[row][c_check + 1] == "O":  # checks right
                self._board[row][c_check + 1] = "X"
                c_check += 1
            c_check = 0
            c_check += column

            while self._board[r_check + 1][column] == "O":  # checks down
                self._board[r_check + 1][column] = "X"
                r_check += 1
            r_check = 0
            r_check += row

            while self._board[row][c_check - 1] == "O":  # checks left
                self._board[row][c_check - 1] = "X"
                c_check -= 1
            c_check = 0
            c_check += column

            while self._board[r_check - 1][c_check + 1] == "O":  # checks diagnonal up right
                self._board[r_check - 1][c_check + 1] = "X"
                r_check -= 1
                c_check += 1
            r_check = 0
            r_check += row
            c_check = 0
            c_check += column

            while self._board[r_check + 1][c_check + 1] == "O":  # checks diagnonal down right
                self._board[r_check + 1][c_check + 1] = "X"
                r_check += 1
                c_check += 1
            r_check = 0
            r_check += row
            c_check = 0
            c_check += column

            while self._board[r_check + 1][c_check - 1] == "O":  # checks diagnonal down left
                self._board[r_check + 1][c_check - 1] = "X"
                r_check += 1
                c_check -= 1
            r_check = 0
            r_check += row
            c_check = 0
            c_check += column

            while self._board[r_check - 1][c_check - 1] == "O":  # checks diagnonal up left
                self._board[r_check - 1][c_check - 1] = "X"
                r_check -= 1
                c_check -= 1
            r_check = 0
            r_check += row
            c_check = 0
            c_check += column

        if color == "white":
            self._board[row][column] = "O"
            r_check += row
            c_check += column

            while self._board[r_check - 1][column] == "X":  # checks up
                self._board[r_check - 1][column] = "O"
                r_check -= 1
            r_check = 0
            r_check += row

            while self._board[row][c_check + 1] == "X":  # checks right
                self._board[row][c_check + 1] = "O"
                c_check += 1
            c_check = 0
            c_check += column

            while self._board[r_check + 1][column] == "X":  # checks down
                self._board[r_check + 1][column] = "O"
                r_check += 1
            r_check = 0
            r_check += row

            while self._board[row][c_check - 1] == "X":  # checks left
                self._board[row][c_check - 1] = "O"
                c_check -= 1
            c_check = 0
            c_check += column

            while self._board[r_check - 1][c_check + 1] == "X":  # checks diagnonal up right
                self._board[r_check - 1][c_check + 1] = "O"
                r_check -= 1
                c_check += 1
            r_check = 0
            r_check += row
            c_check = 0
            c_check += column

            while self._board[r_check + 1][c_check + 1] == "X":  # checks diagnonal down right
                self._board[r_check + 1][c_check + 1] = "O"
                r_check += 1
                c_check += 1
            r_check = 0
            r_check += row
            c_check = 0
            c_check += column

            while self._board[r_check + 1][c_check - 1] == "X":  # checks diagnonal down left
                self._board[r_check + 1][c_check - 1] = "O"
                r_check += 1
                c_check -= 1
            r_check = 0
            r_check += row
            c_check = 0
            c_check += column

            while self._board[r_check - 1][c_check - 1] == "X":  # checks diagnonal up left
                self._board[r_check - 1][c_check - 1] = "O"
                r_check -= 1
                c_check -= 1
            r_check = 0
            r_check += row
            c_check = 0
            c_check += column

        return self._board

    def play_game(self, player_color, piece_position):
        """ Takes color and piece position as parameters.
        player_color - represents which color piece the player is using.
        piece_position - a tuple that represents the position of the player's piece.
        Attempts to make a move for the player with the given color at the specified position.
        If the position the player wants to move is invalid, the function does not make any move and
        returns "Invalid move". It also prints out this message
        "Here are the valid moves:" followed by a list of possible positions.
        If no valid moves exist then the returned list is empty. If the position is valid,
        the function makes that move and updates the board. If the game ends at that point,
        the function prints "Game is ended white piece: number black piece: number" and
        calls the return_winner method."""


        if self.return_available_positions("white") == [] and self.return_available_positions("black") == []:
            self.return_winner()
            print("Game is ended white piece: " + str(self._white_count) + " black piece: " + str(self._black_count))

        if player_color == "black":
            if piece_position not in self.return_available_positions("black") \
                    and self.return_available_positions("black") != []:
                print("Here are the valid moves: " + str(self.return_available_positions("black")))
                return "Invalid move"

            if self.return_available_positions("black") == []:
                return self.return_available_positions("black")

            if piece_position in self.return_available_positions("black"):
                self.make_move(player_color, piece_position)

        if player_color == "white":
            if piece_position not in self.return_available_positions("white") \
                    and self.return_available_positions("white") != []:
                print("Here are the valid moves: " + str(self.return_available_positions("white")))
                return "Invalid move"

            if self.return_available_positions("white") == []:
                return self.return_available_positions("white")

            if piece_position in self.return_available_positions("white"):
                self.make_move(player_color, piece_position)
