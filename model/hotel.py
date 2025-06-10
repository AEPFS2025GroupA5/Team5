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
        
        #TypeError Prüfungen
        if not isinstance(hotel_id, int):
            raise TypeError("hotel_id must be an integer")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(stars, int):
            raise TypeError("stars must be an integer")
        if not isinstance(address, model.Address):
            raise TypeError("address_id must a Adress onject")
        
        self.__hotel_id = hotel_id
        self._name = name
        self._stars = stars
        self.__address: model.Address = address

        # Liste von Räumen
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

    #Kopie von den Räumen bekommen
    @property
    def rooms(self) -> list[model.Room]:
        return self.__rooms.copy()
    

