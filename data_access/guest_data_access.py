from data_access.base_data_access import BaseDataAccess
from model.guest import Guest
from model.address import Address

class GuestDataAccess(BaseDataAccess):
    def __init__(self, 
                 db_path: str = None
        ):
        super().__init__(db_path)

    def read_all_guest(self) -> list[Guest]:
        sql = """
        SELECT guest_id, first_name, last_name, email, address_id FROM guest
        """
        rows = self.fetchall(sql)
        return [Guest(*row) for row in rows]
    
    def read_guest_by_id(self,
                            guest_id:int
        ) -> Guest:
          sql = "SELECT guest_id, first_name, last_name, email, address_id FROM guest WHERE guest_id = ?"
          row = self.fetchone(sql, (guest_id,))
          if row:
            return Guest(*row)
          return None
