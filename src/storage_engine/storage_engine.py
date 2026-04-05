import os
from config.file_config import PAGE_SIZE, SCHEMA_TABLE_ROOT_PAGE_NUMBER
from storage_engine.btree.btree import BTree
from storage_engine.column import Column
from storage_engine.page import Page 
from utils.logger import get_logger


logger = get_logger(name=__name__)

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
            logger.info(
                f"Found database file at: {self.DB_FILE} returning early from storage_engine()"
            )
            return

        logger.info("Database file not found. Creating a new file...")

        # Initialize file
        self.root_page = Page(0)
        self.root_page.write_database_header(
            header_string="Toy DB", page_size=PAGE_SIZE, text_encoding="UTF-8"
        )
        self.root_page.write_page_header(page_type=0)

    def create_table(self, table_name: str, columns: list[Column]) -> None:
        """
        1. Add table record to the schema_table.
        2. Allocate a new page for the table.
        """
        # 1. Get the schema table
        logger.info("Fetching the BTree for schema table...")
        schema_catelog_btree = BTree(page_number=SCHEMA_TABLE_ROOT_PAGE_NUMBER)

        # 2. Create a new record in the schema table
        # schema_catelog_btree.add_record()
        pass


if __name__ == "__main__":
    logger.info("This is the storage engine!")
    pass
