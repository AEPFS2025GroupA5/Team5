import os

import model
import data_access


class RoomManager:
    def __init__(self):
        self.__room_da = data_access.room_data_access.RoomDataAccess()
        self.__room_type_da = data_access.room_type_access.RoomTypeDataAccess()
        self.__room_facility_da = data_access.room_facility_data_access.RoomFacilityDataAccess()
        self.__hotel_da = data_access.hotel_data_access.HotelDataAccess()
        self.__facility_da = data_access.facility_data_access.FacilityDataAccess()


## Admin Funktionen

    def get_all_rooms(self) -> list[model.Room]:
        return self.__room_da.read_all_rooms()
    
    def create_new_room(self,
                        hotel_id: int,
                        room_number: str,
                        room_type: model.RoomType,
                        price_per_night: float
        ) -> model.Room:
        if not isinstance(hotel_id, int) or hotel_id <= 0:
            raise ValueError("Hotel ID must be a positive integer")
        if not room_number or not isinstance(room_number, str):
            raise ValueError("Room number must be a non-empty string")
        if not isinstance(room_type, model.RoomType):
            raise TypeError("Room type must be a RoomType object")
        if not isinstance(price_per_night, (int, float)) or price_per_night <= 0:
            raise ValueError("Price per night must be a positive number")
        
        return self.__room_da.create_new_room(hotel_id, room_number, room_type, price_per_night)
    
    def update_room(self,
                    room_id: int,
                    hotel_id: int,
                    room_number: str,
                    room_type: model.RoomType,
                    price_per_night: float
        ) -> None:
        if not isinstance(room_id, int) or room_id <= 0:
            raise ValueError("Room ID must be a positive integer")
        if not isinstance(hotel_id, int) or hotel_id <= 0:
            raise ValueError("Hotel ID must be a positive integer")
        if not room_number or not isinstance(room_number, str):
            raise ValueError("Room number must be a non-empty string")
        if not isinstance(room_type, model.RoomType):
            raise TypeError("Room type must be a RoomType object")
        if not isinstance(price_per_night, (int, float)) or price_per_night <= 0:
            raise ValueError("Price per night must be a positive number")
        
        room = model.Room(room_id, hotel_id, room_number, room_type, price_per_night)
        self.__room_da.update_room(room)

    def update_room_by_object(self,
                            room: model.Room
        ) -> None:
        if not isinstance(room, model.Room):
            raise TypeError("Room must be a Room object")
        self.__room_da.update_room(room)

    def delete_room_by_id(self,
                          room_id: int
        ) -> None:
        if not isinstance(room_id, int) or room_id <= 0:
            raise ValueError("Room ID must be a positive integer")
        room = self.__room_da.read_room_by_id(room_id)
        if not room:
            raise ValueError(f"No room found with ID {room_id}")
        self.__room_da.delete_room_by_id(room_id)

    def get_room_by_id(self, 
                       room_id: int
        ) -> model.Room:
        room = self.__room_da.read_room_by_id(room_id)
        return room
    
    def get_room_details_for_hotel(self, hotel_id: int) -> list[model.Room]:
        all_rooms = self.__room_da.read_all_rooms()
        result = []
        for room in all_rooms:
            if room.hotel_id == hotel_id:
                result.append(room)
        return result
    
    def get_facilities_for_room(self, room_id: int) -> list[model.Facility]:
        return self.__room_facility_da.get_facilities_for_room(room_id)
    
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
                "Room ID": room.room_id,
                "Room Number": room.room_number,
                "Room Type": room.room_type._description,
                "Facilities": [facility.name for facility in facilities],
                }
            room_info.append(info)
        return room_info
    
## Room Type Management
    def read_all_room_types(self) -> list[model.RoomType]:
        return self.__room_type_da.read_all_room_types()
    
    def create_new_room_type(self,
                            description: str, 
                            max_guests: int
        ) -> model.RoomType:
        return self.__room_type_da.create_new_room_type(description, max_guests)
    
    def update_room_type(self,
                         id: int,
                         description: str,
                         max_guests: int
        ) -> None:
        room_type = model.RoomType(id, description, max_guests)
        self.__room_type_da.update_room_type(room_type)

    def delete_room_type_by_id(self,
                               id: int
        )-> None:
        room_type = self.__room_type_da.read_room_type_by_id(id)
        self.__room_type_da.delete_room_type_by_id(room_type)

### Facility Management

    def add_facility_to_room(self, room_id: int, facility_id: int) -> None:
        if not isinstance(room_id, int) or not isinstance(facility_id, int):
            raise TypeError("Room ID and Facility ID must be integers")
        self.__room_facility_da.add_facility_to_room(room_id, facility_id)

    def get_all_facilities(self) -> list[model.Facility]:
        return self.__facility_da.read_all_facilities()
    
    def create_new_facility(self,
                            name: str
        ) -> model.Facility:
        if not isinstance(name, str) or not name:
            raise ValueError("Facility name must be a non-empty string")
        return self.__facility_da.create_new_facility(name)
    
    def update_facility(self, 
                        id: int,
                        name: str
        ) -> None:
        new_fachility = model.Facility(id, name)
        self.__facility_da.update_facility(new_fachility)

    def delete_facility_by_id(self,
                              facility_id: int
        ) -> None:
        if not isinstance(facility_id, int):
            raise TypeError("Facility ID must be an integer")
        self.__facility_da.delete_facility_by_id(facility_id)

   
    
    

        

       