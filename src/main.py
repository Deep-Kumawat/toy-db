import os
from buffer_pool.buffer_pool import BufferPool
from storage_engine.storage_engine import StorageEngine
from utils.logger import get_logger
from time import perf_counter

logger = get_logger()

if __name__ == "__main__":
	start_ts = perf_counter()

	# try:
	# 	os.remove("electric.db")
	# 	logger.info('Deleted db file')
	# except:
	# 	pass

	storage_engine = StorageEngine()
	# Create Table
	# storage_engine.create_table("CREATE TABLE TBLNUMBERS (ID INT, NUMBER INT)")
	storage_engine.insert_into_table(table_name="TBLNUMBERS", data=(1, 69420))
	# first_page_contents = storage_engine.read_page(0)
	# logger.info(f"Page contents of first (0) page: {first_page_contents}")
	# second_page_contents = storage_engine.read_page(1)
	# logger.info(f"Page contents of second (1) page: {second_page_contents}")
	logger.info("Completed execution in %s", perf_counter() - start_ts)