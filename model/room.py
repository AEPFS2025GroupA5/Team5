from datetime import date
from room_type import RoomType

class Room:
    def __init__(       
        self,
        room_id: int,
        room_number: str,
        roomtype: RoomType,      
        base_price: float
    ):
        
        if not room_id:
            raise ValueError("room_id is required")
        if not isinstance(room_id, int):
            raise TypeError("room_id is to be an integer")
        
        if not room_number:
            raise ValueError("room_number is required")
        if not isinstance(room_number, str):
            raise TypeError("room_number must be a string")
        
        if not isinstance(roomtype, RoomType):
            raise TypeError("roomtype must be a RoomType-object!")
        
        if not isinstance(base_price, (int, float)):
            raise TypeError("base_price must be an float")
        if base_price < 0:
            raise ValueError("base_price has to be positiv")
            
        self._room_id = room_id
        self._room_number = room_number
        self._roomtype:RoomType = roomtype
        self._base_price = float(base_price)
       
        #Leere Booking liste erstmal
        self._bookings = []
        

    @property
    def room_id(self):
        return self._room_id

    @property
    def room_number(self):
        return self._room_number

    @property
    def base_price(self):
        return self._base_price

 ##Setter für Price, wir prüfen den Type und achten darauf das es über 0 ist, sonst Error    
    @base_price.setter
    def base_price(
        self,
        new_price: float
        ) -> None:
        if not isinstance(new_price, float):
            raise TypeError("base_price must be a float")
        if new_price < 0:
            raise ValueError("base_price must be >= 0")
        else:
            self._base_price = new_price

    def price_for_nights(
            self,
            nights:int,
    ) -> float:
        if not isinstance(nights, int):
            raise TypeError("Nights must be int")
        if nights < 0:
            raise ValueError ("Nights must be postiv")
        return self._base_price * nights
 #User Story 2
    def get_details(self):
        return  f" Room ID: {self._room_id}, \n " \
                f"Room Number: {self._room_number}, \n " \
                f"Base Price: {self._base_price:.2f}, \n " \
                f"Max Guests: {self._roomtype.max_guests}, \n " \
                f"Room Type: {self._roomtype.name}, \n " \
                f"Description: {self._roomtype.description}\n " \
                f"Amenities: {self._roomtype.amenities}\n " \
        
    
    
    def is_available(
        self,
        check_in:date,
        check_out:date
        ) -> bool:
        #mit der Booking klasse checken ob er Raum verfügbar ist
        for (start, end) in self._bookings:
            if not (check_out <= start or check_in >= end):
                return False
        return True
            

    def book(
            self,
            check_in:date,
            check_out:date,
            guest_count:int      
    ) -> None: 
        if not isinstance(check_in, date) or not isinstance(check_out, date):
            raise TypeError("check_in and check_out must be date-objekts")
        if check_out <= check_in:
            raise ValueError("check_out must be after check_in")
        if not isinstance(guest_count, int) or guest_count < 1:
            raise ValueError("guest_count must be positiv")
        
        #Max-Gäste prüfugen
        if guest_count > self._roomtype.max_guests:
            raise ValueError("Too many Guests for this Roomtype")
        #Verfügbarkeit prüfen
        if not self.is_available(check_in,check_out):
            raise ValueError("Room is not available in this Timeframe")
        
        self._bookings.append((check_in, check_out))
        print("Room was booked!")
   
    def cancel(
            self,

    ):
        #Das canceln geht wahrscheinlich dann eher in der Booking Class
        pass
    

 
#Testdaten
suite1 = RoomType(20,"solo suite", 1, ["Wlan", "Tisch", "usw"], "Ist ganz okay")
test2 = Room(1, "1. OG ", suite1, 20.00)
print(test2.get_details())


#Buchung simulieren

test2.book(date(2025, 12, 20), date(2025, 12, 25), 1)

testt= test2.is_available(date(2025,10,20), date(2025, 10, 28))
print(testt)


