import os

import model
from model.invoice import Invoice
import data_access
from datetime import date
from business_logic.room_manager import RoomManager
from business_logic.invoice_manager import InvoiceManager
from business_logic.guest_manager import GuestManager

class BookingManager:
    def __init__(self):
        self.__booking_da = data_access.BookingDataAccess()
        self.__room_da = data_access.RoomDataAccess()
        self.__room_manager = RoomManager()
        self.__invoice_manager = InvoiceManager()
        self.__guest_manager = GuestManager()

        self.__all_guests = self.__guest_manager.read_all_guest()
    
    ## Admin
    def read_all_bookings(self):
        bookings= self.__booking_da.read_all_bookings()
        return bookings
        #admin display

    ## Guest Function
    def read_all_av_rooms_by_hotel(self, hotel_id:int, check_out_date:date, check_in_date:date) -> list[model.Room]:
        rooms=  self.__booking_da.read_all_av_rooms_by_hotel(hotel_id, check_out_date, check_in_date)
        return rooms
        #userfriendly display()

    def read_av_rooms(self, check_out_date: date, check_in_date: date) -> list[model.Room]:
        rooms= self.__booking_da.read_av_rooms(check_out_date=check_out_date, check_in_date=check_in_date)
        return rooms    
   
    def create_new_booking(self, room_id:int, check_in_date:date, check_out_date:date, guest_id:int):      
        available_rooms = self.read_all_av_rooms_by_hotel(self.__room_da.read_hotel_by_roomId(room_id).hotel_id, check_out_date, check_in_date)
        available_room_ids = [room_id for room in available_rooms]

        room= self.__room_da.read_room_by_id(room_id)
        # Preis dynamisch anpassen:
        seasonal_price = self.__room_manager.get_price_season(room.price_per_night)
        seasonal_per_night= seasonal_price - room.price_per_night
        room.price_per_night= seasonal_price

        #Berechnung von MWST und Verwaltungskosten
        num_nights = (check_out_date - check_in_date).days
        price = num_nights * room.price_per_night
    

        mwst_satz= 108.1
        verwaltungskosten_satz= 0.1

        verwaltungskosten = price * verwaltungskosten_satz
        base_price = verwaltungskosten + price

        vr_kost= verwaltungskosten/mwst_satz*100

        mwst_betrag= base_price - (base_price/mwst_satz*100)

        total_amount= float(round(base_price, 2))

        seasonal= seasonal_per_night*num_nights

        sub_total= float(round(total_amount-mwst_betrag, 2))

        #Userfriendly Ausgabe für die erstellte Buchung mit Auszug aller Kosten und MWST Betrag -> Aus simplen Gründen haben wir 8.1% genommen
        print(f"   Thank you for your booking!")
        print(f"   🛏 Base Price ({num_nights:.2f} nights at CHF {room.price_per_night:.2f} ): CHF {price:.2f} ")
        print(f"   Seasonal Fee: CHF {seasonal}")
        print(f"   🛠 Administrative Fee: CHF {vr_kost:.2f} ")
        print(f"-------------------------------------------")
        print(f"   Subtotal: {sub_total:.2f}")
        print(f"   🧾 VAT (8.1%): CHF {mwst_betrag:.2f} ")
        print(f"   💵 Total Amount: CHF {total_amount:.2f} ")

        return self.__booking_da.create_new_booking(room_id, check_in_date, check_out_date, guest_id, total_amount)
        
    def read_booking_by_id(self, booking_id: int) -> model.Booking:
        bookings = self.__booking_da.read_all_bookings()
        booking_ids= [booking_id for booking in bookings]

        if booking_id not in booking_ids:
            raise ValueError(f"There is no booking id {booking_id}")
        if not booking_id:
            raise ValueError("Booking Id is required")
        if not isinstance(booking_id, int):
            raise ValueError("Booking ID has to be an integer")
        else:
            return self.__booking_da.read_booking_by_id(booking_id)

    def read_bookings_by_guest(self, guest_id:int)-> model.Booking:
        return self.__booking_da.read_bookings_by_guest(guest_id)   

    def read_av_rooms_city(self, city: str, check_out_date: date, check_in_date: date) -> list[model.Room]:
        return self.__booking_da.read_av_rooms_city(city, check_out_date, check_in_date)

    def cancell_booking(self, booking_id:int)-> None:
        self.__booking_da.cancell_booking(booking_id)
        print (f"❌ Buchung mit ID {booking_id} wurde storniert.")

    ## Fakturierung
    def billing(self):
        bookings = self.read_all_bookings()
        today = date.today()
        billed_bookings = []

        for b in bookings:
            if b.is_cancelled:
                continue
            if b.check_out_date > today:
                continue
            if b.invoice is not None:
                continue  

            inv= InvoiceManager()
            invoice= inv.create_new_invoice(booking_id=b.booking_id, issue_date=today, total_amount=b.total_amount)


            print(f"Rechnung erstellt für Buchung {b.booking_id} (CHF {b.total_amount:.2f})")
            billed_bookings.append(b)

        return billed_bookings
    
    #Filterung
    # def get_guests_by_last_and_firstname(self, last_name:str, first_name:str) -> list[model.Guest]:
    #     matching_guests= [guest for guest in self.__all_guests if last_name.lower() in guest.last_name.lower() and first_name.lower() in guest.first_name.lower()]
    #     return matching_guests

    def get_guests_by_last_and_firstname(self, last_name: str, first_name: str) -> list[model.Guest]:
        last_name = last_name.strip().lower()
        first_name = first_name.strip().lower()
        
        matching_guests = [
            guest for guest in self.__all_guests
            if guest.last_name.strip().lower() == last_name and guest.first_name.strip().lower() == first_name
        ]
        return matching_guests

    #Userfriendly Outputs
    def print_userfriendly_booking(self, bookings: list[model.Booking]):
        for booking in bookings:
            print(model.Booking.show_userfriendly())

    def print_userfriendly_room(self, rooms: list[model.Room]) -> None:
        room= self.__room_manager.get_all_rooms()
        for room in rooms:
            print(model.Room.userfriendly(room, room))
            print(model.RoomType.userfriendly(room))
        
    def print_user_friendly_hotels(self, hotels: list[model.Hotel]) -> None:
        for hotel in hotels:
            print(model.Hotel.show_user_friendly(hotel))