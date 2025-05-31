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
        return [model.Address(*row) for row in rows]

    def read_address_by_id(self, address_id: int) -> model.Address:
        if not address_id:
            raise ValueError("address_id is required")

        sql = "SELECT address_id, street, city, zip_code FROM address WHERE address_id = ?"
        result = self.fetchone(sql, (address_id,))
        if result:
           address_id, street, city, zip_code = result
           return model.Address(address_id, street, city, zip_code)
        return None
    
    def get_address_id_by_city(self, city: str) -> int:
        if not city:
            raise ValueError("city is required")

        sql = "SELECT address_id FROM address WHERE city = ?"
        row = self.fetchall(sql, (city,))
        if row:
            return row[0]
        return None

    def create_new_address(self, street: str, city: str, zip_code: str) -> model.Address:
        if not all(isinstance(x, str) for x in [street, city, zip_code]):
            raise TypeError("street, city, and zipcode must be strings")
        if not all([street, city, zip_code]):
            raise ValueError("All fields must be filled")

        sql = "INSERT INTO address (street, city, zipcode) VALUES (?, ?, ?)"
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

    