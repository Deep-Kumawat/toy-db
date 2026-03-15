import os
import struct
from query_processor.utils import get_table_name
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
        if not os.path.exists(self.DB_FILE):
            logger.info("Database file not found. Creating a new file.")
            # Write page header
            self.FILE_HEADER_OFFSET = 0
            with open(self.DB_FILE, "wb") as f:
                header = bytearray(100)
                header[0:8] = b"Toy DB"
                self.FILE_HEADER_OFFSET += 8
                struct.pack_into(">H", header, 8, self.PAGE_SIZE)
                self.FILE_HEADER_OFFSET += 2
                # offset
                struct.pack_into(">H", header, self.FILE_HEADER_OFFSET, self.FILE_HEADER_OFFSET)

                f.write(header)
                print(f"Initialized file header")
        else:
            logger.info(f"Found database file at: {self.DB_FILE}")

    def _append_to_db(self, data, offset=None):
        with open(self.DB_FILE, "ab") as f:
            if offset:
                f.seek(offset)
            f.write(data)

    def create_table(self, table_name, schema):
        pass


if __name__ == "__main__":
    logger.info("This is the storage engine!")
    pass
