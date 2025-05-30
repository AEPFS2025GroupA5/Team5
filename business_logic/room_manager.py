import os

import model
import data_access


class RoomManager:
    def __init__(self):
        self.__room_da = data_access.room_data_access.RoomDataAccess()
        self.__room_facility_dao = data_access.room_facility_data_access.RoomFacilityDataAccess()

    def get_all_rooms(self) -> list[model.Room]:
        return self.__room_da.read_all_rooms()

    def get_room_details_for_hotel(self, hotel_id: int) -> list[model.Room]:
        all_rooms = self.__room_da.read_all_rooms()
        result = []
        for room in all_rooms:
            if room.hotel_id == hotel_id:
                result.append(room)
        return result
    
    def get_facilities_for_room(self, room_id: int) -> list[model.Facility]:
        return self.__room_facility_dao.get_facilities_for_room(room_id)
    
    def get_room_info_user_friendly(self, hotel_id: int) -> list[dict]:
        rooms = self.get_room_details_for_hotel(hotel_id)
        room_info = []

        for room in rooms:
            facilities = self.get_facilities_for_room(room.room_id)
            info = {
                "Room Number": room.room_number,
                "Room Type": room.room_type._description,
                "Max Guests": room.room_type.max_guests,
                "Facilities": [facility.name for facility in facilities],
                "price_per_night": room.price_per_night,
                ### Rechnung mit Nächte * Preis pro nacht
                
            }
            room_info.append(info)
        return room_info
   
    
    

        

       