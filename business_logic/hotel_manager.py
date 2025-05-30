import os
from datetime import date
import model
import data_access
import business_logic

class HotelManager:
    def __init__(self):
        self.__hotel_da = data_access.HotelDataAccess()
        self.__room_da = data_access.RoomDataAccess()
        self.__booking_da = data_access.BookingDataAccess()
        self.__room_manager = business_logic.RoomManager()
        self.__booking_manager = business_logic.BookingManager()

        self._all_hotels = self.__hotel_da.read_all_hotels()


## Admin Funktionen

    def refresh_all_hotels(self):
        self._all_hotels = self.__hotel_da.read_all_hotels()

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
    
    def read_hotel_by_id(self,
                        hotel_id:int
        ) -> model.Hotel:
          return self.__hotel_da.read_hotel_by_id(hotel_id)
    
    def read_hotel_by_name(self,
                            name:str
        ) -> model.Hotel:
        if not name:
             raise ValueError("Name must be provided")
        if not isinstance(name, str):
             raise ValueError("Name has to be a string") 
        else:     
            return self.__hotel_da.read_hotel_by_name(name) 
        
    def read_all_hotels(self) -> list[model.Hotel]:
        return self.__hotel_da.read_all_hotels() 


## Filterfunktionen

    def get_hotels_by_city(self,
                            city: str
        ) -> list[model.Hotel]:
        if not city:
            raise ValueError("City must be provided")
        
        matching_hotels = [
        hotel for hotel in self._all_hotels if city.lower() in hotel.address.city.lower()
        ]
        return matching_hotels
    
    def get_hotels_by_city_and_stars(self,
                                    city: str,
                                    stars: int
        ) -> list[model.Hotel]:
        if not city:
            raise ValueError("City must be provided")
        if not stars or stars <= 0:
            raise ValueError("Stars must be a positive integer")
        
        matching_hotels = [
        hotel for hotel in self._all_hotels if city.lower() in hotel.address.city.lower() 
        and hotel.stars >= stars
        ]
        return matching_hotels
    
    def get_hotels_by_city_and_max_guests(self,
                                           city: str, 
                                           max_guests: int
        ) -> list[tuple [model.Hotel, model.Room]]:
        if not city:
            raise ValueError("City must be provided")
        if not max_guests or max_guests <= 0:
            raise ValueError("Max guests must be a positive integer")
    
        result = []
        for hotel in self._all_hotels:
            if city.lower() in hotel.address.city.lower():
                rooms = self.__room_manager.get_room_details_for_hotel(hotel.hotel_id)
                av_rooms= [room for room in rooms if room.max_guests >= max_guests]
                if av_rooms:
                    hotel.__rooms = av_rooms
                    result.append(hotel)
                
        return result
    
    def get_users_individual_wishes(self,
                                   city: str = None,
                                   min_stars: int = None,
                                   max_guests: int = None,
                                   check_in_date: date =None,
                                   check_out_date: date = None
        ) -> list[model.Hotel]:
        hotels = self._all_hotels

        # Stadt filtern
        if city:
            hotels = [hotel for hotel in hotels if city.lower() in hotel.address.city.lower()]

        #Sterne filtern
        if min_stars:
            hotels = [hotel for hotel in hotels if hotel.stars >= min_stars]

        # Max Gäste filtern
        if max_guests:
            hotels_with_rooms = []
            for hotel in hotels:
                rooms = self.__room_manager.get_room_details_for_hotel(hotel.hotel_id)
                av_rooms = [room for room in rooms if room.max_guests >= max_guests]
                if av_rooms:
                    hotel.__rooms = av_rooms
                    hotels_with_rooms.append(hotel)
            hotels = hotels_with_rooms

        # Check-in und Check-out Daten filtern
        if check_in_date and check_out_date:
            av = []
            for hotel in hotels:
                if self.__booking_manager.read_all_av_rooms(hotel.hotel_id, check_in_date, check_out_date):
                    av.append(hotel)
            hotels = av
        
        return hotels 
    
## Output Funktionen

    def print_user_friendly_hotels(self, hotels: list[model.Hotel]) -> None:
        for hotel in hotels:
            print(hotel.show_user_friendly())

    def read_hotel_userfriendly(self,) -> list[model.Hotel]:
         all_hotels = self.__hotel_da.read_all_hotels()
         return [hotel.show_user_friendly() for hotel in all_hotels]
    
                  
     
        
    
    

      
            