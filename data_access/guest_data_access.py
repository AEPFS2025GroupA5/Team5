from data_access.base_data_access import BaseDataAccess
import model
from data_access.address_data_access import AddressDataAccess

class GuestDataAccess(BaseDataAccess):
    def __init__(self, 
                 db_path: str = None
        ):
        super().__init__(db_path)

    def read_all_guest(self) -> list[model.Guest]:
        sql = """
        SELECT guest_id, first_name, last_name, email, address_id FROM guest
        """
        rows = self.fetchall(sql)
        guests= []
        if rows:
          for guest_id, first_name, last_name, email, address_Id in rows:
             addr= AddressDataAccess()
             address= addr.read_address_by_id(address_Id)
             guest= model.Guest(guest_id, first_name, last_name, email, address)
             guests.append(guest)
          return guests
        else: 
           return None
    
    def read_guest_by_id(self, guest_id: int) -> model.Guest:
        sql = """
        SELECT g.guest_id, g.first_name, g.last_name, g.email,
              a.address_id, a.street, a.city, a.zip_code
        FROM guest g
        JOIN address a ON g.address_id = a.address_id
        WHERE g.guest_id = ?
        """
        row = self.fetchone(sql, (guest_id,))
        if row:
          guest_id, first_name, last_name, email, address_id, street, city, zip_code = row
          address = model.Address(address_id, street, city, zip_code)
          return model.Guest(guest_id, first_name, last_name, email, address)
        else:
           return None
    
    def read_guest_by_name(self, 
                              last_name:str
        ) -> model.Guest:
        sql = "SELECT guest_id, first_name, last_name, email, address_id FROM guest WHERE last_name LIKE ?"
        params = tuple([f"%{last_name}%"])
        rows = self.fetchall(sql,params)
        if rows:
          return [model.Guest(*row) for row in rows] 
        else:
          return None

    def create_new_guest(self,
                            first_name: str,
                            last_name: str,
                            email: str,
                            address_id: int
        ) -> model.Guest:
      sql= "INSERT INTO guest (first_name, last_name, email, address_id) VALUES (?, ?, ?, ?)"
      params = tuple([first_name, last_name, email, address_id])
      last_row_id, _ = self.execute(sql, params)
      return model.Guest(guest_id=last_row_id, first_name=first_name, last_name=last_name, email=email, address_id=address_id)
  
    def update_guest_by_last_name(self,
                      guest_id:int, 
                      new_last_name:str
        ) -> None:    
      sql = "UPDATE guest SET last_name = ? WHERE guest_id = ?"
      params = (new_last_name, guest_id)
      self.execute(sql, params)

    def delete_guest_by_id(self, guest_id: int) -> None:
      sql = "DELETE FROM guest WHERE guest_id = ?"
      self.execute(sql, (guest_id,))