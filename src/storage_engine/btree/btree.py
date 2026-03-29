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

logger = get_logger()


class BTree:
    def __init__(self, page_number: int | None = None, is_root_page: bool = False):
        if page_number is None:
            # Allocate a new page
            self.page = Page()
            # self.root_btree_node = BTreeNode(self.page)
        else:
            # Page number is provided say, 0:
            validate_positive_integer(page_number)

            # Deserialize page
            self.page = Page(page_number=page_number)
            logger.info(
                f"Deserialized page type: {self.page.get_page_type()} into a BTree object"
            )

        # Initialize a BTree header in the provided page

    def add_record(self, cell_payload: tuple[int | str, ...]) -> None:
        """Returns the cell pointer pointing to the 'cell_payload'"""
        logger.info("Cell Layout provided: %s", cell_payload)
        pass
