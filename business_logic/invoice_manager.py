import os

import model
import data_access
from datetime import date

class InvoiceManager:
    def __init__(self):
        self.__invoice_da = data_access.InvoiceDataAccess()
    
    def read_all_invoice(self) -> list[model.Invoice]:
        return self.__invoice_da.read_all_invoice()
    
    def read_invoice_by_id(self,
                            invoice_id:int
        ) -> model.Invoice:
        return self.__invoice_da.read_invoice_by_id(invoice_id)
    
    def create_new_invoice(self,
                           booking_id: int,
                           issue_date: date,
                           total_amount: float
        ) -> model.Invoice:
        return self.__invoice_da.create_new_invoice(booking_id, issue_date, total_amount)

    def update_invoice_by_total_amount(self, 
                        invoice_id:int,
                        new_total_amount:float
        )-> None:
        return self.__invoice_da.update_invoice_by_total_amount(invoice_id, new_total_amount)

    def delete_invoice_by_id(self, 
                        invoice_id:int
        ) -> None:
        return self.__invoice_da.delete_invoice_by_id(invoice_id)