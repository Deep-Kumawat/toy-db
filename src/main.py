from storage_engine.column import Column
from storage_engine.storage_engine import StorageEngine
from utils.logger import get_logger

logger = get_logger(name=__name__)

if __name__ == "__main__":
    #################################################
    ## Start of program. Load properties from header
    #################################################
    logger.info("Running main.py")
    # buffer_pool = BufferPool()
    # Create Table
    storage_engine = StorageEngine()
    logger.info("Creating a new table...")
    storage_engine.create_table(
        table_name="TBLPLAYERS", columns=[Column(type="STRING", name="PLAYER_NAME")]
    )
    # storage_engine.create_table("TBLWIZARDS", None)
    # logger.info("Created a new table")
    # logger.info("Insert a row into a table")
