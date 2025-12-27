# src > main.py

from buffer_pool.buffer_pool import BufferPool
from storage_engine.storage_engine import StorageEngine
from utils.logger import get_logger

logger = get_logger()

if __name__ == "__main__":
	#################################################
	## Start of program. Load properties from header
	#################################################
	logger.info("Running main.py")
	buffer_pool = BufferPool()
	# Create Table
	storage_engine = StorageEngine()
	logger.info("Creating a new table...")
	storage_engine.create_table("CREATE TABLE TBLNUMBERS (ID INT, NUMBER INT)")
	logger.info("Created a new table")
	logger.info("Insert a row into a table")
	