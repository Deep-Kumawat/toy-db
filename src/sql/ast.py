from sql.constants.datatypes import DataType


class Column:
    def __init__(self, name: str, type: DataType):
        self.name = name
        self.type = type


class CreateQuery:
    def __init__(self, table_name: str, columns: list[Column]):
        self.table_name = table_name
        self.columns = columns
