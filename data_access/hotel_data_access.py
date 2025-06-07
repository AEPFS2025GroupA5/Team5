from data_access.base_data_access import BaseDataAccess
from data_access.address_data_access import AddressDataAccess
import model

class HotelDataAccess(BaseDataAccess):
        def __init__(self, 
                 db_path: str = None               
        ):
                super().__init__(db_path)
                self._address_data_access = AddressDataAccess(db_path)

        
        def read_all_hotels(self) -> list[model.Hotel]:
                sql = """
                SELECT h.hotel_id, h.name, h.stars, a.address_id, a.street, a.city, a.zip_code FROM hotel as h
                JOIN address as a ON h.address_id = a.address_id
                """
                rows = self.fetchall(sql)
                return [
                        model.Hotel(
                                hotel_id, 
                                name, 
                                stars, 
                                model.Address(address_id, street, city, zip_code)
                        ) 
                        for hotel_id, name, stars, address_id, street, city, zip_code in rows
                ]
        
        def read_hotel_by_id(self,
                            hotel_id:int
                ) -> model.Hotel:
                sql = "SELECT hotel_id, name, stars, address_id FROM hotel WHERE hotel_id = ?"
                row = self.fetchone(sql, (hotel_id,))
                if row:
                        hotel_id, name, stars, address_id = row
                        # Adresse laden
                        address = self._address_data_access.read_address_by_id(address_id)
                        return model.Hotel(hotel_id, name, stars, address)
                return None
        
        
       
        def read_hotel_by_name(self, name:str) -> model.Hotel:
                sql = """
                SELECT h.hotel_id, h.name, h.stars, a.address_id, a.street, a.city, a.zip_code
                FROM hotel h
                JOIN address a ON h.address_id = a.address_id
                WHERE h.name LIKE ?
                """
                like= f"%{name}%"
                rows = self.fetchall(sql, (like,))
                hotels= []
                
                for (hotel_id, name, stars, address_id, street, city, zip_code) in rows:
                        address = model.Address(address_id, street, city, zip_code)
                        hotel = model.Hotel(hotel_id, name, stars, address)

                        hotels.append(hotel)               
                                
                return hotels

        def create_new_hotel(self,
                            name: str,
                            stars: int,
                            address_id: int
                ) -> model.Hotel:
                address = self._address_data_access.read_address_by_id(address_id)
                if not address:
                        raise ValueError(f"Address with ID {address_id} not found")
                if not name:
                        raise ValueError("Hotel name must be provided")
                if not isinstance(stars, int) or stars <= 0:
                        raise ValueError("Stars must be a positive integer")
                if not address_id:
                        raise ValueError("Address ID must be provided")
                if not isinstance(name, str):
                        raise ValueError("Hotel name must be a string")

                sql = """
                INSERT INTO hotel (name, stars, address_id) VALUES (?, ?, ?)
                """     
                params = (name, stars, address_id)
                last_row_id, _ = self.execute(sql, params)

                new_hotel = model.Hotel(last_row_id, name, stars, address)
                print(f"New hotel created: {new_hotel}")
                print (f"All hotels in database:")
                for hotel in self.read_all_hotels():
                        print(hotel)
                return new_hotel
        
        def update_hotel_by_object(self,
                        hotel: model.Hotel
                ) -> None:
                if hotel is None:
                        raise ValueError("Hotel has to be defined")
                
                sql = """
                UPDATE hotel SET name = ?, stars = ?, address_id = ? WHERE hotel_id = ?
                """     
                params = (
                hotel.name,
                hotel.stars,
                hotel.address.address_id,
                hotel.hotel_id
                )
                self.execute(sql, params)

        def update_hotel_by_data(self,
                hotel_id: int,
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

                address = self._address_data_access.read_address_by_id(address_id)
                if not address:
                        raise ValueError(f"Address with ID {address_id} not found")

                hotel = model.Hotel(hotel_id, name, stars, address)

                self.update_hotel_by_object(hotel)

                print(f"Hotel {hotel_id} updated successfully.")
                print(f"All hotels in database after update:")
                for hotel in self.read_all_hotels():
                        print(hotel)

        def delete_hotel_by_id(self,
                            hotel_id:int
                ) -> None:
                if not hotel_id:
                        raise ValueError("Hotel ID is required")
               
                sql = "DELETE FROM hotel WHERE hotel_id = ?"
                self.execute(sql, (hotel_id,))

                print(f"Hotel {hotel_id} deleted successfully.")
                print(f"All hotels in database after deletion:")
                for hotel in self.read_all_hotels():
                        print(hotel)

        
        

