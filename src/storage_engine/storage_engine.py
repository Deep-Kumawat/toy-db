import os
import struct
from query_processor.utils import get_table_name
from storage_engine.tuple import Tuple
from utils.logger import get_logger


logger = get_logger()

class StorageEngine:
    """
    1. Save information in file header.
    2. 
    """
    DB_FILE = "electric.db"
    FILE_HEADER_OFFSET = 0
    HEADER_SIZE_BYTES = 30
    PAGE_SIZE_BYTES = 4096
    TABLE_MAP_SIZE_BYTES = 1000
    
    # File Header Variables
    free_page_number = 1
    table_map = {}

    def __init__(self):
        if not os.path.exists(self.DB_FILE):
            logger.info("Database file not found. Creating a new file.")
            # Write page header
            self.FILE_HEADER_OFFSET = 0
            with open(self.DB_FILE, "wb") as f:
                header = bytearray(self.HEADER_SIZE_BYTES)
                header[0:16] = b"Electric DB"
                self.FILE_HEADER_OFFSET += 16
                # Page size
                struct.pack_into(">H", header, self.FILE_HEADER_OFFSET, self.PAGE_SIZE_BYTES)
                self.FILE_HEADER_OFFSET += 2
                # Offset
                struct.pack_into(">H", header, self.FILE_HEADER_OFFSET, self.FILE_HEADER_OFFSET)
                # Free page number
                self.FILE_HEADER_OFFSET += 4
                struct.pack_into(">H", header, self.FILE_HEADER_OFFSET, self.free_page_number)

                f.write(header)
        else:
            # TODO: Set the free page number from db file header
            logger.info(f"Found database file at: {self.DB_FILE}")
    
    def set_free_page_number(self, page_number):
        with open(self.DB_FILE, "wb+") as f:
            f.seek(18)
            buffer = bytearray(4)
            struct.pack_into(">H", buffer, )
        
    def _write_to_db(self, data, offset=None):
        with open(self.DB_FILE, "wb") as f:
            if offset:
                f.seek(offset)
            f.write(data)

    def _append_to_db(self, data, offset=None):
        with open(self.DB_FILE, "ab") as f:
            if offset:
                f.seek(offset)
            f.write(data)

    def get_header_string(self) -> str:
        with open(self.DB_FILE, "rb") as f:
            header = f.read(self.HEADER_SIZE_BYTES)
            return str(header[0:8])
        
    def read_page(self, page_number: int):
        """Reads a page from database file"""
        with open(self.DB_FILE, "rb+") as f:
            offset = page_number * self.PAGE_SIZE_BYTES # Page number is expected to be of 0 based indexing
            f.seek(offset)
            return f.read(self.PAGE_SIZE_BYTES)

    def create_table(self, query):
        """Create a hashmap in the file for every table. NAME : SQL"""
        table_name = get_table_name(query)
        offset = self.HEADER_SIZE_BYTES + 1
        data = bytearray(10)
        data = table_name.encode("utf-8")
        self._append_to_db(data=data, offset=offset)
        offset += 10 + 1
        data = bytearray(86)
        data = query.encode("utf-8")
        self._append_to_db(data=data, offset=offset)
        # Store table btree root page number
        offset += 10 + 1
        address = bytearray(4)
        struct.pack_into(">H", address, 0, self.free_page_number)
        self._append_to_db(data=address, offset=offset)

        # Update memory
        # NOTE: This is not ideal. I think this should again be inititialized by reading the DB header
        self.free_page_number += 1

    def insert_into_table(self, table_name, data):
        # Get the root node of the table btree somehow from the table name
        
        pass

    def select_from_table(self):
        pass

if __name__ == "__main__":
    page_manager = StorageEngine()
    # logger.info(f"[MAIN] Reading file header...")
    page_manager.read_header()
    page_manager.__initialize_schema__()
    print("[STORAGE ENGINE MAIN] Bye!")
