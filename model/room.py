from __future__ import annotations
from datetime import date
from model.room_type import RoomType
from model.hotel import Hotel

class Room:
    def __init__(       
        self,
        room_id: int,
        hotel_id: Hotel,
        room_number: str,
        room_type: RoomType,      
        price_per_night: float
    ):
        # Prüfungen
        if not isinstance(room_id, int):
            raise ValueError("room_id must be an integer")
        
        if not isinstance(room_number, str) or not room_number:
            raise ValueError("room_number must be a non-empty string")
        
        if not hotel_id:
            raise ValueError("hotel is required")
      
        if not room_id:
            raise ValueError("room_id is required")
        if not isinstance(room_id, int):
            raise TypeError("room_id is to be an integer")
   
        if not isinstance(price_per_night, (int, float)):
            raise TypeError("price_per_night must be a number")
        if price_per_night <= 0:
            raise ValueError("price_per_night must be greater than 0")
        
        self.__room_id = room_id
        self.__room_type:RoomType = room_type
        self.__price_per_night = price_per_night
        self._room_number = room_number
        self.__hotel_id = hotel_id
       
    def __repr__(self):
        return (
            f"Room(\n"
            f"  ID: {self.__room_id}\n"
            f"  Hotel ID: {self.__hotel_id}\n"
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
    def hotel_id(self) -> Hotel:
        return self.__hotel_id
    
    @property
    def room_type(self) -> RoomType:
        return self.__room_type

 #Setter    
    @room_number.setter
    def room_number(self, 
                    room_number: str
        ) -> None:
        if not isinstance(room_number, str) or not room_number:
            raise ValueError("room_number must be a non-empty string")
        self._room_number = room_number

    @hotel_id.setter
    def hotel_id(self,
                hotel: Hotel
        )-> None:
        if not hotel:
            raise ValueError("hotel is required")
        self.__hotel = hotel

    # @room_type.setter
    # def type_id(self,
    #             room_type: RoomType
    #     ) -> None:
    #     if not room_type:
    #         raise ValueError("room_type is required")
    #     self.__room_type = room_type

    # @price_per_night.stetter
    # def base_price(
    #     self,
    #     new_price: float
    #     ) -> None:
    #     if not isinstance(new_price, float):
    #         raise TypeError("price per night must be a float")
    #     if new_price < 0:
    #         raise ValueError("price per night must be >= 0")
    #     else:
    #         self.__price_per_night = new_price

    #Funktionen // Maybe schlauer in die Booking Klasse

    # def is_available(
    #     self,
    #     check_in:date,
    #     check_out:date
    #     ) -> bool:
    #     #mit der Booking klasse checken ob er Raum verfügbar ist
    #     for (start, end) in self.__bookings:
    #         if not (check_out <= start or check_in >= end):
    #             return False
    #     return True
            

    # def book(
    #         self,
    #         check_in:date,
    #         check_out:date,
    #         guest_count:int      
    # ) -> None: 
    #     if not isinstance(check_in, date) or not isinstance(check_out, date):
    #         raise TypeError("check_in and check_out must be date-objekts")
    #     if check_out <= check_in:
    #         raise ValueError("check_out must be after check_in")
    #     if not isinstance(guest_count, int) or guest_count < 1:
    #         raise ValueError("guest_count must be positiv")
        
    #     #Max-Gäste prüfugen
    #     if guest_count > self._roomtype.max_guests:
    #         raise ValueError("Too many Guests for this Roomtype")
    #     #Verfügbarkeit prüfen
    #     if not self.is_available(check_in,check_out):
    #         raise ValueError("Room is not available in this Timeframe")
        
    #     self._bookings.append((check_in, check_out))
    #     print("Room was booked!")
   
   
 
