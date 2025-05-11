from data_access.base_data_access import BaseDataAccess
import model

class RoomDataAccess(BaseDataAccess):
    def __init__(self, 
                 db_path: str = None
        ):
        super().__init__(db_path)

    def read_all_rooms(self) -> list[model.Room]:
        sql = """
        SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM room
        """
        rows = self.fetchall(sql)
        return [model.Room(*row) for row in rows]
    
    def read_room_by_id(self,
                        room_id:int
        ) -> model.Room:
          sql = "SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM room WHERE room_id = ?"
          row = self.fetchone(sql, (room_id,))
          if row:
            return model.Room(*row)
          return None
    
    def read_rooms_by_hotel_id(self,
                            hotel_id:int
        ) -> list[model.Room]:
          sql = "SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM room WHERE hotel_id = ?"
          rows = self.fetchall(sql, (hotel_id,))
          return [model.Room(*row) for row in rows]
    
    def update_room(self,
                room: model.Room
        ) -> None:
        if room is None:
            raise ValueError("Room has to be defined")
        
        sql = """
        UPDATE room SET hotel_id = ?, room_number = ?, type_id = ?, price_per_night = ? WHERE room_id = ?
        """
        params = (
        room._hotel_id,
        room.room_number,
        room._type_id,
        room._price_per_night,
        room.room_id
        )

        self.execute(sql, params)

    def create_new_room(self,
                        hotel_id: int,
                        room_number: str,
                        type_id: model.RoomType,
                        price_per_night: float
        ) -> model.Room:
        if not hotel_id:
            raise ValueError("Hotel ID has to be defined")
        if not room_number:
            raise ValueError("Room number has to be defined")
        if not isinstance(price_per_night, (int, float)):
            raise TypeError("base_price must be an float")
        if price_per_night < 0:
            raise ValueError("base_price has to be positiv")
        
        sql = """
        INSERT INTO room (hotel_id, room_number, type_id, price_per_night) VALUES (?, ?, ?, ?)
        """
        params = (hotel_id, room_number, type_id, price_per_night)
        last_row_id, _ = self.execute(sql, params)

        return model.Room(last_row_id, hotel_id, room_number, type_id, price_per_night)
    

    def delete_room_by_id(self,
                        room: model.Room
        ) -> None:
        if room is None:
            raise ValueError("Room has to be defined")
        if not room.room_id:
            raise ValueError("Room was not found")
        sql = """
        DELETE FROM room WHERE room_id = ?
        """
        self.execute(sql, (room.room_id,))

    def delete_rooms_by_hotel_id(self,
                            hotel_id:int
        ) -> None:
        if hotel_id is None:
            raise ValueError("Hotel ID has to be defined")
        sql = """
        DELETE FROM room WHERE hotel_id = ?
        """
        self.execute(sql, (hotel_id,))