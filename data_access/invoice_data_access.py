from data_access.base_data_access import BaseDataAccess
from datetime import datetime
from model.invoice import Invoice
from model.guest import Guest

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, 
                 db_path: str = None
        ):
        super().__init__(db_path)

    def read_all_invoice(self) -> list[Invoice]:
        sql = """
        SELECT invoice_id, booking_id, issue_date, total_amount FROM invoice
        """
        rows= self.fetchall(sql)
        all_invoices=[]

        for row in rows:
            invoice_id, booking_id, issue_date_str, total_amount = row
            issue_date = datetime.strptime(issue_date_str, "%Y-%m-%d").date()
            invoice = Invoice(invoice_id, booking_id, issue_date, float(total_amount))
            all_invoices.append(invoice)

        return all_invoices
    # def read_guest_by_id(self,
    #                         guest_id:int
    #     ) -> Guest:
    #       sql = "SELECT guest_id, first_name, last_name, email, address_id FROM guest WHERE guest_id = ?"
    #       row = self.fetchone(sql, (guest_id,))
    #       if row:
    #         return Guest(*row)
    #       return None
    
    # def read_guest_by_name(self, 
    #                           last_name:str
    #     ) -> Guest:
    #     sql = "SELECT guest_id, first_name, last_name, email, address_id FROM guest WHERE last_name LIKE ?"
    #     params = tuple([f"%{last_name}%"])
    #     rows = self.fetchall(sql,params)
    #     return [Guest(*row) for row in rows]

    # def create_new_guest(self,
    #                         first_name: str,
    #                         last_name: str,
    #                         email: str,
    #                         address_id: int
    #     ) -> Guest:
    #   if not isinstance(first_name, str):
    #     raise TypeError("firstname has to be a str")
    #   if not first_name:
    #     raise ValueError("firstname name is mandatory")
      
    #   if not isinstance(last_name, str):
    #     raise TypeError("lastname has to be a str")
    #   if not last_name:
    #     raise ValueError("lastname name is mandatory")
      
    #   if not isinstance(email, str):
    #     raise TypeError("email has to be a str")
    #   if not email:
    #     raise ValueError("email name is mandatory")

    #   if not isinstance(address_id, int):
    #     raise TypeError("address_id has to be a int")
    #   if not address_id:
    #     raise ValueError("address_id name is mandatory")
    
    #   sql= "INSERT INTO guest (first_name, last_name, email, address_id) VALUES (?, ?, ?, ?)"
    #   params = tuple([first_name, last_name, email, address_id])
    #   last_row_id, _ = self.execute(sql, params)
    #   return Guest(guest_id=last_row_id, first_name=first_name, last_name=last_name, email=email, address_id=address_id)
    
    # def update_guest_by_last_name(self,
    #                   guest_id:int, 
    #                   new_last_name:str
    #     ) -> None:
    #   sql = "UPDATE guest SET last_name = ? WHERE guest_id = ?"
    #   params = (new_last_name, guest_id)
    #   self.execute(sql, params)

    # def delete_guest_by_id(self, guest_id: int) -> None:
    #     sql = "DELETE FROM guest WHERE guest_id = ?"
    #     self.execute(sql, (guest_id,))