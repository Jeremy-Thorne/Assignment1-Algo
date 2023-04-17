from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, val: float):

        self.down = None
        self.right = None
        self.up = None
        self.left = None
        self.val = val

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.head = ListNode(None)

    def printSheet(self):
        currRow = self.head
        while currRow is not None:
            currCol = currRow
            while currCol is not None:
                print(currCol.val, end=' ')
                currCol = currCol.right
            currRow = currRow.down

            print()


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        for cell in lCells:
            if cell.row > self.rows: self.rows = cell.row + 1
            if cell.col > self.cols: self.cols = cell.col + 1

        currNode = self.head
        for i in range(self.rows):   

            currNode.down = ListNode(None)
            currColNode = currNode
            currNode.down.up = currNode
            currNode = currNode.down     

            for j in range(self.cols-1):
                currColNode.right = ListNode(None)
                currColNode.right.left = currColNode 
                currColNode = currColNode.right

        for cell in lCells:
            currNode = self.head
            for i in range(cell.row):
                currNode = currNode.down

            for j in range(cell.col):
                currNode = currNode.right
            currNode.val = cell.val

    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """

        currNode = self.head
        for i in range(self.rows-1):
            currNode = currNode.down

        currNode.down = ListNode(None)
        currNode = currNode.down

        for j in range(self.cols-1):
            currNode.right = ListNode(None)
            currNode.right.left = currNode
            currNode = currNode.right
        self.rows +=1
        return True


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        rowNode = self.head
        while rowNode is not None:
            currNode = rowNode
            while currNode.right is not None:
                currNode = currNode.right
            currNode.right = ListNode(None)
            currNode.right.left = currNode
            rowNode = rowNode.down
        self.cols +=1
        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        if rowIndex > 0 and rowIndex < self.rows:
            currNode = self.head
            for i in range(rowIndex):
                currNode = currNode.down
            tempUp = currNode.up
            currNode.up = ListNode(None)
            currNode.up.down = currNode
            currNode.up.up = tempUp
            if tempUp is not None:
                tempUp.down = currNode.up
            else:
                tempUp = ListNode(2)
            currNode = currNode.up
            self.rows +=1
            for j in range(self.cols-1):
                currNode.right = ListNode(None)
                currNode.right.left = currNode 
                currNode = currNode.right
            return True
        
        elif rowIndex == 0:
            currNode = self.head
            currNode.up = ListNode(None)
            currNode.up.down = currNode
            currNode = currNode.up

            for j in range(self.cols-1):
                currNode.right = ListNode(None)
                currNode.right.left = currNode 
                currNode = currNode.right
            self.rows +=1
            return True

        return False

    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """

        try:
            rowNode = self.head
            while rowNode is not None:
                currNode = rowNode
                for i in range(colIndex-1):
                    currNode = currNode.right
                tempLeft = currNode.left
                currNode.left = ListNode(None)
                currNode.left.right = currNode
                if tempLeft is not None:
                    tempLeft.right = currNode.left
                rowNode = rowNode.down
            self.cols +=1
        except:
            self.printSheet()
        return True


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        if rowIndex >= 0 and rowIndex < self.rows and colIndex >= 0 and colIndex < self.cols:
            currNode = self.head
            for i in range(rowIndex):
                currNode = currNode.down
            for i in range(colIndex):
                currNode = currNode.right
            currNode.val = value
            return True
        else:
            return False


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        return self.rows


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        return self.cols


    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        
        cellList = []

        rowCount = 0
        currRow = self.head
        while currRow is not None:
            colCount = 0
            currCol = currRow
            while currCol is not None:
                if currCol.val == value or (value == -0.123456789 and currCol.val is not None):
                    cellList.append([rowCount,colCount,currCol.val])
                currCol = currCol.right
                colCount += 1
            currRow = currRow.down
            rowCount += 1
        return cellList


    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        cellList = []

        for cell in self.find(-0.123456789): cellList.append(Cell(cell[0], cell[1], cell[2]))

        return cellList
