from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.room import Room


class Hotel:
    def __init__(self,
                hotel_id:int,
                name:str,
                stars:int,
                adress_id:int
         ):
        
        #Prüfungen
        if not isinstance(hotel_id, int):
            raise TypeError("hotel_id must be an integer")
        if not hotel_id:
            raise ValueError("hotel_id is required")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name:
            raise ValueError("name is required")
        if not isinstance(stars, int):
            raise TypeError("stars must be an integer")
        if not isinstance(adress_id, int):
            raise TypeError("address_id must be an integer")
        
        self.__hotel_id = hotel_id
        self._name = name
        self._stars = stars
        self.__adress_id = adress_id
        self.__rooms: list["Room"] = []
    

    def __repr__(self):
        return (
            f"Hotel(\n"
            f"  ID: {self.__hotel_id}\n"
            f"  Name: {self._name}\n"
            f"  Stars: {self._stars}\n"
            f"  Address ID: {self.__adress_id}\n"
            f"  Rooms: {len(self.__rooms)}\n"
            f")"
        )
    
    #Getter    
    @property
    def hotelid(self):
        return self.__hotel_id

    @property
    def name(self):
        return self._name

    @property
    def stars(self):
        return self._stars
    @property
    def address_id(self) -> int:
        return self.__address_id

    @property
    def rooms(self) -> list[Room]:
        return self.__rooms.copy()
    
    
#Funktionen
    def add_room(self,
                room:"Room"
        ): 
        if room not in self.__rooms:
            self.__rooms.append(room)

    def remove_room(self,
                    room: "Room"
        ):
        if room in self.__rooms:
            self.__rooms.remove(room)

