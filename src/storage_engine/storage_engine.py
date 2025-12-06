import os
import struct
from tuple import Tuple
# from src.utils.logger import get_logger


# logger = get_logger()

class StorageEngine:
    """
    1. Save information in file header.
    2. 
    """
    DB_FILE = "toydb.db"
    PAGE_SIZE = 4096
    FILE_HEADER_OFFSET = 0

    def __init__(self):
        if not os.path.exists(self.DB_FILE):
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
            print(f"Found database file at: {self.DB_FILE}")
    
    def read_header(self):
        with open(self.DB_FILE, "rb") as f:
            header = f.read(100)
            page_size = struct.unpack(">H", header[8:10])[0]
            print(f"Header string: {header[0:8]}")
            print(f"Page size: {page_size}")

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
    print("[MAIN] Bye!")
