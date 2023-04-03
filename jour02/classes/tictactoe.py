class TicTacToe():
    def __init__(self):
        self.board = self.__array_builder()
        self.all_possibilities_to_win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    def __array_builder(self):
        rows_and_cols = 3 * 3
        matrice = []
        for i in range(0,rows_and_cols):
            matrice.append("-")
        return matrice

    def check_if_someone_win(self):
        for possibilities_to_win in self.all_possibilities_to_win:
            if(self.board[possibilities_to_win[0]] != '-' and self.board[possibilities_to_win[0]] == self.board[possibilities_to_win[1]] and
            self.board[possibilities_to_win[0]] == self.board[possibilities_to_win[2]]):
                return self.board[possibilities_to_win[0]]
        return None
    
    def __play(self,emplacement,pion):
        if(emplacement >= len(self.board)):
            return False
        
        if(self.board[emplacement] != '-'):
            return False
        else:
            self.board[emplacement] = pion
            return True
    
    def __display_in_console(self):
        count = 1
        returned_array = []
        temp_array= []
        for i in range(len(self.board)):
            temp_array.append(self.board[i])
            if(count % 3 == 0):
                # returned_array.append(temp_array)
                print(temp_array)
                temp_array.clear()
            count += 1


    def launch_game(self):
        winner = self.check_if_someone_win()
        played = False
        while(winner == None):
            if(played == False):
                x = input("A toi joueur X ! à quel index veux-tu mettre jouer : ")
                while(x is str and int(x) > 8 or int(x) < 0):
                    x = input("L'input doit être un nombre compris entre 0 et 8 : ")
                self.__play(int(x),"X")
                played = True
                winner = self.check_if_someone_win()
            else:
                o = input("A toi joueur O ! à quel index veux-tu mettre jouer : ")
                while(int(o) > 8 or int(o) < 0):
                    o = input("L'input doit être un nombre compris entre 0 et 8 : ")
                self.__play(int(o),"O")
                played = False
                winner = self.check_if_someone_win()
            self.__display_in_console()
        
        print(f'Bravo {winner} ! Tu as gagné')