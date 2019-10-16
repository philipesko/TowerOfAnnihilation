import string
from config import MAIN_MENU_BUTTON, NAME_PROJECT, PATH_TO_RESOURCE, MAIN_SIZE_FOR_WINDOW


class Grid:

    def __init__(self):

        # Defining grid
        self.grid = []

        # Defining cell size
        self.cell = (58, 58)

        # Number of cells on X axis
        self.x_cells_quantity = int(MAIN_SIZE_FOR_WINDOW[0] / self.cell[0])
        self.row = self.define_cell_list(self.x_cells_quantity)
        
        # Number of cells on Y axis
        self.y_cells_quantity = int(MAIN_SIZE_FOR_WINDOW[1] / self.cell[1])
        self.string = self.define_cell_list(self.y_cells_quantity)
        # self.grid_cell_names()
        self.convert_to_dict(self.row)
        # Grid list
        self.grid.append(self.row)
        self.grid.append(self.string)
        print(f'Two lists: {self.grid}')


    def define_cell_list(self, cell_quantity):
        """
        Making list for a row or a string
        """
        # Defining empty row/string list
        list_obj = []
        # Making list
        for cell_quantity in range(0, cell_quantity):
            cell_quantity = (cell_quantity + 1)
            list_obj.append(cell_quantity)
        return list_obj


    def grid_cell_names(self):
        """
        Generating cell names like '(1,1)', '(1,2)'...
        """
        self.cell_names = []
        self.row = [self.row [i:i + 1] for i in range(len(self.row))]
        self.string = [self.string [i:i + 1] for i in range(len(self.string))]
        
        # print(f'    ROWS: {self.row}, \n    STRINGS {self.string}')
        # for y in self.row:
        #     for 

    def convert_to_dict(self, input_list):

        self.dictionary = dict.fromkeys(input_list, None)
        print(f'DICTIONARY: {self.dictionary}')

    # def grid_coords(self):
        


"""
вопросы на вечер:
Строка 37: почему, если в скобках сделать "-1", то будет то, что будет (продемонстрировать)
Строка 39: почему в итоге идёт отсчёт не с нуля? Как сделать с нуля? Вручную задать? Нужно ли это?
строка 47, 48: объяснить синтаксис
в init checkpos и расположение инициализации класса
как разделить словарь на список словарей из convert to dict?
"""

    # def generate_cell_names(self):
    #     self.alphabet = string.ascii_uppercase[0:]
    #     self.names_list = []
    #     print(self.alphabet)
    #     for self.alphabet in range(17):
            


if __name__ == '__main__':
    Grid()
