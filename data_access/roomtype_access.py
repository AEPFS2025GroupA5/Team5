from data_access.base_data_access import BaseDataAccess 

class RoomTypeAccess(BaseDataAccess):
    def get_all(self):
        sql = "SELECT type_id, description, max_guests FROM Room_Type"
        return self.fetchall(sql)

    def get_by_id(self, roomtype_id: int):
        sql = "SELECT type_id, description, max_guests FROM Room_Type WHERE type_id = ?"
        return self.fetchone(sql, (roomtype_id,))

    def insert(self, description: str, max_guests: int):
        sql = """
        INSERT INTO Room_Type (description, max_guests)
        VALUES (?, ?)
        """
        return self.execute(sql, (description, max_guests))

    def delete(self, roomtype_id: int):
        sql = "DELETE FROM Room_Type WHERE type_id = ?"
        return self.execute(sql, (roomtype_id,))

    def update(self, roomtype_id: int, description: str, max_guests: int):
        sql = """
        UPDATE Room_Type
        SET description = ?, max_guests = ?
        WHERE type_id = ?
        """
        return self.execute(sql, (description, max_guests, roomtype_id))