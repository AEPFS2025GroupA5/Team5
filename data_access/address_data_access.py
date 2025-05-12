# address_data_access.py

from data_access.base_data_access import BaseDataAccess
import model

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_all_addresses(self) -> list[model.Address]:
        sql = """
        SELECT address_id, street, city, zipcode FROM address
        """
        rows = self.fetchall(sql)
        return [model.Address(*row) for row in rows]

    def read_address_by_id(self, address_id: int) -> model.Address:
        if not address_id:
            raise ValueError("address_id is required")

        sql = "SELECT address_id, street, city, zipcode FROM address WHERE address_id = ?"
        row = self.fetchone(sql, (address_id,))
        if row:
            return model.Address(*row)
        return None

    def create_new_address(self, street: str, city: str, zipcode: str) -> model.Address:
        if not all(isinstance(x, str) for x in [street, city, zipcode]):
            raise TypeError("street, city, and zipcode must be strings")
        if not all([street, city, zipcode]):
            raise ValueError("All fields must be filled")

        sql = "INSERT INTO address (street, city, zipcode) VALUES (?, ?, ?)"
        params = (street, city, zipcode)
        last_row_id, _ = self.execute(sql, params)

        return model.Address(addressid=last_row_id, street=street, city=city, zipcode=zipcode)

    def update_address(self, address: model.Address) -> None:
        sql = """
        UPDATE address SET street = ?, city = ?, zipcode = ? WHERE address_id = ?
        """
        params = (address.street, address.city, address.zipcode, address.addressid)
        self.execute(sql, params)

    def delete_address_by_id(self, address_id: int) -> None:
        sql = "DELETE FROM address WHERE address_id = ?"
        self.execute(sql, (address_id,))

    