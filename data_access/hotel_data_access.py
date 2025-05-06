# data_access/hotel_data_access.py
from __future__ import annotations        # erste Zeile!
import model
from data_access.base_data_access import BaseDataAccess


class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str | None = None):
        super().__init__(db_path)    # übernimmt DB_FILE aus ENV, falls db_path=None

    def read_all_hotels(self) -> list[model.Hotel]:
        sql = """
        SELECT HotelId, Name, Address, City, Stars
        FROM   Hotel
        ORDER BY HotelId
        """
        rows = self.fetchall(sql)    # BaseDataAccess.fetchall → Liste von Tupeln
        return [
            model.Hotel(hotel_id, name, address, city, stars)
            for hotel_id, name, address, city, stars in rows
        ]
