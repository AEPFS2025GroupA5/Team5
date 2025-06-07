from datetime import date
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from model.guest import Guest
    from model.booking import Booking

class Invoice:
    def __repr__(self):
        return  f"Invoicenumber: {self.invoice_id}\n" \
                f"Booking Id: {self.booking_id}\n" \
                f"Issue Date: {self.issue_date}\n" \
                f"Total Amount: CHF {self.total_amount}\n" \

    def __init__(
        self, 
        invoice_id: int, 
        booking_id: int, 
        issue_date: date, 
        total_amount: float, 
    ):

        #Typprüfung
        if invoice_id is None:
            raise ValueError("Invoice Id is required")
        if not isinstance(invoice_id, int):
            raise ValueError("Invoice Id has to be an integer")
        
        if booking_id is None:
            raise ValueError("Booking Id is required")
        if not isinstance(booking_id, int):
            raise ValueError("Booking Id has to be an integer")
        
        if issue_date is None:
            raise ValueError("Issue Date is required")
        if not isinstance(issue_date, date):
            raise ValueError("Issue Date has to be a date")
        
        if total_amount is None:
            raise ValueError("Total Amount is required")
        if not isinstance(total_amount, (int, float)):
            raise ValueError("Total amount must be a number (int or float)")

        self.__invoice_id = invoice_id
        self._issue_date = issue_date
        self._total_amount = total_amount
        self.booking_id = booking_id
      
    # Get und Set für Invoice 
    @property
    def invoice_id(self):
        return self.__invoice_id

    @property
    def issue_date(self):
        return self._issue_date

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter 
    def total_amount(self, new:float):
        if not isinstance(new, float):
            raise ValueError("The new amount has to be a float")
        if new <0:
            raise ValueError("new invoice amount has to be greater than 0")
        else:
            self._total_amount= new