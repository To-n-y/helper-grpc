from piccolo.columns import Boolean, Varchar, Integer, Time
from piccolo.engine.sqlite import SQLiteEngine
from piccolo.table import Table

DB = SQLiteEngine("db.sqlite")


class Event(Table, db=DB):
    name = Varchar()
    type = Varchar()
    age_restrictions = Boolean(default=False)
    day = Integer(default=0)
    time = Time()
