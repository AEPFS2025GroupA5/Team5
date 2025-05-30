import os

import model
import data_access


class RoomManager:
    def __init__(self):
        self.__room_da = data_access.room_data_access.RoomDataAccess()
        self.__room_facility_dao = data_access.room_facility_data_access.RoomFacilityDataAccess()
        self.__hotel_da = data_access.hotel_data_access.HotelDataAccess()

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
    
    def get_rooms_for_admin(self) -> list[dict]:
        rooms = self.get_all_rooms()
        room_info = []

        for room in rooms:
            hotel = self.__hotel_da.read_hotel_by_id(room.hotel_id)
            hotel_name = hotel.name if hotel else "Unknown Hotel"
            facilities = self.get_facilities_for_room(room.room_id)
            info = {
                "Hotel": hotel_name,
                "Room Number": room.room_number,
                "Room Type": room.room_type._description,
                "Facilities": [facility.name for facility in facilities],
                }
            room_info.append(info)
        return room_info
   
    
    

        

       