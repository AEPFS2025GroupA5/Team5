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

    def refresh_all_hotels(self) -> None:
        self._all_hotels = self.__hotel_da.read_all_hotels()

    def create_new_hotel(self,
                        name: str,
                        stars: int,
                        address_id: int      
        )-> model.Hotel:
        new_hotel = self.__hotel_da.create_new_hotel(name, stars, address_id)
        self.refresh_all_hotels()
        return new_hotel
    
    def update_hotel(self,
                    hotel_id :int = None,
                    name: str = None,
                    stars: int = None,
                    address_id: int = None
        ) -> None:
           updated = self.__hotel_da.update_hotel_by_data(hotel_id, name, stars, address_id)
           self.refresh_all_hotels()
           return updated
    
    def delete_hotel_by_id(self,
                            hotel_id:int
        ) -> None:
          result = self.__hotel_da.delete_hotel_by_id(hotel_id)
          self.refresh_all_hotels()
          return result
    
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
        matching_hotels = [
        hotel for hotel in self._all_hotels if city.lower() in hotel.address.city.lower()
        ]
        return matching_hotels
    
    def get_hotels_by_city_and_stars(self,
                                    city: str,
                                    stars: int
        ) -> list[model.Hotel]:
        matching_hotels = [
        hotel for hotel in self._all_hotels if city.lower() in hotel.address.city.lower() 
        and hotel.stars >= stars
        ]
        return matching_hotels
    
    def get_hotels_by_city_and_max_guests(self,
                                           city: str, 
                                           max_guests: int
        ) -> list[tuple [model.Hotel, model.Room]]:
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
                if self.__booking_manager.read_all_av_rooms_by_hotel(hotel.hotel_id, check_out_date, check_in_date):
                    av.append(hotel)
            hotels = av
        
        return hotels 
    
## Output Funktionen

    
    def print_user_friendly_hotels(self, hotels: list[model.Hotel]) -> None:
        for hotel in hotels:
            info = (
            f"Name:    {hotel.name}\n"
            f"Adresse: {hotel.address.street}\n"
            f"City:    {hotel.address.city}\n"
            f"Stars:   {hotel.stars}\n"
            + "-" * 40
        )
            print(info)

    def get_user_frendly_hotel_info_short(hotel: model.Hotel):
        return f"Hotel ID: {hotel.hotel_id}, Name: {hotel.name}, Stars: {hotel.stars}, Address: {hotel.address.city}, {hotel.address.street}"
    
    
                  
     
        
    
    

      
            