# Your previous Plain Text content is preserved below:

# You are implementing the computation & storage component of a spreadsheet
# (think Excel or Google Sheets). You have a UI developer who will be
# responsible for, well, User Interaction (rendering, handling user input,
# etc).

# We will be providing the UI developer two functions:

# 1. set_cell - to be used like `set_cell("C1", "45")` 
#             or, for formulas, `set_cell("C1", "=A1+B1")`
# 2. get_value - ie, `get_value("C1")`, and return an integer value.
 
# We will not be implementing all of a spreadsheet's features, but we need the
# ability for a cell to refer to other cells in formulas, and to sum values
# from other cells. 

# When in doubt, bias towards simplicity.

# ===================
# Sample spreadsheet:
# ===================
#     A   B   C
# 1   3   5
# 2           =A1+B1
# ===================

class Spreadsheet:

    def __init__(self):
        self.data = {}

    def sum_cells(self, cells_list):
        result = []
        for cell in cells_list:
            if isinstance(cell, list):
                result.append(self.sum_cells(cell))
            else:
                result.append(self.get_value(cell))  
        return sum(result)

    def set_cell(self, position, value):
        if value[0] == '=':
            cells = value[1:].split('+')
            self.data[position] = cells
        else:
            self.data[position] = int(value)

    def get_value(self, position):
        if position in self.data:
            if isinstance(self.data[position], list):
                return self.sum_cells(self.data[position])
            else:
                return self.data.get(position)
        else:
            raise ValueError(f"Data is missing in position {position}")

res = Spreadsheet()

#TC1
res.set_cell("C1", "45")
print(res.get_value("C1"))

# TC2
res.set_cell("A1", "5")
res.set_cell("B1", "20")
res.set_cell("D5", "30")
res.set_cell("C2", "=A1+B1+D5")
res.set_cell("A1", "100")
print(res.get_value("C2"))