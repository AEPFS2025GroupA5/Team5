from __future__ import annotations
from typing import TYPE_CHECKING
from model.facility import Facility

class RoomType:
    def __init__(self,
                type_id: int,
                description: str,
                max_guests: int,
        ):
        
        # TypeErrors
        if not isinstance(type_id, int):
            raise TypeError("type_id must be an int")

        if not isinstance(description, str):
            raise TypeError("description must be a string")

        if not isinstance(max_guests, int):
            raise TypeError("max_guests must be an int")
     
        self.__type_id = type_id
        self._description = description
        self._max_guests = max_guests

             
    def __repr__(self):
        return (
        f"  ID:{self.__type_id}\n"
        f"  Description:{self._description}\n"
        f"  Max Guests:{self._max_guests}\n"
        )

    
    ##Getter
    @property
    def type_id(self) -> int:
        return self.__type_id

    @property
    def description(self) -> str:
        return self._description
    
    @property
    def max_guests(self) -> int:
        return self._max_guests
    
    
    #Setter
    @description.setter
    def description(self, description: str):
        if not isinstance(description, str):
            raise TypeError("description must be a string")

    @max_guests.setter
    def max_guests(self, max_guests: int):
        if not isinstance(max_guests, int):
            raise TypeError("max_guests must be an int")

  