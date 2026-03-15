from storage_engine.column import Column


class Schema:
    def __init__(self):
        self.columns = []

    def add_columns(self, column):
        if isinstance(column, Column):
            self.columns.append(column)
        else:
            raise ValueError("Schema can only contain objects of class Column")
