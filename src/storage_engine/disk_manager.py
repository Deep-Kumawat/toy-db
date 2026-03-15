import os
from config.file_config import DATABASE_FILE_PATH
from exceptions.disk_manager import FailedToReadBytes, FailedToAllocateBytes


class DiskManager:
    def allocate_bytes(self, n):
        try:
            with open(DATABASE_FILE_PATH, "ab") as f:
                return f.append(n)
        except:
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
        with open(self.DB_FILE, "wb") as f:
            if offset:
                f.seek(offset)
            f.write(data)

    def get_database_file_size(self):
        return os.path.getsize(DATABASE_FILE_PATH)
