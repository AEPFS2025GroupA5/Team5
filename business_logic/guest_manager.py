import os

import model
import data_access

class GuestManager:
    def __init__(self):
        self.__guest_da = data_access.GuestDataAccess()
    
    def read_all_guest(self) -> list[model.Guest]:
        return self.__guest_da.read_all_guest()
    
    def read_guest_by_id(self,
                            guest_id:int
        ) -> model.Guest:
        return self.__guest_da.read_guest_by_id(guest_id)
    
    def read_guest_by_name(self, 
                              last_name:str
        ) -> model.Guest:
        return self.__guest_da.read_guest_by_name(last_name)

    def create_new_guest(self,
                            first_name: str,
                            last_name: str,
                            email: str,
                            address_id: int
        ) -> model.Guest:
        return self.__guest_da.create_new_guest(first_name, last_name, email, address_id) #bei Address ID lieber den ganzen Objekt returnen

    def update_guest_by_last_name(self,
                      guest_id:int, 
                      new_last_name:str
        ) -> None:
        return self.__guest_da.update_guest_by_last_name(guest_id, new_last_name)

    def delete_guest_by_id(self, guest_id: int) -> None:
        return self.__guest_da.delete_guest_by_id(guest_id)