from data_access.base_data_access import BaseDataAccess
import model

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_all_addresses(self) -> list[model.Address]:
        sql = """
        SELECT address_id, street, city, zip_code FROM address
        """
        rows = self.fetchall(sql)
        if rows:
            return [model.Address(*row) for row in rows]
        else:
            return None

    def read_address_by_id(self, address_id: int) -> model.Address:
        sql = "SELECT address_id, street, city, zip_code FROM address WHERE address_id = ?"
        result = self.fetchone(sql, (address_id,))
        if result:
           address_id, street, city, zip_code = result
           return model.Address(address_id, street, city, zip_code)
        return None
    
    def get_address_id_by_city(self, city: str) -> int: 
        sql = "SELECT address_id, street, city, zip_code FROM address WHERE city LIKE ?"
        like = f"%{city}%"
        rows = self.fetchall(sql, (like,))
        addresses= []
        if rows:
            for (address_id, street, city, zip_code) in rows:
                address= model.Address(address_id, street, city, zip_code)
                addresses.append(address)
            return addresses
        return None

    def create_new_address(self, street: str, city: str, zip_code: str) -> model.Address:
        sql = "INSERT INTO address (street, city, zip_code) VALUES (?, ?, ?)"
        params = (street, city, zip_code)
        last_row_id, _ = self.execute(sql, params)

        return model.Address(address_id=last_row_id, street=street, city=city, zip_code=zip_code)
        

    def update_address(self, street:str, city:str, zip_code:int, address_id) -> None:
        sql = """
        UPDATE address SET street = ?, city = ?, zip_code = ? WHERE address_id = ?
        """
        params = (street, city, zip_code, address_id)
        self.execute(sql, params)

    def delete_address_by_id(self, address_id: int) -> None:
        sql = "DELETE FROM address WHERE address_id = ?"
        self.execute(sql, (address_id,))

    