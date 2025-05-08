#Achtung hier ist ein zirkulärer Import, den ich irgendwie nicht lösen kann.

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from guest import Guest

class Invoice:
    def __str__(self):
        return  f"Invoice number: {self.invoice_id}\n" \
                f"Issue Date: {self.issue_date}\n" \
                f"Paid: {self.is_paid}\n" \

    def __init__(
        self, 
        invoice_id: int, 
        issue_date: date, 
        inv_amount: float, 
        is_paid: bool = False, 
        guest:"Guest" = None
    ):

        #Typprüfung
        if not invoice_id:
            raise ValueError("Invoice Id is required")
        if not isinstance(invoice_id, int):
            raise ValueError("Invoice Id has to be a integer")
        
        if not issue_date:
            raise ValueError("Issue Date is required")
        if not isinstance(issue_date, date):
            raise ValueError("Issue date has to be a date")
        
        if not isinstance(inv_amount, float):
            raise ValueError("Invoice Amount has to be a float")
        if inv_amount < 0:
            raise ValueError("Invoice has to be over CHF 0")

        if not isinstance(is_paid, bool):
            raise ValueError("Invoice has to be a bool")
        if is_paid:
            raise ValueError("Invoice has to be unpaid")
        
        # if not isinstance(guest, Guest):
        #     raise ValueError("guest has to be a Guest-object!")

        self.__invoice_id = invoice_id
        self._issue_date = issue_date
        self._inv_amount = inv_amount
        self._is_paid = is_paid
        self.__guest:Guest = guest
    
    #Problem: wo genau werden dann die Invoices gespeichert? Soll ich es beim Guest lassen oder doch lieber beim Booking eine leere Liste ertellen mit Rechnungen? 

    #Funktionen
    def get_details(self):
        return  f"Invoicenumber: {self.invoice_id}\n" \
                f"{self.guest}\n" \
                f"Issue Date: {self.issue_date}\n" \
                f"Total Amount: CHF {self.inv_amount:.2f}\n" \
                f"Paid Status: {self.is_paid}\n"

    # def get_unpaid(self):
    #     print("Unpaid Invoices:")
    #     if not self.is_paid:
    #         return  f"Invoicenumber: {self.invoice_id}\n" \
    #                 f"{self.guest}\n" \
    #                 f"Total Amount: CHF {self.inv_amount:.2f}\n" \
    #                 f"Paid Status: {self.is_paid}\n" 
    #     else:
    #         None


    #Get für Guest
    @property
    def guest(self):
        return self.__guest
    
    #Get und Set für Invoice 
    @property
    def invoice_id(self):
        return self.__invoice_id

    @property
    def issue_date(self):
        return self._issue_date

    @property
    def inv_amount(self):
        return self._inv_amount

    @inv_amount.setter #Rabatt als optionale UserStory
    def inv_amount(self, new:float):
        if not isinstance(new, float):
            raise ValueError("The new amount has to be a float")
        if new <0:
            raise ValueError("new invoice amount has to be greater than 0")
        else:
            self._inv_amount= new
            #Hier möglicherweise noch im Guest ändern die Liste (vllt. mit pop() und sagen self.__invoiceId == list mit der gleichen ID?)

    @property
    def is_paid(self):
        return self._is_paid

    @is_paid.setter
    def is_paid(self, new:bool):
        if not isinstance(new, bool):
            raise ValueError("is_paid must be a boolean.")
        if not self._is_paid and new:
            self._is_paid = True
            print(f'You have changed "is_paid" to: {self.is_paid}')
        else:
            raise ValueError("Invoice already paid or invalid update.")
        
