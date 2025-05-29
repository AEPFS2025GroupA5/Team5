import os

import model
import data_access


class RoomManager:
    def __init__(self):
        self.__room_da = data_access.room_data_access.RoomDataAccess()

    def get_all_rooms(self) -> list[model.Room]:
        return self.__room_da.read_all_rooms()

    def get_room_details_for_hotel(self, hotel_id: int) -> list[model.Room]:
        all_rooms = self.__room_da.read_all_rooms()
        result = []
        for room in all_rooms:
            if room.hotel_id == hotel_id:
                result.append(room)
        return result
    
    

        

       