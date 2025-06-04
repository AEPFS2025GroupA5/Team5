from .invoice import Invoice
from .address import Address
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.booking import Booking

class Guest:
    def __repr__(self):
        return (
        f" \n"
        f"  ID: {self.guest_id}\n"
        f"  Guest's fullname: {self.first_name} {self.last_name}\n"
        f"  Guest's E-Mail: {self.email}\n"
        f"  Guest's Address ID: {self.address}\n"
        f")"
    )

    def __init__(
            self, 
            guest_id:int, 
            first_name:str, 
            last_name:str, 
            email:str , 
            address:Address
        ):

        #Typprüfung
        if guest_id is None:
            raise ValueError("Guest Id is required")
        if not isinstance(guest_id, int):
            raise ValueError("Guest Id has to be an integer")
        
        if first_name is None:
            raise ValueError("First name is required")
        if not isinstance(first_name, str):
            raise ValueError("First name has to be a string")

        if last_name is None:
            raise ValueError("Last name is required")
        if not isinstance(last_name, str):
            raise ValueError("Last name has to be a string")        

        if email is None:
            raise ValueError("E-Mail is required")
        if not isinstance(email, str):
            raise ValueError("E-Mail has to be a string")     
        
        if address is None:
            raise ValueError("Address Id is required")
        if not isinstance(address, Address):
            raise ValueError("Adress has to be an object")

        self.__guest_id = guest_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self.__invoice: list[Invoice] = [] #Aggregation Invoice
        self.__address:Address = address    #Aggregation mit Address
        self.__bookings: list[Booking] = [] #Aggregation Booking leere Liste, wo man alle Buchungen vom Kunden sehen kann

    #Getter Funktion vom Invoices
    @property
    def invoice(self):
        return self.__invoice
    
    #Getter Funktion vom Address
    @property
    def address(self):
        return self.__address

    #Get vom Booking
    @property
    def bookings(self):
        return self.__bookings

    #Getter and Setter vom Guest
    @property
    def guest_id(self):
        return self.__guest_id
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, new:str):
        if not isinstance(new, str):
            raise ValueError("First Name has to be a string")
        if not new:
            raise ValueError("First Name is required")
        else:
            self._first_name = new
            return f"You have changed First Name into: {self.first_name}"

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new:str):
        if not isinstance(new, str):
            raise ValueError("Last Name has to be a string")
        if not new:
            raise ValueError("Last Name is required")
        else:
            self._last_name = new
            return f"You have changed Last Name into: {self._last_name}"

    @property
    def email(self):
        return self._email  

    @email.setter
    def email(self, new:str):
        if not isinstance(new, str):
            raise ValueError("E-Mail has to be a string")
        if not new:
            raise ValueError("E-Mail is required")
        if not "@" in new:
            raise ValueError('E-Mail needs an "@" in their address')
        else:
            self._email=new
            return f"You have changed E-Mail into: {self._email}"
        
    #Userfriendly
    def userfriendly(self):
        return f"""👤 Guest Details
            ID: {self.guest_id}
            Name: {self.first_name} {self.last_name}
            E-Mail: {self.email}
            {self.address.show_user_friendly()}
            """