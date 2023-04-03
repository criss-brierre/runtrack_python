class Chess:
    def __init__(self,n):
        self.__n = n
        self.__board_array = self.__matrice_builder()

    def __matrice_builder(self):
        cols = self.__n
        matrice = []
        for i in range(cols):
            row = []
            for j in range(cols):
                row.append('O')
            matrice.append(row)
        return matrice
    
    def puissance(self,x,n):
        if n == 0:
            return 1
        return x*self.puissance(x,n-1)
        
chess = Chess(0)
            
print(chess.puissance(5,3))

        



