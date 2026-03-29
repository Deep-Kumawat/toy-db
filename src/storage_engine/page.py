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
    TEXT_ENCODING_MAP,
    PageConstants,
    PageHeader,
)
from exceptions.page import NotRootPageError
from storage_engine.disk_manager import DiskManager


class Page:
    disk_manager = DiskManager()
    page_number = None

    def __init__(self, page_number: int | None = None):
        self.page_number = page_number
        if self.page_number is None:
            # Allocate a new page
            self.page_number = self.disk_manager.get_new_page_number()
            self.disk_manager.allocate_bytes(PAGE_SIZE)
            return self.page_number
        if self.disk_manager.is_db_file_exists() and self._page_exists():
            return
        self._allocate_page()

    def get_page_type(self) -> bytes:
        """Returns the page type"""
        # Read bytes from [0:2]
        return self.disk_manager.read_bytes(2, 100)

    def _allocate_page(self) -> int:
        page_number = self.disk_manager.get_new_page_number()
        self.disk_manager.allocate_bytes(PAGE_SIZE)
        return page_number

    def _page_exists(self):
        if self.page_number is None:
            raise ValueError(
                "Page number cannot be None when trying to check if page exists"
            )
        database_file_size = self.disk_manager.get_database_file_size()
        expected_page_size_if_page_exists = self.page_number * PAGE_SIZE
        return (
            True if expected_page_size_if_page_exists <= database_file_size else False
        )

    def is_db_root_page(self):
        """Very simple for now"""
        return True if self.page_number == 0 else False

    def get_header(self):
        if self.is_db_root_page():
            if self.page_number is None:
                raise ValueError("Page number cannot be None when trying to get header")
            seek = PAGE_SIZE * self.page_number
            self.disk_manager.read_bytes(n=BTREE_PAGE_HEADER_SIZE, s=seek)
        else:
            self.disk_manager.read_bytes(n=ROOT_PAGE_HEADER_SIZE, s=0)

    def write_database_header(
        self, header_string: str, page_size: int, text_encoding: str
    ):
        if not self.is_db_root_page():
            raise NotRootPageError

        # Validate input sizes against limits defined in DATABASE_HEADER_STRUCTURE
        header_string_length_limit = DATABASE_HEADER_STRUCTURE["HEADER_STRING"]["SIZE"]
        page_size_length_limit = DATABASE_HEADER_STRUCTURE["PAGE_SIZE"]["SIZE"]
        text_encoding_length_limit = DATABASE_HEADER_STRUCTURE["TEXT_ENCODING"]["SIZE"]
        header_string_offset = DATABASE_HEADER_STRUCTURE["HEADER_STRING"]["OFFSET"]
        page_size_offset = DATABASE_HEADER_STRUCTURE["PAGE_SIZE"]["OFFSET"]
        text_encoding_offset = DATABASE_HEADER_STRUCTURE["TEXT_ENCODING"]["OFFSET"]

        text_encoding_val = TEXT_ENCODING_MAP["UTF-8"]
        if (
            len(bytes(header_string, encoding=text_encoding))
            > header_string_length_limit
        ):
            raise ValueError(
                f"Header string provided exceeded the allowed length of {header_string_length_limit}"
            )
        if page_size > 2 ** (page_size_length_limit * 8):
            raise ValueError(
                f"Page size provided exceeded the allowed length of {page_size_length_limit}"
            )
        if text_encoding_val > text_encoding_length_limit * 8:
            raise ValueError(
                f"Text encoding provided exceeded the allowed length of {text_encoding_length_limit}"
            )

        self.disk_manager.write_bytes(
            data=bytes(header_string, encoding=text_encoding),
            offset=header_string_offset,
        )
        self.disk_manager.write_bytes(data=page_size, offset=page_size_offset)
        self.disk_manager.write_bytes(
            data=text_encoding_val, offset=text_encoding_offset
        )

    def write_page_header(self, page_type: int):
        """Writes the page header for a page"""
        if self.is_db_root_page():
            self.disk_manager.write_bytes(
                data=page_type, offset=PageHeader.ROOT_PAGE_OFFSET
            )
            return
        self.disk_manager.write_bytes(
            data=page_type, offset=PageHeader.BTREE_PAGE_OFFSET
        )

    def add_record(self):
        self.disk_manager.write_bytes(data=b"test", offset=PageConstants.RECORD_OFFSET)
        pass


if __name__ == "__main__":
    page = Page()
