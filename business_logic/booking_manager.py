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
        self.__hotel_dao = data_access.HotelDataAccess()
        self.__invoice_manager = InvoiceManager()
        self.__guest_manager = GuestManager()

        self.__all_guests = self.__guest_manager.read_all_guest()
    
    ## Admin
    def read_all_bookings(self):
        bookings= self.__booking_da.read_all_bookings()
        return bookings

    def update_booking_price_for_guest(self, price_to_set:float, booking_id:int)-> None:
        booking=self.__booking_da.read_booking_by_id(booking_id)
        if booking is None:
            raise ValueError(f"There is no booking ID {booking_id} in the systems")
        if booking.invoice:
            raise ValueError(f"You cannot change a total amount of a booking where there is already an invoice")

        self.__booking_da.update_booking_price_for_guest(price_to_set, booking_id)

## Guest Function
    #Read Functions
    def read_all_av_rooms_by_hotel(self, hotel_id:int, check_out_date:date, check_in_date:date) -> list[model.Room]:
        if check_in_date < date.today():
            raise ValueError("Check-in date cannot be in the past.")

        if check_out_date <= check_in_date:
            raise ValueError("Check-out date must be after check-in date.")

        hotel= self.__hotel_dao.read_hotel_by_id(hotel_id)

        if hotel is None:
            raise ValueError(f"Such hotel ID {hotel_id} does not exist in our systems")


        rooms=  self.__booking_da.read_all_av_rooms_by_hotel(hotel_id, check_out_date, check_in_date)
        return rooms

    def read_av_rooms(self, check_out_date: date, check_in_date: date) -> list[model.Room]:
        if check_in_date >= check_out_date:
            raise ValueError("Check-out date must be after check-in date.")

        rooms= self.__booking_da.read_av_rooms(check_out_date=check_out_date, check_in_date=check_in_date)
        return rooms    
   
    def read_booking_by_id(self, booking_id: int) -> model.Booking:
        bookings = self.__booking_da.read_all_bookings()
        booking_ids= [booking_id for booking in bookings]

        if booking_id not in booking_ids:
            raise ValueError(f"There is no booking id {booking_id}")
        else:
            return self.__booking_da.read_booking_by_id(booking_id)

    def read_bookings_by_guest(self, guest_id:int)-> model.Booking:
        guest= self.__guest_manager.read_guest_by_id(guest_id)
        if guest is None:
            raise ValueError("There is no such guest")
        return self.__booking_da.read_bookings_by_guest(guest_id)   

    def read_av_rooms_city(self, city: str, check_out_date: date, check_in_date: date) -> list[model.Room]:
        if check_in_date < date.today():
            raise ValueError("Check-in date cannot be in the past.")

        if check_out_date <= check_in_date:
            raise ValueError("Check-out date must be after check-in date.")
        
        return self.__booking_da.read_av_rooms_city(city, check_out_date, check_in_date)


    #Admin Function
    def create_new_booking(self, room_id:int, check_in_date:date, check_out_date:date, guest_id:int):
        if check_in_date >= check_out_date:
            raise ValueError("Check-out date must be after check-in date.")
        
        guest= self.__guest_manager.read_guest_by_id(guest_id)
        if guest is None:
            raise ValueError("There is no such guest")
        
        room= self.__room_manager.get_room_by_id(room_id)
        if room is None:
            raise ValueError("There is no such room")
        
        available_rooms = self.read_all_av_rooms_by_hotel(room.hotel.hotel_id, check_out_date, check_in_date)
        available_room_ids = [room.room_id for room in available_rooms]

        if room_id not in available_room_ids:
            raise ValueError("This room isn't available")
        
        # Preis dynamisch anpassen:
        seasonal_price = self.__room_manager.get_price_season(check_in_date, room.price_per_night)
        seasonal_per_night= seasonal_price - room.price_per_night
        room.price_per_night= seasonal_price

        #Berechnung von MWST und Verwaltungskosten
        num_nights = (check_out_date - check_in_date).days
        price = num_nights * room.price_per_night
    
        mwst_satz= 108.1
        verwaltungskosten_satz= 0.1

        verwaltungskosten = price * verwaltungskosten_satz
        base_price = verwaltungskosten + price

        mwst_betrag= base_price - (base_price/mwst_satz*100)

        total_amount= float(round(base_price, 2))

        seasonal= seasonal_per_night*num_nights

        booking= self.__booking_da.create_new_booking(room_id, check_in_date, check_out_date, guest_id, total_amount)

        if booking:
            print("\n Thank you for your booking!")
            print(f"{'-'*70}")
            print(f"{'Stay duration:':<40}{num_nights:.0f} nights")
            print(f"{'Price per night:':<40}CHF {room.price_per_night:>10.2f}")
            print(f"{'Amount for stay:':<40}CHF {price:>10.2f}")
            print(f"{'Seasonal surcharge:':<40}CHF {seasonal:>10.2f}")
            print(f"{'Administrative fee:':<40}CHF {verwaltungskosten:>10.2f}")
            print(f"{'-'*70}")
            print(f"{'included VAT (8.1%):':<40}CHF {mwst_betrag:>10.2f}")
            print(f"{'-'*70}")
            print(f"{'Total amount due:':<39}CHF {total_amount:>10.2f}")
            print(f"{'-'*70}\n")
            return booking
        else:
            return None        
        
    

    def cancell_booking(self, booking_id:int)-> None:
        booking= self.read_booking_by_id(booking_id)
        #Das Check In Datum soll in nicht in der Vergangenheit liegen
        if booking.check_in_date <= date.today():
            raise ValueError("This Booking cannot be cancelled.")
        
        #Die Buchung soll nicht nochmals storniert werden
        if booking.is_cancelled:
            raise ValueError("This Booking has already been cancelled")
        
        #Buchungen, die eine Rechnung haben sollten nicht storniert werden können
        if booking.invoice is not None:
            raise ValueError("This Booking has been billed and cannot be cancelled")
        
        self.__booking_da.cancell_booking(booking_id)
        print (f"Booking ID {booking_id} is cancelled.")
        inv= self.__invoice_manager.create_new_invoice(booking_id, date.today(), 0.00)
        print(f"Invoice of CHF 0.00 has been created!")
        booking.invoice= inv
    
    def billing(self, booking_id:int):
        booking = self.read_booking_by_id(booking_id)
        today = date.today()

        if booking.is_cancelled:
            print(f"You cannot bill an invoice where the booking is cancelled")
            return None
        if booking.check_out_date > today:
            print(f"You cannot bill an invoice where the check_out_date is in the future")
            return None
        if booking.invoice is not None:
            print("You cannot bill a booking where there is already an existing invoice")
            return None  

        inv= InvoiceManager()
        invoice= inv.create_new_invoice(booking_id=booking.booking_id, issue_date=today, total_amount=booking.total_amount)
        booking.invoice= invoice

        return invoice
    
   #Filter Funktion
    def get_guests_by_last_and_firstname(self, last_name: str, first_name: str) -> list[model.Guest]:
        last_name = last_name.strip().lower()
        first_name = first_name.strip().lower()
        
        all_guests = self.__guest_manager.read_all_guest()

        matching_guests = [
            guest for guest in all_guests
            if guest.last_name.strip().lower() == last_name and guest.first_name.strip().lower() == first_name
        ]
        return matching_guests

    #Userfriendly Outputs
    def print_userfriendly_booking(self, bookings: list[model.Booking]):
        for booking in bookings:
            print(model.Booking.show_userfriendly())

    def print_userfriendly_room(self, rooms: list[model.Room]) -> None:
        rooms= self.__room_manager.get_all_rooms()
        for room in rooms:
            print(model.Room.userfriendly(room))
            print(model.RoomType.userfriendly(room))
        
    def print_user_friendly_hotels(self, hotels: list[model.Hotel]) -> None:
        for hotel in hotels:
            print(model.Hotel.show_user_friendly(hotel))


