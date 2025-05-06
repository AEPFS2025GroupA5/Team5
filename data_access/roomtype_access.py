import sqlite3
from .base_data_access import BaseDataAccess

class RoomTypeAccess(BaseDataAccess):
     def _row_to_entity(row: sqlite3.Row):
          pass