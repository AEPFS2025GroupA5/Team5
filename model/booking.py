from .invoice import Invoice
from .guest import Guest
from datetime import date
from hotel import Hotel

class Booking:

    def __repr__(self):
        return (
            f"Booking(\n"
            f"  ID: {self.__booking_id}\n"
            f"  Check In Date: {self.check_in_date}\n"
            f"  Check Out Date: {self.check_out_date}\n"
            f"  Total Amount of the Booking: {self.__total_amount}\n"
            f"  Guest ID: {self.__guest}\n"
            f"  Is cancelled: {self.__is_cancelled}\n"
            f")"
        )

    def __init__(
        self, 
        booking_id: int, 
        check_in_date: date, 
        check_out_date: date, 
        total_amount: float, 
        hotel:Hotel, 
        guest:Guest,
        is_cancelled: bool = False,  
        invoice:Invoice =None
    ):
        
        #Typprüfung
        if not booking_id:
            raise ValueError("booking Id is required")
        if not isinstance(booking_id, int):
            raise ValueError("booking Id has to be an integer")
        
        if not check_in_date:
            raise ValueError("check in date is required")
        if not isinstance(check_in_date, date):
            raise ValueError("check in date has to be a date")
        
        if not check_out_date:
            raise ValueError("check out date is required")
        if not isinstance(check_out_date, date):
            raise ValueError("check out date has to be a date")
        
        if total_amount < 0:
            raise ValueError("total amount has to be over CHF 0")
        if not isinstance(total_amount, float):
            raise ValueError("total amount has to be a float")
        
        if not isinstance(hotel, Hotel):
            raise ValueError("hotel has to be a Hotel-object!")
        
        if not isinstance(guest, Guest):
            raise ValueError("guest has to be a Guest-object!")
        
        if is_cancelled:
            raise ValueError("is cancelled has to be false")        
        if not isinstance(is_cancelled, bool):
            raise ValueError("is cancelled has to be a boolean")

        self.__booking_id = booking_id
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__total_amount = total_amount
        self.__hotel:Hotel = hotel #Aggregation mit Hotel
        self.__guest:Guest = guest #Aggregation mit Guest
        self.__is_cancelled = is_cancelled
        self.__invoice: Invoice = None #Komposition mit Invoice

    #Funktion, wo man den Total Amount berechnet mit Nebenkosten (mit Room verbinden und base price nutzen)

    # def create_invoice(self):
    #     if not isinstance(self.__total_amount, float):
    #         raise ValueError("Total amount must be a float.")
        
    #     if not self.__total_amount >0:
    #         raise ValueError("Total amount has to be over CHF 0")
        
    #     if self.__is_cancelled:
    #         raise ValueError("Booking is cancelled. Cannot create invoice.")

        # if self.__check_out_date > date.today():
        #     raise ValueError("Client is still in the hotel. Try invoicing after checkout.")

        #Invoice erzeugen lassen
        # self.__invoice = Invoice(self.__booking_id, self.__check_out_date, self.__total_amount, False, self.__guest)
        # print(f"Invoice with the Id {self.__invoice.invoice_id} has been created.\n")
    
        #Rechnung wird mit dem Kunden verknüpft (Aggregation)
        # if self.__guest:
        #     self.__guest.add_invoice(self.__invoice)
        #     print(self.__invoice.get_details())

    # Getter für Zugriff auf die Rechnung
    @property
    def invoice(self):
        return self.__invoice
    
    # Getter für Zugriff auf den Gast
    @property
    def guest(self):
        return self.__guest
    
    #Getter für Zugriff auf Hotel
    @property
    def hotel(self):
        return self.__hotel

    #Getter and Setter für Zugriff auf Booking relevante Attribute
    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def check_in_date(self):
        return self.__check_in_date

    @property
    def check_out_date(self):
        return self.__check_out_date

    @property
    def is_cancelled(self):
        return self.__is_cancelled

    @is_cancelled.setter #Man erlaubt nur zu stornieren und niemals zurückzunehmen, da es auch in der Praxis so ist.
    def is_cancelled(self, new:bool):
        if not isinstance(new, bool):
            raise ValueError("It has to be a bool")
        if not new:
            raise ValueError("You cannot uncancell an already cancelled booking")
        else:
            self.__is_cancelled = new
            print(f'You have changed "is_cancelled" to: {self.__is_cancelled}')