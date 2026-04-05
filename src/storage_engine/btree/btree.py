"""
This module implements the btree class which has methods for
inserting, fetching and deleting a tuple/cell from a btree
This class should be able to take a page as a constructor arg
and deserialze it.
IF the page is db root page, manage the layout accordingly
IF the page is None, create a new page.
"""

from storage_engine.page import Page
from validation.validations import validate_positive_integer
from utils.logger import get_logger

logger = get_logger(name=__name__)


class BTree:
    def __init__(self, page_number: int | None = None, is_root_page: bool = False):
        if page_number is None:
            logger.info("Provided page number was None")
            # Allocate a new page
            self.page = Page()
            # self.root_btree_node = BTreeNode(self.page)
        else:
            logger.info("Provided page number was %d", page_number)
            # Page number is provided say, 0:
            # 1. Validate page_number
            validate_positive_integer(page_number)

            # 2. Deserialize page
            logger.info("Fetching the page for BTree")
            self.page = Page(page_number=page_number)

    def add_record(self, cell_payload: tuple[int | str, ...]) -> None:
        """Returns the cell pointer pointing to the 'cell_payload'"""
        logger.info("Cell Layout provided: %s", cell_payload)
        pass
