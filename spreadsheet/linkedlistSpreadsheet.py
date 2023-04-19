from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell
from operator import itemgetter


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
        while currRow.down is not None:
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

        # Get Number of rows and columns to generate
        for cell in lCells:
            if cell.row > self.rows: self.rows = cell.row + 1
            if cell.col > self.cols: self.cols = cell.col + 1

        # Create Empty 2D List
        currNode = self.head

        # Make "Vertical" Linked list of rows
        for i in range(self.rows):   
            currNode.down = ListNode(None)
            currColNode = currNode
            currNode.down.up = currNode
            currNode = currNode.down     
            
            # Make "Horizontal" Linked list of columns attached to rows
            for j in range(self.cols-1):
                currColNode.right = ListNode(None)
                currColNode.right.left = currColNode 
                currColNode = currColNode.right
        
        # Create List of Cells
        cellList = []
        for cell in lCells:
            cellList.append([cell.row,cell.col,cell.val])

        # Sort List
        sorted_list = sorted(cellList, key=itemgetter(0, 1))  

        currNode = self.head
        rowNode = currNode
        previousCol = 0
        previousRow = 0

        # Loop Through List to insert values
        # Current cell data is store to save time in loop
        for i in range(len(sorted_list)):

            rowNum = sorted_list[i][0]

            # Move down to next row value
            for j in range(rowNum - previousRow):
                colNum = 0
                rowNode = rowNode.down
                currNode = rowNode
                previousCol = 0

            colNum = sorted_list[i][1]
            
            # Move across to nex col value
            for k in range(colNum - previousCol):
                currNode = currNode.right

            currNode.val = sorted_list[i][2]
            
            # Store previous cell location
            previousCol = colNum
            previousRow = rowNum  

        
    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """

        # Move last row and add a head row node
        currNode = self.head
        while currNode.down.down is not None:
            currNode = currNode.down
        currNode.down = ListNode(None)
        currNode = currNode.down

        # Add col nodes 
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

        # For each row node
        while rowNode is not None:
            currNode = rowNode

            # Traverse to end col node and add one col to right
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
                tempUp = ListNode(None)
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
        else:
            return False

    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """
        
        if colIndex >= 0 and colIndex < self.cols:
            rowNode = self.head

            # For each row node
            while rowNode is not None and rowNode.down is not None:
                currNode = rowNode

                # Move to colIndex
                for i in range(colIndex-1):
                    if currNode.right is not None:
                        currNode = currNode.right

                # Add node to left of colIndex
                tempLeft = currNode.left
                currNode.left = ListNode(None)
                currNode.left.right = currNode

                # If col index 0
                if tempLeft is not None:
                    tempLeft.right = currNode.left

                rowNode = rowNode.down

            self.cols +=1
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

        if rowIndex >= 0 and rowIndex < self.rows and colIndex >= 0 and colIndex < self.cols:
            currNode = self.head

            # Goto Node at rowIndex, colIndex
            for i in range(rowIndex):
                currNode = currNode.down
            for i in range(colIndex):
                currNode = currNode.right
            
            # Update Value
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

        isFindCommand = -0.123456789

        rowCount = 0
        currRow = self.head

        # Itereate through sheet
        while currRow is not None:
            colCount = 0
            currCol = currRow

            while currCol is not None:
                if currCol.val == value or (value == isFindCommand and currCol.val is not None):
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
        numberToIndicateFind = -0.123456789

        # Reuse Find Function to save code
        for cell in self.find(numberToIndicateFind): cellList.append(Cell(cell[0], cell[1], cell[2]))

        return cellList
