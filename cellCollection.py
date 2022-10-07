class CellCollection:
    def __init__(self, cells):
        self.cells = {}
        for cell in cells:
            self.cells[cell.getCellNum()] = cell
        self.cellNumList = list(cells)
        self.cellNumIndex = 0
    
    def __contains__(self, cellNum):
        return cellNum in self.cells
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cellNumIndex < len(self.cells):
            self.cellNumIndex += 1
            return self.cellNumIndex
        else:
            raise StopIteration