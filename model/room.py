from __future__ import annotations
from model.room_type import RoomType
from model.hotel import Hotel

class Room:
    def __init__(       
                self,
                room_id: int,
                hotel: Hotel,
                room_number: str,
                room_type: RoomType,      
                price_per_night: float
    ):
        # TypeErrors
        if not isinstance(room_id, int):
            raise TypeError("room_id is to be an integer")
        if not isinstance(hotel, Hotel):
            raise TypeError("hotel must be a Hotel object")
        if not isinstance(room_number, str):
            raise TypeError("room_number must be a string")
        if not isinstance(room_type, RoomType):
            raise TypeError("room_type must be a RoomType object")
        if not isinstance(price_per_night, (int, float)):
            raise TypeError("price_per_night must be a number")
        
        self.__room_id = room_id
        self.__room_type:RoomType = room_type
        self.__price_per_night = price_per_night
        self._room_number = room_number
        self.__hotel:Hotel = hotel
       
    def __repr__(self):
        return (
            f"Room(\n"
            f"  ID: {self.__room_id}\n"
            f"  Hotel ID: {self.__hotel.hotel_id}\n"
            f"  Room Number: {self._room_number}\n"
            f"  Type ID: {self.__room_type}\n"
            f"  Price per night: {self.__price_per_night:.2f}\n"
            f")"
        )
    #Getters
    @property
    def room_id(self):
        return self.__room_id

    @property
    def room_number(self):
        return self._room_number

    @property
    def price_per_night(self):
        return self.__price_per_night
    
    @property
    def hotel(self) -> Hotel:
        return self.__hotel
    
    @property
    def room_type(self) -> RoomType:
        return self.__room_type
    
    @property
    def max_guests(self) -> int:
        return self.__room_type.max_guests

 #Setter    
    @room_number.setter
    def room_number(self, 
                    room_number: str
        ) -> None:
        if not isinstance(room_number, str) or not room_number:
            raise ValueError("room_number must be a non-empty string")
        self._room_number = room_number

    @room_type.setter
    def room_type(self,
                 room_type: RoomType
        ) -> None:
        if not room_type:
             raise ValueError("room_type is required")
        self.__room_type = room_type

    @price_per_night.setter
    def price_per_night(self, 
                        price_per_night: float
        ) -> None:
        if not isinstance(price_per_night, (int, float)):
            raise TypeError("price_per_night must be a number")