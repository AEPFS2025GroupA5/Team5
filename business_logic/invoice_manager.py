import os
import business_logic
import model
import data_access
from datetime import date

class InvoiceManager:
    def __init__(self):
        self.__invoice_da = data_access.InvoiceDataAccess()
        self.__booking_dao= data_access.BookingDataAccess()
        self.__guest_dao= data_access.GuestDataAccess()
        self.__guest_manager= business_logic.GuestManager()
    
    #Read Functions
    def read_all_invoice(self) -> list[model.Invoice]:
        return self.__invoice_da.read_all_invoice()
    
    def read_invoice_by_id(self,
                            invoice_id:int
        ) -> model.Invoice:
        return self.__invoice_da.read_invoice_by_id(invoice_id)
    
    def read_invoices_by_guest(self, guest_id:int):
        guest= self.__guest_manager.read_guest_by_id(guest_id)

        if not guest:
            raise ValueError("There is no such guest in our systems")
        else:
            return self.__invoice_da.read_invoices_by_guest(guest_id)

    
    #Admin Functions
    def create_new_invoice(self,
                           booking_id: int,
                           issue_date: date,
                           total_amount: float
        ) -> model.Invoice:
        booking= self.__booking_dao.read_booking_by_id(booking_id)
        if booking is None:
            raise ValueError("There is no such booking in our systems")
        
        return self.__invoice_da.create_new_invoice(booking_id, issue_date, total_amount)

    def update_invoice_by_total_amount(self, 
                        invoice_id:int,
                        new_total_amount:float
        )-> None:
        invoice= self.__invoice_da.read_invoice_by_id(invoice_id)
        if invoice is None:
            raise ValueError("There is no such Invoice in our systems")

        return self.__invoice_da.update_invoice_by_total_amount(invoice_id, new_total_amount)

    def delete_invoice_by_id(self, 
                        invoice_id:int
        ) -> None:
        invoice= self.__invoice_da.read_invoice_by_id(invoice_id)
        if invoice is None:
            raise ValueError("There is no such Invoice in our systems")
        
        return self.__invoice_da.delete_invoice_by_id(invoice_id)