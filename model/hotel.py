from __future__ import annotations
from typing import TYPE_CHECKING

import model

class Hotel:
    def __init__(self,
                hotel_id:int,
                name:str,
                stars:int,
                address:model.Address,
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
        if not isinstance(address, model.Address):
            raise TypeError("address_id must a Adress onject")
        
        self.__hotel_id = hotel_id
        self._name = name
        self._stars = stars
        self.__address: model.Address = address
        self.__rooms: list[model.Room] = []
    

    def __repr__(self):
        return (
            f"Hotel(\n"
            f"  ID: {self.__hotel_id}\n"
            f"  Name: {self._name}\n"
            f"  Stars: {self._stars}\n"
            f"  Address ID: {self.__address}\n"
            f")"
        )
    
    def show_user_friendly(self):
        return (
            f"Name: {self._name}\n"
            f"{self.__address.show_user_friendly()}"
            f"Stars: {self._stars}\n"
            
        )
    #Getter    
    @property
    def hotel_id(self):
        return self.__hotel_id

    @property
    def name(self):
        return self._name

    @property
    def stars(self):
        return self._stars
    @property
    def address(self) -> model.Address:
        return self.__address

    @property
    def rooms(self) -> list[model.Room]:
        return self.__rooms.copy()
    
    ##Setter
    @rooms.setter
    def rooms(self, new_rooms: list[model.Room]):
        if not isinstance(new_rooms, list):
            raise TypeError("Rooms must be a list of Room objects")
        if not all(isinstance(room, model.Room) for room in new_rooms):
            raise TypeError("All items in the list must be Room objects")
        self.__rooms = new_rooms
    
    
#Funktionen
    def add_room(self,
                room: model.Room
        ): 
        if room.__hotel is not self:
            raise ValueError("Room does not belong to this hotel")
        if room not in self.__rooms:
            self.__rooms.append(room)

    def remove_room(self,
                    room: model.Room
        ):
        if room in self.__rooms:
            self.__rooms.remove(room)

