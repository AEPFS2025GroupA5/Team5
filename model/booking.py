from model.invoice import Invoice
from model.guest import Guest
from datetime import date
from model.hotel import Hotel
from model.room import Room


class Booking:
    def __repr__(self):
        return (
            f"Booking(\n"
            f"  ID: {self.__booking_id}\n"
            f"  Room: {self.room}\n"
            f"  Check In Date: {self.check_in_date}\n"
            f"  Check Out Date: {self.check_out_date}\n"
            f"  Total Amount of the Booking: {self.__total_amount}\n"
            f"  Guest: {self.__guest}\n"
            f"  Is cancelled: {self.__is_cancelled}\n"
            f")"
        )
    
    def __init__(
        self, 
        booking_id: int, 
        room:Room,
        check_in_date: date, 
        check_out_date: date, 
        total_amount: float, 
        guest:Guest,
        is_cancelled: bool = False,  
    ):
        
        # Typprüfung
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
        
        if not isinstance(guest, Guest):
            raise ValueError("guest has to be an integer")
        
        if not isinstance(room, Room):
            raise ValueError("room id has to be an integer")
            
        if not isinstance(is_cancelled, bool):
            raise ValueError("is cancelled has to be a boolean")

        self.__booking_id = booking_id
        self.__room:Room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__total_amount = total_amount
        self.__guest:Guest = guest #Aggregation mit Guest
        self.__is_cancelled = is_cancelled
        self.__invoice: Invoice = None #Komposition mit Invoice
        
    def show_userfriendly(self):
        return f"""
            Booking-ID: {self.booking_id}
            Check-In: {self.check_in_date}
            Check-Out: {self.check_out_date}
            Total Amount: CHF{self.total_amount:.2f} 
            Invoice: {self.invoice}
            Cancelled: {self.is_cancelled}
            """

    # Getter für Zugriff auf die Rechnung
    @property
    def invoice(self):
        return self.__invoice
    
    @invoice.setter
    def invoice(self, thing):
        if not isinstance(thing, Invoice) and thing is not None:
            raise ValueError("invoice must be an Invoice object or None.")
        self.__invoice = thing
    
    # Getter für Zugriff auf den Gast
    @property
    def guest(self):
        return self.__guest
    
    #Getter für Zugriff auf Room
    @property
    def room(self):
        return self.__room

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
        if not self.new:
            raise ValueError("Booking ID is required")
        self.__is_cancelled = new
        print(f'You have changed "is_cancelled" to: {self.__is_cancelled}')