from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: float):

        self.left = None
        self.right = None
        self.up = None
        self.down  = None
        self.word_frequency = word_frequency

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.rows = 0
        self.cols = 0
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.linkedListSpreadsheet = ListNode(None)


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        # TO BE IMPLEMENTED
        for cell in lCells:
            if cell.row > self.rows: 
                self.rows = cell.row + 1 

            if cell.col > self.cols: 
                self.cols = cell.col + 1

        self.linkedListSpreadsheet = [[ListNode(None) for j in range(self.cols)] for i in range(self.rows)]

        for cell in lCells:
           node = self.linkedListSpreadsheet[cell.row - 1][cell.col - 1]
           node.word_frequency = cell.val

        for rows in range(self.rows):
            for cols in range(self.cols):
                node = self.linkedListSpreadsheet[rows][cols]

                if rows > 0:
                    node.up = self.linkedListSpreadsheet[rows - 1][cols]

                if rows < self.rows - 1:
                    node.down = self.linkedListSpreadsheet[rows + 1][cols]

                if cols > 0:
                    node.left = self.linkedListSpreadsheet[rows][cols - 1]

                if cols < self.cols - 1:
                    node.right = self.linkedListSpreadsheet[rows][cols + 1]

        self.head = self.linkedListSpreadsheet[0][0]
        self.tail = self.linkedListSpreadsheet[self.rows - 1][self.cols - 1]


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """

        # TO BE IMPLEMENTED
        try:
            new_row = [ListNode(None) for i in range(self.cols)]

            for i in range(self.cols):
                node = new_row[i]

                if i > 0:
                    node.left = new_row[i - 1]

                if i < self.cols - 1:
                    node.right = new_row[i + 1]

                if len(self.linkedListSpreadsheet) > 0:
                    node.up = self.linkedListSpreadsheet[-1][i]
                    self.linkedListSpreadsheet[-1][i].down = node

            self.linkedListSpreadsheet.append(new_row)
            self.rows += 1
            return True
        
        except:
            return False


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        # TO BE IMPLEMENTED
        try:
            new_col = [ListNode(None) for j in range(self.rows)]

            for j in range(self.rows):
                node = new_col[j]

                if j > 0:
                    node.up = self.linkedListSpreadsheet[j - 1][self.cols - 1]
                    self.linkedListSpreadsheet[j - 1][self.cols - 1].down = node

                if j < self.rows - 1:
                    node.down = self.linkedListSpreadsheet[j + 1][self.cols - 1]
                    self.linkedListSpreadsheet[j + 1][self.cols - 1].up = node

                node.left = self.linkedListSpreadsheet[j][self.cols - 1]
                self.linkedListSpreadsheet[j][self.cols - 1].right = node
            
            self.linkedListSpreadsheet.append(new_col)
            self.cols += 1
            return True
        
        except:
            return False


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        # TO BE IMPLEMENTED
        try:        
            if rowIndex > 0:
                self.linkedListSpreadsheet.insert(rowIndex, [ListNode(None) for i in range(self.cols)])
                self.rows += 1
                return True
            
            else:
                return False
            
        except:
            return False


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """

        # TO BE IMPLEMENTED
        try:      
            if colIndex > 0:  

                for i in range(self.rows): 
                    self.linkedListSpreadsheet[i].insert(colIndex, ListNode(None))

                self.cols += 1                   
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

        # TO BE IMPLEMENTED
        if rowIndex > self.rows or colIndex > self.cols:
            return False
        
        try:
            self.linkedListSpreadsheet[rowIndex - 1][colIndex - 1].word_frequency = value
            return True
        
        except:
            return False


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        return self.rows


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        return self.cols


    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        cellList = []

        for i in range(self.rows):
            for j in range(self.cols):
                currVal = self.linkedListSpreadsheet[i - 1][j - 1].word_frequency

                if currVal == value:
                    cellList.append([i, j, currVal])

        return cellList


    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        # TO BE IMPLEMENTED
        cellList = []

        for i in range(self.rows - 1):
            for j in range(self.cols - 1):
                currVal = self.linkedListSpreadsheet[i][j].word_frequency

                if currVal is not None:
                    cellList.append(Cell(i + 1, j + 1, currVal))

        return cellList
