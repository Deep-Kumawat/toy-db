|<--------------------------- PAGE SIZE -------------------------->|

+------------------------------------------------------------------+
|                        Database Header (0 - 99)                  |
+------------------------------------------------------------------+
| Magic String (16B)        | "mydb format"                        |
| Page Size (2B)            | e.g., 4096                           |
| Format Version (1B)       |                                      |
| Reserved (1B)             |                                      |
| Total Page Count (4B)     |                                      |
| Free Page Head (4B)       |                                      |
| Schema Version (4B)       |                                      |
| Transaction ID (4B)       |                                      |
| Reserved / Padding (64B)                                         |
+----------------------+-------------------------------------------+
| Schema Page Header   | (starts at offset 100)                    |
| Page Type (2B)       | e.g., 1 (TABLE_BTREE_PAGE)                | -- Each page header must contain this
| (~100 - ~120)        |                                           |
+----------------------+-------------------------------------------+
| Cell Pointer Array (grows ↓)                                     |
+------------------------------------------------------------------+
|                                                                  |
|                        Free Space                                |
|                                                                  |
+------------------------------------------------------------------+
| Cells (grow ↑ from bottom of page)                               |
+------------------------------------------------------------------+
