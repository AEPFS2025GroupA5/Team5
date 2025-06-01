from data_access.base_data_access import BaseDataAccess
import model
import data_access.room_type_access
import model.room 

class RoomDataAccess(BaseDataAccess):
    def __init__(self, 
                 db_path: str = None
        ):
        super().__init__(db_path)

        self.__room_type_dao = data_access.room_type_access.RoomTypeDataAccess()

    def read_all_rooms(self) -> list[model.Room]:
        sql = """
        SELECT r.room_id, h.hotel_id, r.room_number, r.type_id, r.price_per_night 
        FROM room as r
        JOIN hotel as h ON r.hotel_id = h.hotel_id
        """
        rows = self.fetchall(sql)
        rooms = []
        room_type_dao = data_access.room_type_access.RoomTypeDataAccess()
        # Dafür das man auch den ganzen RoomType hat
        for row in rows:
            room_id, hotel_id, room_number, type_id, price = row
            room_type = room_type_dao.read_room_type_by_id(type_id)
            room = model.Room(room_id, hotel_id, room_number, room_type, price)
            rooms.append(room)
        return rooms
    
    def read_room_by_id(self,
                        room_id:int
        ) -> model.Room:
          sql = "SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM room WHERE room_id = ?"
          row = self.fetchone(sql, (room_id,))
          if row:
                room_id, hotel_id, room_number, type_id, price = row
                room_type_dao = data_access.room_type_access.RoomTypeDataAccess()
                room_type = room_type_dao.read_room_type_by_id(type_id)
                return model.Room(room_id, hotel_id, room_number, room_type, price)
    
          return None

    def read_hotel_by_roomId(self, room_id: int) -> model.Hotel:
        sql = """
        SELECT h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code
        FROM room r
        JOIN hotel h ON r.hotel_id = h.hotel_id
        JOIN address a ON h.address_id = a.address_id
        WHERE r.room_id = ?
        """
        row = self.fetchone(sql, (room_id,))
        if not row:
            raise ValueError(f"No hotel found for room ID {room_id}")

        hotel_id, name, stars, address_id, street, city, zip_code = row
        address = model.Address(address_id, street, city, zip_code)
        hotel = model.Hotel(hotel_id, name, stars, address)
        return hotel

    def read_rooms_by_hotel_id(self,
                            hotel_id:int
        ) -> list[model.Room]:
          sql = "SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM room WHERE hotel_id = ?"
          rows = self.fetchall(sql, (hotel_id,))
          rooms = []

          for row in rows:
             room_id, hotel_id, room_number, type_id, price = row
             room_type = self.__room_type_dao.read_room_type_by_id(type_id)
             room = model.Room(room_id, hotel_id, room_number, room_type, price)
             rooms.append(room)
          return rooms
    
    def update_room(self,
                room: model.Room
        ) -> None:
        if room is None:
            raise ValueError("Room has to be defined")
        
        sql = """
        UPDATE room SET hotel_id = ?, room_number = ?, type_id = ?, price_per_night = ? WHERE room_id = ?
        """
        params = (
        room.hotel_id,
        room.room_number,
        room.room_type.type_id,
        room.price_per_night,
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