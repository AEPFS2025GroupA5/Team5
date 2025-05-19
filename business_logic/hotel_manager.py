import os

import model
import data_access

class HotelManager:
    def __init__(self):
        self.__hotel_da = data_access.HotelDataAccess()

    def create_new_hotel(self,
                            name: str,
                            stars: int,
                            address_id: int      
        )-> model.Hotel:
            return self.__hotel_da.create_new_hotel(name, stars, address_id)
        
    def update_hotel(self,
                        hotel: model.Hotel
        ) -> None:
           return self.__hotel_da.update_hotel(hotel)
                

    def delete_hotel_by_id(self,
                            hotel_id:int
        ) -> None:
          return self.__hotel_da.delete_hotel_by_id(hotel_id)
    
    def read_all_hotels(self) -> list[model.Hotel]:
        return self.__hotel_da.read_all_hotels()   
                
        
    def read_hotel_by_id(self,
                            hotel_id:int
        ) -> model.Hotel:
          return self.__hotel_da.read_hotel_by_id(hotel_id)
                

        
        

