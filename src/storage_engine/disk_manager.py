from config.file_config import DATABASE_FILE_PATH
from exceptions.file_io_helper import FailedToReadBytes


class DiskManager:
    def read_bytes(self, n, s):
        """Reads the :n number of bytes from the DB with :s seek"""
        try:
            with open(DATABASE_FILE_PATH, "r") as f:
                f.seek(s)
                return f.read(n)
        except:
            raise FailedToReadBytes

    # def _write_to_db(self, data, offset=None):
    #     with open(self.DB_FILE, "wb") as f:
    #         if offset:
    #             f.seek(offset)
    #         f.write(data)
