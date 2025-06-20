from data_access.base_data_access import BaseDataAccess
from data_access.address_data_access import AddressDataAccess
import model
import pandas as pd

class HotelDataAccess(BaseDataAccess):
        def __init__(self, 
                 db_path: str = None               
        ):
                super().__init__(db_path)
                self._address_data_access = AddressDataAccess(db_path)

        ## Read Funktionen
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
        
        
       
        def read_hotel_by_name(self, 
                               name:str
                ) -> model.Hotel:
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

        ## Admin Funktionen
        def create_new_hotel(self,
                            name: str,
                            stars: int,
                            address_id: int
                ) -> model.Hotel:
                sql = """
                INSERT INTO hotel (name, stars, address_id) VALUES (?, ?, ?)
                """     
                params = (name, stars, address_id)
                last_row_id, _ = self.execute(sql, params)
                address = self._address_data_access.read_address_by_id(address_id)
                new_hotel = model.Hotel(last_row_id, name, stars, address)
                print(f"New hotel created with ID: {new_hotel.hotel_id}")
                
        
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
                address = self._address_data_access.read_address_by_id(address_id)
                if not address:
                        raise ValueError(f"Address with ID {address_id} not found")
                hotel = model.Hotel(hotel_id, name, stars, address)
                self.update_hotel_by_object(hotel)
                print(f"Hotel with ID {hotel.hotel_id} updated successfully.")

        def delete_hotel_by_id(self,
                               hotel_id:int
                ) -> None:
               
                sql = "DELETE FROM hotel WHERE hotel_id = ?"
                self.execute(sql, (hotel_id,))
                print(f"Hotel with ID: {hotel_id} deleted successfully.")

        ## Optionale User Story

        def price_analytics(self) -> pd.DataFrame:
                sql = """
                SELECT h.name, a.city, r.price_per_night
                FROM room r
                JOIN hotel h ON r.hotel_id = h.hotel_id
                JOIN address a ON h.address_id = a.address_id
                """
                return pd.read_sql(sql, self._connect())
        
        

