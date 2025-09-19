import pygame
class Cell:
    def __init__(self, value, row, col, screen):
        """
        Constructor for a single cell in the Sudoku board.
        :param value: The initial value of the cell (0 if empty).
        :param row: The row index of this cell.
        :param col: The column index of this cell.
        :param screen: The PyGame screen where the cell is drawn.
        """
        self.value = value 
        self.row = row
        self.col = col 
        self.screen = screen 
        self.sketch = 0
        self.selected = False
        self.size = 600 / 9  # all the square board 
        # this is create because display window using pygame.display.set_mode((width, height)
        self.exist = True
        if self.value == 0:
            self.exist = False
        self.x = self.row * self.size
        self.y = self.col * self.size
            
    def set_cell_value(self, value):
        """
        Sets the permanent value of this cell.
        :param value: The value to set (any number between 1-9).
        """
        self.value = value
        
    def set_sketched_value(self, value):
        """
        Sets the potential value of this cell.
        :param value: The sketched value to se(any number between 1-9).
        
        """
        self.sketch = value
        
    def draw(self):
        """
            Draw this cell and cotent inside the cell
            If the cell selected, it is outlined in red
            if it has a value, that value is displayed; otherwise, no value is displayed in cell
        """


        value_font = pygame.font.Font(None, 40) # set default font for values
        small_font = pygame.font.Font(None, 25) # smaller font for sketch values
        value = value_font.render(str(self.value), True, (0, 0, 0)) 
        small = small_font.render(str(self.sketch), True, (128,128,128))

        # Draw highlight if selected
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.size, self.size), 3) # red outline  

        # Draw value
        if self.value != 0:
            value_rect = value.get_rect(center = (self.x + self.size // 2, self.y + self.size // 2))
            self.screen.blit(value, value_rect)


        #draw sketch
        elif self.sketch != 0: 
            small_rect = small.get_rect(center = (self.x + 10, self.y + 15))
            self.screen.blit(small, small_rect)
            
            

          

        
        
            
            
        
        
