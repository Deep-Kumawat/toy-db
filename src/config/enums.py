from enum import IntEnum


class PageType(IntEnum):
    ROOT_PAGE = 0x00
    TABLE_BTREE_PAGE = 0x01
    TABLE_INDEX_PAGE = 0x02
