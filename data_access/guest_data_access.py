from data_access.base_data_access import BaseDataAccess
import model

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
        return [model.Guest(*row) for row in rows]
    
    def read_guest_by_id(self, guest_id: int) -> model.Guest:
        sql = """
        SELECT g.guest_id, g.first_name, g.last_name, g.email,
              a.address_id, a.street, a.city, a.zip_code
        FROM guest g
        JOIN address a ON g.address_id = a.address_id
        WHERE g.guest_id = ?
        """
        row = self.fetchone(sql, (guest_id,))
        # if not row:
        #     raise ValueError(f"No guest found with ID {guest_id}")

        guest_id, first_name, last_name, email, address_id, street, city, zip_code = row
        address = model.Address(address_id, street, city, zip_code)
        return model.Guest(guest_id, first_name, last_name, email, address)
    
    def read_guest_by_name(self, 
                              last_name:str
        ) -> model.Guest:
        sql = "SELECT guest_id, first_name, last_name, email, address_id FROM guest WHERE last_name LIKE ?"
        params = tuple([f"%{last_name}%"])
        rows = self.fetchall(sql,params)
        return [model.Guest(*row) for row in rows]

    def create_new_guest(self,
                            first_name: str,
                            last_name: str,
                            email: str,
                            address_id: int
        ) -> model.Guest:
      if not isinstance(first_name, str):
        raise TypeError("firstname has to be a str")
      if not first_name:
        raise ValueError("firstname name is mandatory")
      
      if not isinstance(last_name, str):
        raise TypeError("lastname has to be a str")
      if not last_name:
        raise ValueError("lastname name is mandatory")
      
      if not isinstance(email, str):
        raise TypeError("email has to be a str")
      if not email:
        raise ValueError("email name is mandatory")

      if not isinstance(address_id, int):
        raise TypeError("address_id has to be a int")
      if not address_id:
        raise ValueError("address_id name is mandatory")
      
      else:
        sql= "INSERT INTO guest (first_name, last_name, email, address_id) VALUES (?, ?, ?, ?)"
        params = tuple([first_name, last_name, email, address_id])
        last_row_id, _ = self.execute(sql, params)
        return model.Guest(guest_id=last_row_id, first_name=first_name, last_name=last_name, email=email, address_id=address_id)
    
    def update_guest_by_last_name(self,
                      guest_id:int, 
                      new_last_name:str
        ) -> None:
      
      if not isinstance(guest_id, int):
         raise ValueError("Guest ID has to be an integer")
      if guest_id is None:
         raise ValueError("Guest ID is required")
      
      if not isinstance(new_last_name, str):
         raise ValueError("The new last name has to be a string")
      if new_last_name is None:
         raise ValueError("In order to change the last name you need to type in the new last name")

      else:
        sql = "UPDATE guest SET last_name = ? WHERE guest_id = ?"
        params = (new_last_name, guest_id)
        self.execute(sql, params)

    def delete_guest_by_id(self, guest_id: int) -> None:
      if not isinstance(guest_id, int):
        raise ValueError("Guest ID has to be an integer")
      if guest_id is None:
        raise   ValueError("In order to delete a guest you need to type in the Guest ID")

      else:
        sql = "DELETE FROM guest WHERE guest_id = ?"
        self.execute(sql, (guest_id,))