from __future__ import annotations
from typing import TYPE_CHECKING

class Facility:

    _facility_list: dict[int, Facility] = {}

    def __init__(self,
            facility_id:int,
            name:str
        ):
    
        # Prüfungen
        if not isinstance(facility_id, int):
            raise TypeError("facility_id must be an int")
        if not facility_id:
            raise ValueError("facility_id is required")

        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name:
            raise ValueError("name must not be empty")
        
        self.__facility_id: int = facility_id
        self._name:str = name

        Facility._facility_list[facility_id] = self

    def __repr__(self):
         return f"Facility(ID: {self.__facility_id} | Name: {self._name})"

    ##Getter
    @property
    def facility_id(self) -> int:
        return self.__facility_id
    
    @property
    def name(self) -> str:
        return self._name

    
    def get(facility_id: int) -> Facility:
        try:
            return Facility._facility_list[facility_id]
        except KeyError:
            raise ValueError(f"Facility with id {facility_id} not found")
    
    ##Setter
    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name:
            raise ValueError("name can't be empty")
        self._name = name




        