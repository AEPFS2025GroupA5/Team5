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
                        hotel_id :int,
                        name: str,
                        stars: int,
                        address_id: int
        ) -> None:
           if not hotel_id:
            raise ValueError("Hotel ID must be provided")
           if not name:
                raise ValueError("Hotel name must be provided")
           if not isinstance(stars, int) or stars <= 0:
                raise ValueError("Stars must be a positive integer")
           if not address_id:
                raise ValueError("Address ID must be provided")
           
           return self.__hotel_da.update_hotel_by_data(hotel_id, name, stars, address_id)
                

    def delete_hotel_by_id(self,
                            hotel_id:int
        ) -> None:
          return self.__hotel_da.delete_hotel_by_id(hotel_id)
    
    def read_all_hotels(self) -> list[model.Hotel]:
        return self.__hotel_da.read_all_hotels()   
    
    def read_hotel_userfriendly(self,) -> list[model.Hotel]:
         all_hotels = self.__hotel_da.read_all_hotels()
         return [hotel.show_user_friendly() for hotel in all_hotels]

    def read_hotel_by_name(self, name:str) -> model.Hotel:
        if not name:
             raise ValueError("Name must be provided")
        if not isinstance(name, str):
             raise ValueError("Name has to be a string") 
        else:     
            return self.__hotel_da.read_hotel_by_name(name)        
        
    def read_hotel_by_id(self,
                            hotel_id:int
        ) -> model.Hotel:
          return self.__hotel_da.read_hotel_by_id(hotel_id)
    
    def get_hotels_by_city(self, city: str) -> list[model.Hotel]:
        if not city:
            raise ValueError("City must be provided")
        
        all_hotels = self.__hotel_da.read_all_hotels()
        matching_hotels = [
        hotel for hotel in all_hotels if hotel.address.city.lower() == city.lower()
        ]
        if not matching_hotels:
             return f"No hotels found in {city}"
        
        return matching_hotels
    
    def get_hotels_by_city_and_stars(self, city: str, stars: int) -> list[model.Hotel]:
        if not city:
            raise ValueError("City must be provided")
        if not stars or stars <= 0:
            raise ValueError("Stars must be a positive integer")
        
        all_hotels = self.__hotel_da.read_all_hotels()
        matching_hotels = [
        hotel for hotel in all_hotels if hotel.address.city.lower() == city.lower() 
        and hotel.stars >= stars
        ]
        if not matching_hotels:
             return f"No hotels found in {city} with {stars} stars"
        
        return matching_hotels
    
    def get_hotels_by_city_and_max_guests(self, city: str, max_guests: int) -> list[model.Hotel]:
        if not city:
            raise ValueError("City must be provided")
        if not max_guests or max_guests <= 0:
            raise ValueError("Max guests must be a positive integer")
        
        all_hotels = self.__hotel_da.read_all_hotels()
        matching_hotels = [
        hotel for hotel in all_hotels if hotel.address.city.lower() == city.lower() 
        and any(room.max_guests >= max_guests for room in hotel.rooms)
        ]
        if not matching_hotels:
             return f"No hotels found in {city} with a maximum of {max_guests} guests"
        
        return matching_hotels
      
                

        
        

