import os
import struct
from config.file_config import DATABASE_FILE_PATH, PAGE_SIZE
from exceptions.disk_manager import FailedToReadBytes, FailedToAllocateBytes
from utils.logger import get_logger
from validation.validations import validate_positive_integer

logger = get_logger()


class DiskManager:
    def allocate_bytes(self, n: int):
        validate_positive_integer(n)
        try:
            with open(DATABASE_FILE_PATH, "ab") as f:
                f.write(b"\x00" * n)
                return
        except Exception as e:
            logger.error(f"Failed to allocate bytes in DB file. Error: {e}")
            raise FailedToAllocateBytes

    def read_bytes(self, n: int, s: int):
        """Reads the :n number of bytes from the DB with :s seek"""
        validate_positive_integer(n)
        validate_positive_integer(s)
        try:
            with open(DATABASE_FILE_PATH, "rb") as f:
                f.seek(s)
                return f.read(n)
        except:
            raise FailedToReadBytes

    def write_bytes(self, data: bytes | int, offset: int | None = None):
        with open(DATABASE_FILE_PATH, "r+b") as f:
            if offset:
                f.seek(offset + 1)
            if isinstance(data, int):
                f.write(struct.pack("H", data))
                return
            f.write(data)

    def get_database_file_size(self):
        if os.path.exists(DATABASE_FILE_PATH):
            return os.path.getsize(DATABASE_FILE_PATH)
        return 0

    def is_db_file_exists(self):
        return os.path.exists(DATABASE_FILE_PATH)

    def get_new_page_number(self) -> int:
        """
        Returns page number of the new page to create.
        Ex: Current page total page count = 5 then
        returns 6.
        """
        if self.get_database_file_size() % PAGE_SIZE != 0:
            raise FailedToAllocateBytes(
                f"Failed to allocate bytes for new page as the current database file size is not a multiple of PAGE_SIZE. Current database file size: {self.get_database_file_size()}"
            )
        return self.get_database_file_size() // PAGE_SIZE
