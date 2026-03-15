"""
This file implements the page class which is responsible for handling tuples with a slotted arrays data structure for optimal disk usage.
"""

"""
-------------
Page's APIs
-------------

0. is_root()            Returns True if its the root page else False
1. get_header()         Remember: header length is dependent on whether or not the page is a root or not
2. 

"""


from config.file_config import ROOT_PAGE_HEADER_SIZE, BTREE_PAGE_HEADER_SIZE, PAGE_SIZE
from storage_engine.disk_manager import DiskManager


class Page:
    # 1. Page Header
    # 2. Slotted array
    # a. input a tuple

    # Just storing sequentially for now.
    # Keep track of page header offset and page offset

    TUPLE_SIZE_BYTES = 20
    PAGE_NUMBER = None

    filer = DiskManager()

    def __init__(self, page_number):
        self.PAGE_NUMBER = page_number

    def is_root(self):
        """Very simple for now"""
        return True if self.PAGE_NUMBER == 0 else False

    def get_header(self):
        if self.is_root():
            seek = PAGE_SIZE * self.PAGE_NUMBER
            self.filer.read_bytes(n=BTREE_PAGE_HEADER_SIZE, s=seek)
        else:
            self.filer.read_bytes(n=ROOT_PAGE_HEADER_SIZE, s=0)


if __name__ == "__main__":
    page = Page()
