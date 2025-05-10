from data_access.base_data_access import BaseDataAccess
from datetime import datetime
from datetime import date
from model.invoice import Invoice

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
            invoice_id, booking_id, issue_date, total_amount = row
            invoice = Invoice(invoice_id, booking_id, issue_date, float(total_amount))
            all_invoices.append(invoice)

        return all_invoices
    
    def read_invoice_by_id(self,
                            invoice_id:int
        ) -> Invoice:
          sql = "SELECT invoice_id, booking_id, issue_date, total_amount FROM invoice WHERE invoice_id = ?"
          row = self.fetchone(sql, (invoice_id,))
          if row:
            return Invoice(*row)
          return None
    
    def create_new_invoice(self,
                           booking_id: int,
                           issue_date: date,
                           total_amount: float
        ) -> Invoice:
        
        if not isinstance(booking_id, int):
            raise TypeError("booking_id must be an integer")
        if not booking_id:
            raise ValueError("booking_id is mandatory")

        if not isinstance(issue_date, date):
            raise TypeError("issue_date must be a date")
        
        if not isinstance(total_amount, (int, float)):
            raise TypeError("total_amount must be a number")
        if total_amount <= 0:
            raise ValueError("total_amount must be greater than 0")

        sql = "INSERT INTO invoice (booking_id, issue_date, total_amount) VALUES (?, ?, ?)"
        params = tuple([booking_id, issue_date, total_amount])
        
        last_row_id, _ = self.execute(sql, params)

        return Invoice(invoice_id=last_row_id, booking_id=booking_id, issue_date=issue_date, total_amount=total_amount)



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