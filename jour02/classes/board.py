class Board:
    
    def __init__(self,i,j):
        self.__i = i
        self.__j = j
        self.__board_array = self.__matrice_builder()
    
    def __matrice_builder(self):
        cols = self.__i
        rows = self.__j
        matrice = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append('O')
            matrice.append(row)
        return matrice
    
    def get_board_array_for_client(self):
        for col in range(len(self.__board_array[0])):
            arr = []
            for row in range(0, len(self.__board_array)):
                arr.append(self.__board_array[row][col])
            print(arr)

    def play(self,emplacement_pion,couleur_pion):
        if(emplacement_pion > len(self.__board_array) - 1):
            return

        for i in range(0,len(self.__board_array[emplacement_pion])):
            if(self.__board_array[emplacement_pion][i] != 'O'):
                if(i == 0):
                    break
                self.__board_array[emplacement_pion][i - 1] = couleur_pion
                break
            if(i == len(self.__board_array[emplacement_pion]) - 1):
                self.__board_array[emplacement_pion][i] = couleur_pion
                break
    
    def start_game(self):
        move_played = False
        while(self.__check_if_someone_win() == None):
            if(move_played != True):
                index = input("C'est au tour des Rouges ! Donne l'index que tu veux jouer : ")
                self.play(int(index),"R")
                move_played = True
                self.get_board_array_for_client()
            else:
                index = input("C'est au tour des Jaunes ! Donne l'index que tu veux jouer : ")
                self.play(int(index),"J")
                move_played = False
                self.get_board_array_for_client()
        if(self.__check_if_someone_win() == "R"):
            print("Le joueur rouge a gagné !")
        else:
            print("Le joueur jaune a gagné !")
      
    def __check_columns(self,max_align):  
        for row in self.__board_array:
            temp_cell = ""
            num_align = max_align
            for cell in row:
                if cell == temp_cell and cell != 'O':
                    num_align += max_align
                    if num_align == 4:
                        return temp_cell
                else:
                    temp_cell = cell
                    num_align = 1
        return None

    def __check_diagonals(self,max_align):
        # Vérification des diagonales du haut vers le bas
        for i in range(len(self.__board_array) - 3):
            for j in range(len(self.__board_array[0]) - 3):
                cell = self.__board_array[i][j]
                if cell != 'O' and cell == self.__board_array[i+1][j+1] and cell == self.__board_array[i+2][j+2] and cell == self.__board_array[i+3][j+3]:
                    return cell
        # Vérification des diagonales du bas vers le haut
        for i in range(3, len(self.__board_array)):
            for j in range(len(self.__board_array[0]) - 3):
                cell = self.__board_array[i][j]
                if cell != 'O' and cell == self.__board_array[i-1][j+1] and cell == self.__board_array[i-2][j+2] and cell == self.__board_array[i-3][j+3]:
                    return cell
        
        return None

    def __check_rows(self,max_align):
        for col in range(len(self.__board_array[0])):
            num_align = 1
            for row in range(1, len(self.__board_array)):
                if self.__board_array[row][col] == self.__board_array[row-1][col] and self.__board_array[row][col] != 'O':
                    num_align += 1
                    if num_align == 4:
                        return self.__board_array[row][col]
                else:
                    num_align = 1
        return None

    def __check_if_someone_win(self):
        winner = self.__check_columns()
        if(winner != None):
            return winner
        winner = self.__check_rows()
        if(winner != None):
            return winner
        winner = self.__check_diagonals()
        if(winner != None):
            return winner
        return None