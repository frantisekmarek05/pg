from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        direction = 1 if self.color == 'white' else -1

        if self.is_position_on_board((row + direction, col)):
            moves.append((row + direction, col))

        if (self.color == 'white' and row == 2) or (self.color == 'black' and row == 7):
            if self.is_position_on_board((row + 2 * direction, col)):
                moves.append((row + 2 * direction, col))

        if self.is_position_on_board((row + direction, col + 1)):
            moves.append((row + direction, col + 1))
        if self.is_position_on_board((row + direction, col - 1)):
            moves.append((row + direction, col - 1))

        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        directions = [
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        moves = []
        for direction in directions:
            for i in range(1, 8):
                new_row = row + i * direction[0]
                new_col = col + i * direction[1]
                if self.is_position_on_board((new_row, new_col)):
                    moves.append((new_row, new_col))
                else:
                    break
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        moves = []
        for direction in directions:
            for i in range(1, 8):
                new_row = row + i * direction[0]
                new_col = col + i * direction[1]
                if self.is_position_on_board((new_row, new_col)):
                    moves.append((new_row, new_col))
                else:
                    break
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        moves = []
        for direction in directions:
            for i in range(1, 8):
                new_row = row + i * direction[0]
                new_col = col + i * direction[1]
                if self.is_position_on_board((new_row, new_col)):
                    moves.append((new_row, new_col))
                else:
                    break
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        moves = []
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if self.is_position_on_board((new_row, new_col)):
                moves.append((new_row, new_col))
        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())