from data_access.base_data_access import BaseDataAccess
import model

class GuestDataAccess(BaseDataAccess):
    def __init__(self, 
                 db_path: str = None
        ):
        super().__init__(db_path)

    def read_all_guest(self) -> list[model.Guest]:
        sql = """
        SELECT guest_id, first_name, last_name, e-mail, address_id FROM guest
        """
        rows = self.fetchall(sql)
        return [model.Guest(*row) for row in rows]
    
    def read_guest_by_id(self,
                            guest_id:int
        ) -> model.Guest:
          sql = "SELECT guest_id, first_name, last_name, e-mail, address_id WHERE guest_id = ?"
          row = self.fetchone(sql, (guest_id,))
          if row:
            return model.Guest(*row)
          return None
