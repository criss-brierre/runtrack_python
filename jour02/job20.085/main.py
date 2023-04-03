import sys
sys.path.insert(0, '../classes')
from board import Board

class Ai_One():
    def __init__(self, i,j):
        self.i = i
        self.j = j
        self.board = Board(i,j)

    def think(self):
        return self._Board__board_array
    

ai = Ai_One(6,7)


print(ai.think())


        