from data_access.base_data_access import BaseDataAccess
import model

class HotelDataAccess(BaseDataAccess):
        def __init__(self, 
                 db_path: str = None
        ):
                super().__init__(db_path)

        
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
                                model.Address(address_id, street, city, zipcode)
                        ) 
                        for hotel_id, name, stars, address_id, street, city, zipcode in rows
                ]
        
        def read_hotel_by_id(self,
                            hotel_id:int
                ) -> model.Hotel:
                sql = "SELECT hotel_id, name, stars, address_id FROM hotel WHERE hotel_id = ?"
                row = self.fetchone(sql, (hotel_id,))
                if row:
                        return model.Hotel(*row)
                return None
       
        def create_new_hotel(self,
                            name: str,
                            stars: int,
                            address_id: int
                ) -> model.Hotel:
                if not name:
                        raise ValueError("Name has to be defined")
                if not isinstance(stars, int) or stars <= 0:
                        raise ValueError("Stars have to be positiv")
                if not address_id:
                        raise ValueError("Address ID has to be defined")
                sql = """
                INSERT INTO hotel (name, stars, address_id) VALUES (?, ?, ?)
                """     
                params = (name, stars, address_id)
                last_row_id, _ = self.execute(sql, params)
                return model.Hotel(last_row_id, name, stars, address_id)
        
        def update_hotel(self,
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
                hotel.address_id,
                hotel.hotel_id
                )
                self.execute(sql, params)

        def delete_hotel_by_id(self,
                            hotel_id:int
                ) -> None:
                sql = "DELETE FROM hotel WHERE hotel_id = ?"
                self.execute(sql, (hotel_id,))

        
        

