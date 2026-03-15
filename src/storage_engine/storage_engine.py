import os
import struct
from config.file_config import PAGE_SIZE
from query_processor.utils import get_table_name
from storage_engine.page import Page
from storage_engine.schema import Schema
from storage_engine.tuple import Tuple
from utils.logger import get_logger


logger = get_logger()

"""
-----------
FILE LAYOUT
-----------

Database Header              100B

"""

"""
    --------
    APIs
    --------
    1. create_table()
    2. insert()
    3. select()
"""


class StorageEngine:
    """
    1. Save information in file header.
    2.
    """

    DB_FILE = "toydb.db"
    PAGE_SIZE = 4096
    FILE_HEADER_OFFSET = 0
    HEADER_SIZE_BYTES = 100

    def __init__(self):
        if os.path.exists(self.DB_FILE):
            logger.info(f"Found database file at: {self.DB_FILE}")
            return

        logger.info("Database file not found. Creating a new file.")

        # Initialize file
        root_page = Page(0)
        root_page.write_database_header(
            header_string="Toy DB", page_size=PAGE_SIZE, text_encoding="UTF-8"
        )

    def create_table(self, table_name: str, schema: Schema):
        pass


if __name__ == "__main__":
    logger.info("This is the storage engine!")
    pass
