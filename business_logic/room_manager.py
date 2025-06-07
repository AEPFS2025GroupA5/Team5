import os

import model
import data_access
from datetime import date


class RoomManager:
    def __init__(self):
        self.__room_da = data_access.room_data_access.RoomDataAccess()
        self.__room_type_da = data_access.room_type_access.RoomTypeDataAccess()
        self.__room_facility_da = data_access.room_facility_data_access.RoomFacilityDataAccess()
        self.__hotel_da = data_access.hotel_data_access.HotelDataAccess()
        self.__facility_da = data_access.facility_data_access.FacilityDataAccess()


## Read Methods

    def get_all_rooms(self) -> list[model.Room]:
        rooms= self.__room_da.read_all_rooms()
        return rooms
    
    def get_room_by_id(self, 
                       room_id: int
        ) -> model.Room:
        room = self.__room_da.read_room_by_id(room_id)
        return room
    
    def get_room_details_for_hotel(self, hotel_id: int) -> list[model.Room]:
        all_rooms = self.get_all_rooms()
        result = []
        for room in all_rooms:
            if room.hotel_id == hotel_id:
                result.append(room)
        return result
    
    def get_facilities_for_room(self, room_id: int) -> list[model.Facility]:
        return self.__room_facility_da.get_facilities_for_room(room_id)
    
    def get_room_info_user_friendly(self, hotel_id: int) -> list[dict]:
        rooms = self.get_room_details_for_hotel(hotel_id)
        

        for room in rooms:
            facilities = self.get_facilities_for_room(room.room_id)
            print(f"Room Number:    {room.room_number}")
            print(f"Room Type:      {room.room_type.description}")
            print(f"Max Guests:     {room.room_type.max_guests}")
            print(f"Facilities:     {[facility.name for facility in facilities]}")
            print(f"Price per Night: {room.price_per_night:.2f} CHF")
            print("-" * 40)

                
    ## Admin Methods
    def create_new_room(self,
                        hotel_id: int,
                        room_number: str,
                        type_id: int,
                        price_per_night: float
        ) -> model.Room:
        #Prüfung der Eingaben // Doppelt, weil eigentlich die BL für die Prüfungen zuständig ist
        if price_per_night <= 0:
            raise ValueError("Price per night must be a positive number")
        t1 = self.__hotel_da.read_hotel_by_id(hotel_id)
        if not t1:
            raise ValueError(f"Hotel with ID {hotel_id} does not exist")
        t2 = self.__room_type_da.read_room_type_by_id(type_id)
        if not t2:
            raise ValueError(f"Room type with ID {t2} does not exist")
        
        
        return self.__room_da.create_new_room(hotel_id, room_number, type_id, price_per_night)
    
    def update_room(self,
                    room_id: int,
                    hotel_id: int,
                    room_number: str,
                    type_id: int,
                    price_per_night: float
        ) -> None:
         if price_per_night <= 0:
            raise ValueError("Price per night must be a positive number")
         t1 = self.__hotel_da.read_hotel_by_id(hotel_id)
         if not t1:
            raise ValueError(f"Hotel with ID {t1} does not exist")
         room_type = self.__room_type_da.read_room_type_by_id(type_id)
         if not room_type:
            raise ValueError(f"Room type with ID {room_type} does not exist")
        
         room = model.Room(room_id, hotel_id, room_number, room_type, price_per_night)
         self.__room_da.update_room(room)

    def update_room_by_object(self,
                            room: model.Room
        ) -> None:
        if not isinstance(room, model.Room):
            raise TypeError("Room must be a Room object")
        self.__room_da.update_room(room)

    def delete_room(self,
                          room: model.Room
        ) -> None:
        room = self.__room_da.read_room_by_id(room.room_id)
        if not room:
            raise ValueError(f"No room found")
        
        self.__room_da.delete_room(room)
    
    def change_price_per_night(self,
                               room_id: int,
                               new_price: float
        ) -> None:
        room = self.__room_da.read_room_by_id(room_id)
        if not room:
            raise ValueError(f"No room found with ID {room_id}")
        if new_price <= 0:
            raise ValueError("New price per night must be a positive number")
        
        room.price_per_night = new_price
        self.__room_da.update_room(room)

    def get_rooms_for_admin(self) -> list[model.Room]:
        rooms = self.get_all_rooms()
        

        for room in rooms:
            hotel = self.__hotel_da.read_hotel_by_id(room.hotel_id)
            hotel_name = hotel.name if hotel else "Unknown Hotel"
            facilities = self.get_facilities_for_room(room.room_id)
            
            print(f"Hotel: {hotel_name}")
            print(f"Room ID: {room.room_id}")
            print(f"Room Number: {room.room_number}")
            print(f"Room Type: {room.room_type._description}")
            print(f"Max Guests: {room.room_type.max_guests}")
            print(f"Facilities: {[facility.name for facility in facilities]}")
            print(f"Price per Night: {room.price_per_night}")
            print("-" * 40)


## Room Type Management
    def get_room_type_by_id(self,
                            id: int
        ) -> model.RoomType:
        return self.__room_type_da.read_room_type_by_id(id)

    def read_all_room_types(self) -> list[model.RoomType]:
        return self.__room_type_da.read_all_room_types()
    
    def create_new_room_type(self,
                            description: str, 
                            max_guests: int
        ) -> model.RoomType:
        if max_guests <= 0:
            raise ValueError("Max guests must be a positive integer")
        
        return self.__room_type_da.create_new_room_type(description, max_guests)
    
    def update_room_type(self,
                         id: int,
                         description: str,
                         max_guests: int
        ) -> None:

        if max_guests <= 0:
            raise ValueError("Max guests must be a positive integer")
        
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

    def delete_facility_from_room (self,
                                    room_id: int,
                                    facility_id: int 
        ) -> None:
        facilities = self.__room_facility_da.get_facilities_for_room(room_id)
        if not any(f.facility_id == facility_id for f in facilities):
            raise ValueError(f"Facility ID {facility_id} is not assigned to room {room_id}")
        
        self.__room_facility_da.delete_facility_from_room(room_id, facility_id)

##Pricing Management
    def get_price_season(self, check_in_date: date, price_per_night:float) -> float:
        percent= self.get_percent_season(check_in_date)
        base_price = price_per_night

        return round(base_price * percent, 2)

    def get_percent_season(self, check_in_date: date) -> float:
        month = check_in_date.month

        if 6 <= month <= 9 or month == 12:  
            percent = 2.0
        elif 1 <= month <= 5:  
            percent = 1.5
        else:
            percent = 1.0 

        return percent
   
    
    

        

       