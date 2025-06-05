import numpy as np
import os

class Map:
    def __init__(self, rows, cols, value= None):
        
        self.value = value
        
        if self.value is None:
            self.value = ' '
        
        else:
            self.value = str(value)
       
        self.map = np.full((rows, cols), self.value)
        
    def show_map(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.map:
            print("".join(row))
            
    def import_person(self):
        
        from personagem import Person
        return Person
    
    def update_cell(self, row, col, new_value):
        for i, line in enumerate(new_value):  # percorre as linhas de new_value
            for j, char in enumerate(line):  # percorre os caracteres dentro de cada linha
                
                if not (0 <= row + i < self.map.shape[0] and 0 <= col + j < self.map.shape[1]) : # Verifica se a posição de cada caractere está dentro dos limites do mapa
                    #raise IndexError("Invalid position for character placement")
                    return False
                    
                else:
                    
                    self.map[row + i][col + j] = char
                    
   
            

    def  clear_map(self):
        self.map = np.full((self.map.shape[0], self.map.shape[1]), ' ')

        
        