import os
import struct
from config.file_config import DATABASE_FILE_PATH
from exceptions.disk_manager import FailedToReadBytes, FailedToAllocateBytes
from utils.logger import get_logger

logger = get_logger()


class DiskManager:
    def allocate_bytes(self, n):
        try:
            with open(DATABASE_FILE_PATH, "ab") as f:
                f.write(b"\x00" * n)
                return
        except Exception as e:
            logger.error(f"Failed to allocate bytes in DB file. Error: {e}")
            raise FailedToAllocateBytes

    def read_bytes(self, n, s):
        """Reads the :n number of bytes from the DB with :s seek"""
        try:
            with open(DATABASE_FILE_PATH, "rb") as f:
                f.seek(s)
                return f.read(n)
        except:
            raise FailedToReadBytes

    def write_bytes(self, data, offset=None):
        with open(DATABASE_FILE_PATH, "r+b") as f:
            if offset:
                f.seek(offset + 1)
            if isinstance(data, int):
                f.write(struct.pack("H", data))
                return
            f.write(data)

    def get_database_file_size(self):
        return os.path.getsize(DATABASE_FILE_PATH)

    def is_db_file_exists(self):
        return os.path.exists(DATABASE_FILE_PATH)
