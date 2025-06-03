import os
import model
import data_access


class AddressManager:
    def __init__(self):

        self.__address_da = data_access.AddressDataAccess()

    def create_new_address(self,
                            street: str,
                            city: str,
                            zip_code: str
                        ) -> model.Address:
        
        return self.__address_da.create_new_address(street, city, zip_code)
    
    def read_all_addresses(self) -> list[model.Address]:
        return self.__address_da.read_all_addresses()
    
    def read_address_by_id(self,
                            address_id: int
                        ) -> model.Address:
        return self.__address_da.read_address_by_id(address_id)
    
    def get_address_id_by_city(self,
                                city: str
                            ) -> int:
        return self.__address_da.get_address_id_by_city(city)
    
    def update_address(self,
                        street: str,
                        city: str,
                        zip_code: str,
                        address_id: int
                    ) -> None:
        return self.__address_da.update_address(street, city, zip_code, address_id)
    
    def delete_address_by_id(self,
                                address_id: int
                            ) -> None:
        return self.__address_da.delete_address_by_id(address_id)
