# models/room_type.py
from dataclasses import dataclass

@dataclass
class RoomType:
    id: int
    name: str
    max_guests: int
    description: str
    price: float


# data_access/roomtype_access.py
import sqlite3
from .base_data_access import BaseDataAccess
from model import RoomType

class RoomTypeAccess(BaseDataAccess):
    """CRUD-Klasse für die Tabelle room_type."""

    def _row_to_entity(self, row: sqlite3.Row) -> RoomType:
        """Konvertiert einen DB-Row in ein RoomType-Objekt."""
        return RoomType(
            id=row["id"],
            name=row["room_type"],
            max_guests=row["max_guests"],
            description=row["description"],
            price=row["price"]
        )