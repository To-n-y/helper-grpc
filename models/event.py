from piccolo.columns import Boolean, Varchar, Integer
from piccolo.engine.sqlite import SQLiteEngine
from piccolo.table import Table

DB = SQLiteEngine("test_database.db")


class Event(Table, db=DB):
    name = Varchar()
    type = Varchar()
    age_restrictions = Boolean(default=False)
    day = Integer(default=0)
