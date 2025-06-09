from __future__ import annotations
from typing import TYPE_CHECKING

class Facility:
    def __init__(self,
                facility_id:int,
                name:str
        ):
    
        # TypeErrors
        if not isinstance(facility_id, int):
            raise TypeError("facility_id must be an int")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        
        self.__facility_id = facility_id
        self._name = name


    def __repr__(self):
         return f"Facility(ID: {self.__facility_id} | Name: {self._name})"

    ##Getter
    @property
    def facility_id(self) -> int:
        return self.__facility_id
    
    @property
    def name(self) -> str:
        return self._name
    
    ##Setter
    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name




        