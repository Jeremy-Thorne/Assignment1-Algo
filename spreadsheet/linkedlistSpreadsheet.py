from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, val: float):

        self.down = None
        self.right = None
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
        for i in range(self.rows+1):
            currCol = currRow
            for j in range(self.cols):
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
            if cell.row > self.rows: self.rows = cell.row
            if cell.col > self.cols: self.cols = cell.col

        currNode = self.head
        for i in range(self.rows):   

            currNode.down = ListNode(None)
            currColNode = currNode
            currNode = currNode.down

            for j in range(self.cols):
                currColNode.right = ListNode(None)
                currColNode = currColNode.right

        for cell in lCells:
            currNode = self.head
            for i in range(cell.row-1):
                currNode = currNode.down

            for j in range(cell.col-1):
                currNode = currNode.right
            currNode.val = cell.val

    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """

        currNode = self.head
        for i in range(self.rows):
            currNode = currNode.down

        currNode.down = ListNode(None)
        currNode = currNode.down

        for j in range(self.cols):
            currNode.right = ListNode(None)
            currNode = currNode.right
        
        return True


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """


        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """


        return False


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """

        return False


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        if rowIndex < self.rows or colIndex < self.cols:
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



        return cellList


    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        cellList = []


        return cellList
