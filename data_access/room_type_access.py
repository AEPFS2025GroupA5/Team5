from data_access.base_data_access import BaseDataAccess
import model

class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, 
                 db_path: str = None
        ):
        super().__init__(db_path)

    ## Read Methods
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
    
    ## Admin Methods
    def create_new_room_type(self,
                             description: str,
                             max_guests: int
        ) -> model.RoomType:
        sql = """
        INSERT INTO room_type (description, max_guests) VALUES (?, ?)
        """
        params = (description, max_guests)
        last_row_id, _ = self.execute(sql, params)

        return model.RoomType(last_row_id, description, max_guests)
    
    def update_room_type(self,
                         room_type: model.RoomType
        ) -> None:
        sql = """
        UPDATE room_type SET description = ?, max_guests = ? WHERE type_id = ?
        """
        params = (
        room_type.description,
        room_type.max_guests,
        room_type.type_id
        )

        self.execute(sql, params)

    def delete_room_type_by_id(self, 
                         room_type: model.RoomType
        ) -> None:
        sql = """
        DELETE FROM room_type WHERE type_id = ?
        """
        params = ([room_type.type_id])

        self.execute(sql, params)
    

         
