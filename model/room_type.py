from __future__ import annotations
from typing import TYPE_CHECKING
from model.facility import Facility

class RoomType:
    def __init__(self,
        type_id: int,
        description: str,
        max_guests: int,
        facility_ids: list[Facility] = None
        ):
        
        # Prüfungen
        if not isinstance(type_id, int):
            raise TypeError("type_id must be an int")
        if not type_id:
            raise ValueError("type_id is required")

        if not isinstance(description, str):
            raise TypeError("description must be a string")
        if not description:
            raise ValueError("description must not be empty")

        if not isinstance(max_guests, int):
            raise TypeError("max_guests must be an int")
        if max_guests <= 0:
            raise ValueError("max_guests must be greater than 0")

        facility_ids = facility_ids or []
        if not all(isinstance(fid, int) for fid in facility_ids):
            raise TypeError("All facility_ids must be integers")
     
        self.__type_id = type_id
        self._description = description
        self._max_guests = max_guests

        # Facilities Verbinden
        self.__facilities: list[Facility] = []
        if facility_ids is not None:
            for id in facility_ids:
             facility = Facility.get(id)
             self.__facilities.append(facility)
             
    def __repr__(self):
        facility_names = ", ".join(f.name for f in self.__facilities) if self.__facilities else "None"
        return (
        f"RoomType(\n"
        f"  ID: {self.__type_id}\n"
        f"  Beschreibung: {self._description}\n"
        f"  Max Gäste: {self._max_guests}\n"
        f"  Facilities: {facility_names}\n"
        f")"
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
    
    @property
    def facilities(self) -> list[Facility]:
        return self.__facilities.copy()
    
    #Setter
    @description.setter
    def description(self, description: str):
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        if not description:
            raise ValueError("description can't be empty")
        self._description = description

    @max_guests.setter
    def max_guests(self, max_guests: int):
        if not isinstance(max_guests, int):
            raise TypeError("max_guests must be an int")
        if max_guests <= 0:
            raise ValueError("max_guests must be greater than 0")
        self._max_guests = max_guests

    def facilities(self) -> list[Facility]:
        return self.__facilities.copy()

    def add_facility(self, facility: Facility):
        if not isinstance(facility, Facility):
            raise TypeError("facility must be a Facility instance")
        if facility not in self.__facilities:
            self.__facilities.append(facility)

    def remove_facility(self, facility: Facility):
        if facility in self.__facilities:
            self.__facilities.remove(facility)

    


  