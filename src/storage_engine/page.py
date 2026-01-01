"""
This file implements the page class which is responsible for handling tuples with a slotted arrays data structure for optimal disk usage.
"""
from config import PAGE_SIZE_BYTES

class Page:
    # 1. Page Header
    # 2. Slotted array
        # a. input a tuple 

    # Just storing sequentially for now.
    # Keep track of page header offset and page offset
    TUPLE_SIZE_BYTES = 20

    def __init__(self, page_number):
        # 1. Initilize an internal BTree page first
        # 2. Initilize a leaf BTree page connected to that internal page
        
        # Check if a page corresponding to the given page number exists
        page_buffer = self.read_page(page_number=page_number)
        if (page_buffer == 0):
            # Page doesn't exist
            pass
            # 1. Create an internal page
            internal_page_buffer = bytearray(PAGE_SIZE_BYTES)
            
        elif (page_buffer == PAGE_SIZE_BYTES):
            # Page exists
            pass
        else:
            raise IOError("Incorrect bytes read while trying to read a page")

    def read_page(self, page_number: int):
        """Reads a page from database file"""
        with open(self.DB_FILE, "rb+") as f:
            offset = page_number * self.PAGE_SIZE_BYTES # Page number is expected to be of 0 based indexing
            f.seek(offset)
            return f.read(self.PAGE_SIZE_BYTES)


if __name__ == "__main__":
    page = Page()
