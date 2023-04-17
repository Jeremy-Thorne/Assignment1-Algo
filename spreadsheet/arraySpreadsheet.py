from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        
        self.spreadSheet = []
        self.numCols = 0
        self.numRows = 0

    def printSheet(self):
        for row in self.spreadSheet:
            print(row)

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """           
        
        for cell in lCells:
            if cell.row > self.numRows:
                self.numRows = cell.row + 1
            if cell.col > self.numCols: 
                self.numCols = cell.col + 1

        self.numRows += 1
        self.numCols += 1
            
        #spreadsheet = [[None for i in range(self.numCols)] for j in range(self.numRows)]
 
        for i in range(self.numRows):
            col = []
            for j in range(self.numCols):
                col.append(None)
            self.spreadSheet.append(col)
            
        
        try:
            for cell in lCells:
                self.spreadSheet[cell.row][cell.col] = cell.val
        except BaseException as e:
            print(e)
            print(len(self.spreadSheet), self.numRows, len(self.spreadSheet[0]), self.numCols)
            print("error",cell.row, cell.col)


    def appendRow(self)->bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        try:        
            self.spreadSheet.append([None for i in range(self.numCols)])
            self.numRows += 1 
            return True
        except:
            return False


    def appendCol(self)->bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        try:        
            for i in range(self.numRows): self.spreadSheet[i].append(None)  
            self.numCols += 1             
            return True      
        except:
            return False


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        try:        
            if rowIndex > 0:
                self.spreadSheet.insert(rowIndex, [None for i in range(self.numCols)])
                self.numRows += 1 
                return True
            return False
        except:
            return False


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        try:      
            if colIndex > 0:  
                for i in range(self.numRows): self.spreadSheet[i].insert(colIndex,None)
                self.numCols += 1                   
                return True
            return False
        except:
            return False


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        try:     
            self.spreadSheet[rowIndex][colIndex] = value          
            return True
        
        except:
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
        for i in range(self.numRows):
            for j in range(self.numCols):
                currVal = self.spreadSheet[i][j]
                if currVal == value:
                    cellList.append([i,j,currVal])

        return cellList




    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        cellList = []
        for i in range(self.numRows):
            for j in range(self.numCols):
                currVal = self.spreadSheet[i][j]
                if currVal != None:
                    cellList.append(Cell(i,j,currVal))

        return cellList

