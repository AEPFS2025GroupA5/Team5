from data_access.base_data_access import BaseDataAccess
from datetime import datetime
from datetime import date
import model

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, 
                 db_path: str = None
        ):
        super().__init__(db_path)
    
    def read_all_invoice(self) -> list[model.Invoice]:
        sql = """
        SELECT invoice_id, booking_id, issue_date, total_amount FROM invoice
        """
        rows = self.fetchall(sql)
        all_invoices = []

        for row in rows:
            invoice_id, booking_id, issue_date, total_amount = row
            # Stelle sicher, dass total_amount ein Float mit zwei Dezimalstellen ist
            total_amount = float(f"{total_amount:.2f}")
            invoice = model.Invoice(invoice_id, booking_id, issue_date, total_amount)
            all_invoices.append(invoice)

        return all_invoices
    
    def read_invoice_by_id(self,
                            invoice_id:int
        ) -> model.Invoice:
          sql = "SELECT invoice_id, booking_id, issue_date, total_amount FROM invoice WHERE invoice_id = ?"
          row = self.fetchone(sql, (invoice_id,))
          if row:
            return model.Invoice(*row)
          return None
    
    def create_new_invoice(self,
                           booking_id: int,
                           issue_date: date,
                           total_amount: float
        ) -> model.Invoice:
        
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

        return model.Invoice(invoice_id=last_row_id, booking_id=booking_id, issue_date=issue_date, total_amount=total_amount)

    def update_invoice_by_total_amount(self, 
                        invoice_id:int,
                        new_total_amount:float
        )-> None:
        sql = "UPDATE invoice SET total_amount = ? WHERE invoice_id = ?"
        params = (new_total_amount, invoice_id)
        self.execute(sql, params)

    def delete_invoice_by_id(self, 
                        invoice_id:int
        ) -> None:
        sql = "DELETE FROM invoice WHERE invoice_id = ?"
        self.execute(sql, (invoice_id,))