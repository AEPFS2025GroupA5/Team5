from data_access.base_data_access import BaseDataAccess
import model

class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, 
                 db_path: str = None
        ):
        super().__init__(db_path)

    def read_all_room_types(self) -> list[model.RoomType]:
        sql = """
        SELECT type_id, description, max_guests FROM room_type
        """
        rows = self.fetchall(sql)
        return [model.RoomType(*row) for row in rows]
    
    def read_room_type_by_id(self,
                            type_id:int
        ) -> model.RoomType:
          sql = "SELECT type_id, description, max_guests FROM room_type WHERE type_id = ?"
          row = self.fetchone(sql, (type_id,))
          if row:
            return model.RoomType(*row)
          return None
