import pygame
from Cell import Cell
from sudoku_generator import *
class Board:
      def __init__(self, width, height, screen, difficulty):
            """ The constructor for the board class
                  the Initial the variable 
                  width: width of sodoku board in pixels
                  height: height of the sudoku board in pixels
                  screen: the pygame screen where the board is draw
                  difficulty: chosen by user('esay', 'medium', 'hard')
            """
            self.width = width
            self.height = height
            self.screen = screen 
            self.difficulty = difficulty
            self.cell_size = 600 / 9 # Calculates cell size by dividing board width by 9 (standard Sudoku grid)
            self.board = generate_sudoku(9,difficulty) 
            self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
            self.space_cells = []
            
      def draw(self):
            """
                  Draw the Sudoku board
            """

            self.screen.fill((20,51,205))
            for i in range(10):
                  if i % 3 == 0: # thicker line width 3 every 3 cells which 3x#
                        line_width = 3 
                  else: # thinner line for other grid lines as 9x9 
                        line_width = 1 
                  pygame.draw.line( # Draws vertical lines across the board for each lines at multiple of cell size
                        self.screen,
                        (0,0,0), # Black color
                        (i * self.cell_size, 0),
                        (i * self.cell_size, self.width),
                        line_width
                  )
                  pygame.draw.line( # Draws Horizontal lines across the board for each lines at multiple of cell size
                        self.screen,
                        (0,0,0), # Black color
                        (0, i * self.cell_size),
                        (self.height, i * self.cell_size),
                        line_width
                  )
                  #Draws each individual cell in the grid
            for cells in self.cells:
                  for cell in cells:
                        cell.draw()

      
      def select(self, row, col): 
            # Marks the cell at (row, col) as the selected cell.
            # deselct any previously selected cell
            for cells in self.cells:  # Provides visual feedback to the user about which cell they're currently interacting with
                  for cell in cells:
                        cell.selected = False
            # select the new cell
            self.cells[row][col].selected = True

      
      def click(self, x, y):
      #check if click is within board 
            if 0 <= x <= self.width and 0 <= y <= self.height:
                  # Calculate row and col base on click coordinates
                  row = y // self.cell_size
                  col = x // self.cell_size
                  return [round(row), round(col)]
            return None

      def clear(self):
      # only clear if a cell is sleected and not locked
            for i in range(9):
                  for j in range(9):
                        if self.cells[i][j].selected:
                              if self.cells[i][j].exist == False:
                                    self.cells[i][j].value = 0
                                    self.cells[i][j].sketch = 0
                              
            

      def sketch(self, value):
            """
                  Sets a sketched value for the selected cell.
                  """
            for cells in self.cells:
                  for cell in cells:
                        if cell.selected:
                              cell.set_sketched_value(value)

      def place_number(self, value):
            """
                  Sets the final value for the selected cell.
            """
            self.find_empty()
            for row in range(9):
                  for col in range(9):
                        if self.cells[row][col].selected == True:
                              if(row,col) in self.space_cells:
                                    self.cells[row][col].set_cell_value(value)


      def reset_to_original(self):
            for i in range(9):
                  for j in range(9):
                        if(i , j) in self.space_cells:
                              self.cells[i][j].set_cell_value(0)
                              self.cells[i][j].set_sketched_value(0)
                              self.cells[i][j].selected = False

      def is_full(self):
            for i in range(9):
                  for j in range(9):
                        if self.cells[i][j].value == 0:
                              return False
            return True

      def update_board(self):
            for i in range(9):
                  for j in range(9):
                        self.board[i][j] = self.cells[i][j].value

      def find_empty(self):
            for i in range(9):
                  for j in range(9):
                        if self.cells[i][j].value == 0:
                              self.space_cells.append((i,j))

      def check_board(self):
            for row in self.cells:
                  dic = {}
                  for cell in row:
                        if cell.value != 0:
                              if cell.value in dic:
                                    return False
                        dic[cell.value] = 1
            
            for col in range(9):
                  dic = {}
                  for row in range(9):
                        if self.cells[row][col].value != 0:
                              if self.cells[row][col].value in dic:
                                    return False
                              dic[self.cells[row][col].value] = 1
            
            for box_row in range(0,9,3):
                  for box_col in range(0 , 9 ,3):
                        dic = {}
                        for i in range(3):
                              for j in range(3):
                                    if self.cells[box_row + i][box_col+j].value != 0:
                                          if self.cells[box_row + i][box_col+j].value in dic:
                                                return False
                                          dic[self.cells[box_row + i][box_col+j].value] = 1
            return True



                        
