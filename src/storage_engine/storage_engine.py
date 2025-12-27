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
        
        # if not instance:
        #     self.instance = StorageEngine()
        # return self.instance

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
        
    def get_page_size(self) -> str:
        with open(self.DB_FILE, "rb") as f:
            header = f.read(100)
            page_size = struct.unpack(">H", header[8:10])[0]
            return page_size
    
    def read_header(self):
        with open(self.DB_FILE, "rb") as f:
            header = f.read(100)
            page_size = struct.unpack(">H", header[8:10])[0]
            print(f"Header string: {header[0:8]}")
            print(f"Page size: {page_size}")

    def create_table(self, query):
        """Create a hashmap in the file for every table. NAME : SQL"""
        table_name = get_table_name(query)
        offset = self.HEADER_SIZE_BYTES + 1
        data = bytearray(10)
        data = table_name.encode("utf-8")
        self._append_to_db(data=data, offset=offset)
        offset += 10 + 1
        data = bytearray(80)
        data = query.encode("utf-8")
        self._append_to_db(data=data, offset=offset)
        # Store table btree address
        

    def insert_into_table(self):
        pass

    def select_from_table(self):
        pass

    def __initialize_schema__(self):
        """Create schema table in root page"""
        # Write a tuple for testing
        with open(self.DB_FILE, "ab") as f:
            tuple = Tuple()
            tuple_byte_array = tuple.create_tuple(b"Deep", b"22")
            f.write(tuple_byte_array)
        # self.read_header()

if __name__ == "__main__":
    page_manager = StorageEngine()
    # logger.info(f"[MAIN] Reading file header...")
    page_manager.read_header()
    page_manager.__initialize_schema__()
    print("[STORAGE ENGINE MAIN] Bye!")
