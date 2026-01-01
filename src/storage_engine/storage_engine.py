import os
import struct
from query_processor.utils import get_table_name_from_sql
from storage_engine.btree import BTree
from storage_engine.tuple import Tuple
from utils.logger import get_logger
from config import PAGE_SIZE_BYTES, HEADER_SIZE_BYTES, TABLE_MAP_SIZE_BYTES, FILE_HEADER_OFFSET

logger = get_logger()

class StorageEngine:
    """
    1. Save information in file header.
    2. 
    """
    DB_FILE = "electric.db"

    # File Header Variables
    free_page_number = 1
    table_map = {}

    HEADER_CONFIG = {
        "db_string": {
            "size_in_bytes": 16,
            "offset": 0
        },
        "page_size": {
            "size_in_bytes": 2,
            "offset": 16
        },
        "free_page_number": {
            "size_in_bytes": 4,
            "offset": 18
        },
    }
    btree = BTree()

    def __init__(self):
        self.FILE_HEADER_OFFSET = FILE_HEADER_OFFSET
        self.HEADER_SIZE_BYTES = HEADER_SIZE_BYTES
        self.PAGE_SIZE_BYTES = PAGE_SIZE_BYTES
        self.TABLE_MAP_SIZE_BYTES = TABLE_MAP_SIZE_BYTES

        if os.path.exists(self.DB_FILE):
            # TODO: Set the free page number from db file header
            logger.info(f"✅ Found database file at: {self.DB_FILE}")
            db_root_buffer = self.read_page(0)
            header = db_root_buffer[0:self.HEADER_SIZE_BYTES]
            logger.info("Header: %s", header)
            self.PAGE_SIZE_BYTES = int.from_bytes(header[16:18], byteorder="big")
            logger.info("Page size: %s", self.PAGE_SIZE_BYTES)
            self.free_page_number = int.from_bytes(header[18:22], byteorder="big")
            logger.info("Free page number: %s", self.free_page_number)

            ##################################
            ## Table Map
            ##################################

            tabel_map_buffer = db_root_buffer[self.HEADER_SIZE_BYTES : self.TABLE_MAP_SIZE_BYTES + self.HEADER_SIZE_BYTES]
            # logger.info(f"Table map buffer: {tabel_map_buffer}")
            for i in range(0, self.TABLE_MAP_SIZE_BYTES, 100):
                table_name = tabel_map_buffer[i : i+10].decode("utf-8")
                table_sql = tabel_map_buffer[i+10 : i+96] # Memory leak
                table_page = int.from_bytes(tabel_map_buffer[i+96 : i+100])
                if table_name:
                    self.table_map[table_name] = table_page
            logger.info("ℹ️  Table Map: %s", self.table_map)
        else:
            logger.info("⚠️ Database file not found. Creating a new file.")
            # Write page header
            self.FILE_HEADER_OFFSET = 0
            with open(self.DB_FILE, "wb") as f:
                header = bytearray(self.HEADER_SIZE_BYTES)
                # Database Header String
                header[0:16] = b"Electric DB".ljust(16)
                self.FILE_HEADER_OFFSET += 16
                # Page size
                struct.pack_into(">H", header, self.FILE_HEADER_OFFSET, self.PAGE_SIZE_BYTES)
                self.FILE_HEADER_OFFSET += 2
                # Free page number
                struct.pack_into(">I", header, self.FILE_HEADER_OFFSET, self.free_page_number)
                self.FILE_HEADER_OFFSET += 4
                # Offset
                # self.FILE_HEADER_OFFSET += 2
                # struct.pack_into(">H", header, self.FILE_HEADER_OFFSET+2, self.FILE_HEADER_OFFSET)
                f.write(header)

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

    def _get_header_string(self) -> str:
        with open(self.DB_FILE, "rb") as f:
            header = f.read(self.HEADER_SIZE_BYTES)
            return str(header[0:16])
        
    def set_free_page_number(self, page_number):
        self.free_page_number = page_number
        with open(self.DB_FILE, "r+b") as f:
            f.seek(self.HEADER_CONFIG["free_page_number"]["offset"])
            f.write(struct.pack(">I", page_number))        
        
    def read_page(self, page_number: int):
        """Reads a page from database file"""
        with open(self.DB_FILE, "rb+") as f:
            offset = page_number * self.PAGE_SIZE_BYTES # Page number is expected to be of 0 based indexing
            f.seek(offset)
            return f.read(self.PAGE_SIZE_BYTES)

    def create_table(self, query):
        """Create a hashmap in the file for every table. NAME : SQL"""
        table_name = get_table_name_from_sql(query)
        offset = self.HEADER_SIZE_BYTES
        data = bytearray(10)
        data = table_name.encode("utf-8")
        self._append_to_db(data=data, offset=offset)
        offset += 10
        data = bytearray(86)
        data = query.encode("utf-8").ljust(86)
        assert len(data) == 86
        self._append_to_db(data=data, offset=offset)
        # Store table btree root page number
        offset += 86
        address = bytearray(4)
        struct.pack_into(">I", address, 0, self.free_page_number)
        self._append_to_db(data=address, offset=offset)

        # Update memory
        # NOTE: This is not ideal. I think this should again be inititialized by reading the DB header
        self.set_free_page_number(self.free_page_number + 1)

        # Table Map
        self.table_map[table_name] = self.free_page_number

    def insert_into_table(self, table_name, data):
        # Get the root node of the table btree somehow from the table name
        
        pass

    def select_from_table(self):
        pass

if __name__ == "__main__":
    page_manager = StorageEngine()
    # logger.info(f"[MAIN] Reading file header...")
    page_manager.read_header()
    print("[STORAGE ENGINE MAIN] Bye!")
