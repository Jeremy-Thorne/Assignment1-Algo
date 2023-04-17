from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------




class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.numCols = 0
        self.numRows = 0
        self.ColA = []
        self.ValA = []
        self.SumA = []

    def printSheet(self):
        print(self.ColA,
                self.ValA,
                self.SumA)

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        self.ColA = []
        self.ValA = []
        self.SumA = []
        cellList = []

        for cell in lCells:
            if cell.row > self.numRows: self.numRows = cell.row + 1
            if cell.col > self.numCols: self.numCols = cell.col + 1

        for cell in lCells: cellList.append([cell.row, cell.col, cell.val])

        cumulativeVal = 0
        cellList = sorted(cellList)
        for i in range(self.numRows):
            for cell in cellList:
                if cell[0] == i:
                    self.ColA.append(cell[1]) 
                    self.ValA.append(cell[2])
                    cumulativeVal += cell[2]
            self.SumA.append(cumulativeVal)

    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        self.SumA.append(self.SumA[len(self.SumA) - 1])
        self.numRows += 1
        return True

    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        self.numCols += 1
        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        if(rowIndex > 0 and rowIndex < (self.numRows)):
            self.SumA.insert(rowIndex, self.SumA[rowIndex])
            self.numRows += 1
            return True
        else:
            return False
    
    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        if(colIndex > 0 and colIndex < (self.numCols)):
            for i in range(len(self.ColA)):
                if self.ColA[i] > colIndex:
                    self.ColA[i] = self.ColA[i] + 1
            self.numCols += 1
            return True
        else:
            return False

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        if(colIndex > 0 and colIndex < (self.numCols) and rowIndex > 0 and rowIndex < (self.numRows)):
            currentSum = 0
            valIndex = 0
            rowCount = 0
            for i in range(len(self.SumA)):
                while currentSum != self.SumA[i]:
                    currentSum += self.ValA[valIndex]
                    valIndex += 1
                    if i == rowIndex:
                        valIndex -= 1
                        rowCount += 1
                if i == rowIndex - 1:
                    break        
            while True:
                if valIndex >= len(self.ColA):
                    self.ColA.append(colIndex)
                    self.ValA.append(value)
                    for index, sum in enumerate(self.SumA):
                        if index >= rowIndex:
                            self.SumA[index] += value
                    break
                if colIndex == self.ColA[valIndex]:
                    self.SumA[rowIndex] += value - self.ValA[valIndex] 
                    for index, sum in enumerate(self.SumA):
                        if index > rowIndex:
                            self.SumA[index] = self.SumA[index] + (value - self.ValA[valIndex])
                    self.ColA[valIndex] = colIndex
                    self.ValA[valIndex] = value               
                    break
                if colIndex < self.ColA[valIndex] or rowCount <= 0:
                    for index, sum in enumerate(self.SumA):
                        if index >= rowIndex:
                            self.SumA[index] += value
                    self.ColA.insert(valIndex, colIndex)
                    self.ValA.insert(valIndex, value)
                    break

                colIndex += 1
                rowCount -= 1

            return True
        else:
            return False

    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        return self.numRows


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        return self.numCols




    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        cellList = []
        currentSum = 0
        valIndex = 0
        currRow = 0
        for i in range(len(self.SumA)):
            while currentSum != self.SumA[i]:
                currentSum += self.ValA[valIndex]
                if self.ValA[valIndex] == value: cellList.append([currRow, self.ColA[valIndex], value])
                valIndex += 1
            currRow += 1            
        return cellList




    def entries(self) -> [Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """
        
        cellList = []
        currentSum = 0
        valIndex = 0
        currRow = 0
        for i in range(len(self.SumA)):
            while currentSum != self.SumA[i]:
                currentSum += self.ValA[valIndex]                     
                cellList.append(Cell(currRow, self.ColA[valIndex], self.ValA[valIndex]))
                valIndex += 1
            currRow += 1

        return cellList