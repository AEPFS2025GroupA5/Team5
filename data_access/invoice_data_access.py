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

        if rows:
            for row in rows:
                invoice_id, booking_id, issue_date, total_amount = row
                total_amount = float(f"{total_amount:.2f}")
                invoice = model.Invoice(invoice_id, booking_id, issue_date, total_amount)
                all_invoices.append(invoice)

            return all_invoices
        else:
            return None

    def read_invoice_by_id(self,
                            invoice_id:int
        ) -> model.Invoice:
        if not invoice_id:
            raise ValueError("Invoice ID is required")
        if not isinstance(invoice_id, int):
            raise ValueError("Invoice ID has to be an integer")

        sql = "SELECT invoice_id, booking_id, issue_date, total_amount FROM invoice WHERE invoice_id = ?"
        row = self.fetchone(sql, (invoice_id,))
        if row:
            inv= model.Invoice(*row)
            total_amount= float(inv.total_amount)
            sub_total= float(round(total_amount/108.1*100,2))
            mwst_betrag= total_amount - sub_total
            print(f"   Subtotal of Invoice: {sub_total:.2f}")
            print(f"   MwSt (8.1%): CHF {mwst_betrag:.2f} ")
            print(f"   Gesamtbetrag: CHF {total_amount:.2f} ")
            return inv
        return None
    
    def create_new_invoice(self,
                           booking_id: int,
                           issue_date: date,
                           total_amount: float
        ) -> model.Invoice:
        
        if not isinstance(booking_id, int):
            raise TypeError("Booking Id must be an integer")
        if booking_id is None:
            raise ValueError("Booking Id is mandatory")

        if not isinstance(issue_date, date):
            raise ValueError("Issue Date must be a date")
        if issue_date is None:
            raise ValueError("Issue Date is mandatory")
        
        if not isinstance(total_amount, (int, float)):
            raise ValueError("Total amount must be a number (int or float)")
        if total_amount < 0:
            raise ValueError("Total Amount must be greater than 0")
        if total_amount is None:
            raise ValueError("Totale Amount is mandatory")

        sql = "INSERT INTO invoice (booking_id, issue_date, total_amount) VALUES (?, ?, ?)"
        params = tuple([booking_id, issue_date, total_amount])
        
        last_row_id, _ = self.execute(sql, params)

        invoice= model.Invoice(invoice_id=last_row_id, booking_id=booking_id, issue_date=issue_date, total_amount=total_amount)
        print(f"Invoice created for booking {booking_id} (CHF {total_amount:.2f})")

        return invoice

    def update_invoice_by_total_amount(self, 
                        invoice_id:int,
                        new_total_amount:float
        )-> None:
        if not isinstance(invoice_id, int):
            raise ValueError("Invoice Id has to be an integer")
        if invoice_id is None:
            raise ValueError("In order to change the total amount you need to give an Invoice ID")
        
        if not isinstance(new_total_amount, float):
            raise ValueError("The new total amount has to be a float")
        if new_total_amount is None:
            raise ValueError(f"In order to change the total amount of this invoice ID {invoice_id} you need to put in a total amount")

        else:
            sql = "UPDATE invoice SET total_amount = ? WHERE invoice_id = ?"
            params = (new_total_amount, invoice_id)
            self.execute(sql, params)

    def delete_invoice_by_id(self, 
                        invoice_id:int
        ) -> None:
        if not isinstance(invoice_id, int):
            raise ValueError("Invoice Id has to be an integer")
        if invoice_id is None:
            raise ValueError("In order to delete a whole invoice you need to give an invoice ID")
        
        else:
            sql = "DELETE FROM invoice WHERE invoice_id = ?"
            self.execute(sql, (invoice_id,))