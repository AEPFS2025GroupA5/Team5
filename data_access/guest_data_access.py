from data_access.base_data_access import BaseDataAccess
import model
import pandas as pd
from data_access.address_data_access import AddressDataAccess

class GuestDataAccess(BaseDataAccess):
  def __init__(self, 
              db_path: str = None
    ):
    super().__init__(db_path)
    self.__address_dao= AddressDataAccess()

#Read Functions
  def read_all_guest(self) -> list[model.Guest]:
    sql = """
    SELECT guest_id, first_name, last_name, email, address_id FROM guest
    """
    rows = self.fetchall(sql)
    guests= []
    if rows:
      for guest_id, first_name, last_name, email, address_Id in rows:
          address= self.__address_dao.read_address_by_id(address_Id)
          guest= model.Guest(guest_id, first_name, last_name, email, address)
          guests.append(guest)
      return guests
    else: 
        return None
  
  def read_guest_by_id(self, 
                          guest_id: int
      ) -> model.Guest:
    if not guest_id:
      raise ValueError("Guest ID is required")
    if not isinstance(guest_id, int):
      raise ValueError("Guest ID has to be an integer")

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
    if not last_name:
      raise ValueError("Last Name is required")
    if not isinstance(last_name, str):
      raise ValueError("Last name has to be a string")

    sql = "SELECT guest_id, first_name, last_name, email, address_id FROM guest WHERE last_name LIKE ?"
    params = tuple([f"%{last_name}%"])
    rows = self.fetchall(sql,params)
    guests= []
    if rows:
      for (guest_id, first_name, last_name, email, address_id) in rows:
        addre= self.__address_dao.read_address_by_id(address_id)
        address= model.Address(addre.address_id, addre.street, addre.city, addre.zip_code)
        guest= model.Guest(guest_id, first_name, last_name, email, address)
        guests.append(guest)
      return guests 
    else:
      return None

#Admin Functions
  def create_new_guest(self,
                          first_name: str,
                          last_name: str,
                          email: str,
                          address_id: int
      ) -> model.Guest:
    
    if not first_name:
      raise ValueError("First name is required")
    if not isinstance(first_name, str):
      raise ValueError("First name has to be a string")
    if not last_name:
      raise ValueError("Last name is required")
    if not isinstance(last_name, str):
      raise ValueError("Last name has to be a string")
    if not email:
      raise ValueError("Email is required")
    if not isinstance(email, str):
      raise ValueError("Email has to be a string")
    if not address_id:
      raise ValueError("Address ID is required")
    if not isinstance(address_id, int):
      raise ValueError("Address ID has to be an integer")

    sql= "INSERT INTO guest (first_name, last_name, email, address_id) VALUES (?, ?, ?, ?)"
    params = tuple([first_name, last_name, email, address_id])
    last_row_id, _ = self.execute(sql, params)
    addre= self.__address_dao.read_address_by_id(address_id)
    address= model.Address(addre.address_id, addre.street, addre.city, addre.zip_code)
    return model.Guest(last_row_id, first_name, last_name, email, address)

  def update_guest_last_name_by_id(self,
                                  guest_id:int, 
                                  new_last_name:str
      ) -> None:  
    if not guest_id:
      raise ValueError("Guest ID is required")
    if not isinstance(guest_id, int):
      raise ValueError("Guet ID has to be an integer")
    if not new_last_name:
      raise ValueError("Last name is required")
    if not isinstance(new_last_name, str):
      raise ValueError("Last name has to be a string")  

    sql = "UPDATE guest SET last_name = ? WHERE guest_id = ?"
    params = (new_last_name, guest_id)
    self.execute(sql, params)

  def update_guest_first_name_by_id(self, 
                                    guest_id: int, 
                                    new_first_name: str
        ) -> None:
      if not guest_id:
          raise ValueError("Guest ID is required")
      if not isinstance(guest_id, int):
          raise ValueError("Guest ID has to be an integer")
      if not new_first_name:
          raise ValueError("First name is required")
      if not isinstance(new_first_name, str):
          raise ValueError("First name has to be a string")
      
      sql = "UPDATE guest SET first_name = ? WHERE guest_id = ?"
      params = (new_first_name, guest_id)
      self.execute(sql, params)


  def update_guest_address_by_id(self, 
                                 guest_id: int, 
                                 address_id: str
        ) -> None:
      if not guest_id:
          raise ValueError("Guest ID is required")
      if not isinstance(guest_id, int):
          raise ValueError("Guest ID has to be an integer")
      if not address_id:
          raise ValueError("Address is required")
      if not isinstance(address_id, int):
          raise ValueError("Address has to be an integer")
      
      sql = "UPDATE guest SET address_id = ? WHERE guest_id = ?"
      params = (address_id, guest_id)
      self.execute(sql, params)


  def update_guest_email_by_id(self, 
                                guest_id: int, 
                                new_email: str
        ) -> None:
      if not guest_id:
          raise ValueError("Guest ID is required")
      if not isinstance(guest_id, int):
          raise ValueError("Guest ID has to be an integer")
      if not new_email:
          raise ValueError("Email is required")
      if not isinstance(new_email, str):
          raise ValueError("Email has to be a string")
      
      sql = "UPDATE guest SET email = ? WHERE guest_id = ?"
      params = (new_email, guest_id)
      self.execute(sql, params)


  def delete_guest_by_id(self, 
                         guest_id: int
      ) -> None:
    sql = "DELETE FROM guest WHERE guest_id = ?"
    self.execute(sql, (guest_id,))

#Data Visualization
  def city_of_guests(self) -> pd.DataFrame:
    sql= """
    SELECT 
    Count(city) as anzahlPersonen,
    city
    from Guest
    Join Address on Address.address_id=Guest.address_id
    GROUP BY city
    """

    params = tuple()
    return pd.read_sql(sql, self._connect(), params=params)
        