30     Bytes -- Header
    16 Bytes -- DB String
    2  Bytes -- Page Size
    4  Bytes -- Free Page Number 
1000   Bytes -- Table Map
    10 Bytes -- Table Name
    86 Bytes -- Table SQL
    4 Bytes -- Table Btree address

## Btree
Page can either be an internal or a leaf page
Page format for Btree:
    Page header 8 bytes
    Page type   1 byte





