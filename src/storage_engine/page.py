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


from config.file_config import (
    ROOT_PAGE_HEADER_SIZE,
    DATABASE_HEADER_STRUCTURE,
    BTREE_PAGE_HEADER_SIZE,
    PAGE_SIZE,
)
from exceptions.page import NotRootPageError
from storage_engine.disk_manager import DiskManager


class Page:
    # 1. Page Header
    # 2. Slotted array
    # a. input a tuple

    # Just storing sequentially for now.
    # Keep track of page header offset and page offset

    TUPLE_SIZE_BYTES = 20
    PAGE_NUMBER = None

    disk_manager = DiskManager()

    def __init__(self, page_number):
        self.PAGE_NUMBER = page_number
        if self._check_if_page_exists():
            return
        self._allocate_page()

    def _allocate_page(self):
        self.disk_manager.allocate_bytes(PAGE_SIZE)

    def _check_if_page_exists(self):
        database_file_size = self.disk_manager.get_database_file_size()
        expected_page_size_if_page_exists = self.PAGE_NUMBER * PAGE_SIZE
        return (
            True if expected_page_size_if_page_exists == database_file_size else False
        )

    def is_root(self):
        """Very simple for now"""
        return True if self.PAGE_NUMBER == 0 else False

    def get_header(self):
        if self.is_root():
            seek = PAGE_SIZE * self.PAGE_NUMBER
            self.disk_manager.read_bytes(n=BTREE_PAGE_HEADER_SIZE, s=seek)
        else:
            self.disk_manager.read_bytes(n=ROOT_PAGE_HEADER_SIZE, s=0)

    def write_database_header(self, header_string, page_size, text_encoding):
        if not self.is_root():
            raise NotRootPageError

        # Validate input sizes
        header_string_length_limit = DATABASE_HEADER_STRUCTURE["HEADER_STRING"]["SIZE"]
        page_size_length_limit = DATABASE_HEADER_STRUCTURE["PAGE_SIZE"]["SIZE"]
        text_encoding_length_limit = DATABASE_HEADER_STRUCTURE["TEXT_ENCODING"]["SIZE"]
        header_string_offset = DATABASE_HEADER_STRUCTURE["HEADER_STRING"]["OFFSET"]
        page_size_offset = DATABASE_HEADER_STRUCTURE["PAGE_SIZE"]["OFFSET"]
        text_encoding_offset = DATABASE_HEADER_STRUCTURE["TEXT_ENCODING"]["OFFSET"]
        if len(bytes(header_string)) > header_string_length_limit:
            raise ValueError(
                f"Header string provided exceeded the allowed length of {header_string_length_limit}"
            )
        if len(bytes(page_size)) > page_size_length_limit:
            raise ValueError(
                f"Header string provided exceeded the allowed length of {page_size_length_limit}"
            )
        if len(bytes(text_encoding)) > text_encoding_length_limit:
            raise ValueError(
                f"Header string provided exceeded the allowed length of {text_encoding_length_limit}"
            )

        self.disk_manager.write_bytes(
            data=bytes(header_string), offset=header_string_offset
        )
        self.disk_manager.write_bytes(data=bytes(page_size), offset=page_size_offset)
        self.disk_manager.write_bytes(
            data=bytes(text_encoding), offset=text_encoding_offset
        )


if __name__ == "__main__":
    page = Page()
