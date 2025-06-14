import os
import pandas as pd
import model
import data_access

class GuestManager:
    def __init__(self):
        self.__guest_da = data_access.GuestDataAccess()
    
    #Read Functions
    def read_all_guest(self) -> list[model.Guest]:
        return self.__guest_da.read_all_guest()
    
    def read_guest_by_id(self,
                            guest_id:int
        ) -> model.Guest:
        guest= self.__guest_da.read_guest_by_id(guest_id)

        if guest is None:
            raise ValueError("There is no such guest in our systems")

        return self.__guest_da.read_guest_by_id(guest_id)
    
    def read_guest_by_name(self, 
                              last_name:str
        ) -> model.Guest:
        return self.__guest_da.read_guest_by_name(last_name)

    #Admin Functions
    def create_new_guest(self,
                            first_name: str,
                            last_name: str,
                            email: str,
                            address_id: int
        ) -> model.Guest:
        if "@" not in email or "." not in email:
            raise ValueError("Email must be a valid email address.")
    
        all_guests= self.read_all_guest()
        for guest in all_guests:
            if guest.email == email:
                raise ValueError("This email is already in use.")
            
            if (guest.first_name == first_name and
                guest.last_name == last_name and
                guest.address.address_id == address_id):
                raise ValueError("This guest already exists in the system.")

        return self.__guest_da.create_new_guest(first_name, last_name, email, address_id) 

    def update_guest_last_name_by_id(self,
                      guest_id:int, 
                      new_last_name:str
        ) -> None:

        guest= self.read_guest_by_id(guest_id)
        if new_last_name != guest.last_name:
            return self.__guest_da.update_guest_last_name_by_id(guest_id, new_last_name)
        else:
            print("No change: Last name is already up to date.")

    def update_guest_first_name_by_id(self, 
                                      guest_id: int, 
                                      new_first_name: str
        ) -> None:
        guest= self.read_guest_by_id(guest_id)
        
        if guest is None:
            print("There is no such Guest in our systems")
        if new_first_name != guest.first_name:
            return self.__guest_da.update_guest_first_name_by_id(guest_id, new_first_name)
        else:
            print("No change: First name is already up to date.")


    def update_guest_address_by_id(self, 
                                   guest_id: int, 
                                   new_address_id: str
        ) -> None:

        guest= self.read_guest_by_id(guest_id)

        if guest is None:
            print("There is no such Guest in our systems")
        if new_address_id != guest.address.address_id:
            return self.__guest_da.update_guest_address_by_id(guest_id, new_address_id)
        else:
            print("No change: Address is already up to date.") 

    def update_guest_email_by_id(self, 
                                 guest_id: int, 
                                 new_email: str
        ) -> None:
        guest= self.read_guest_by_id(guest_id)

        if "@" not in new_email or "." not in new_email:
            raise ValueError("Email must be a valid email address.")
        if guest is None:
            print("There is no such Guest in our systems")
        if new_email != guest.email:
            return self.__guest_da.update_guest_email_by_id(guest_id, new_email)
        else:
            print("No change: E-Mail is already up to date.")

    def delete_guest_by_id(self, guest_id: int) -> None:
        guest= self.read_guest_by_id(guest_id)
        if guest is None:
            raise ValueError("There is no such guest ID in our system.")

        return self.__guest_da.delete_guest_by_id(guest_id)
    

    def city_of_guests(self) -> pd.DataFrame:
        return self.__guest_da.city_of_guests()
        