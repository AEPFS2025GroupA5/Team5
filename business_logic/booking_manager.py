import os

import model
from model.invoice import Invoice
import data_access
from datetime import date
from business_logic.invoice_manager import InvoiceManager

class BookingManager:
    def __init__(self):
        self.__guest_da = data_access.BookingDataAccess()
    
    def read_all_bookings(self):
        return self.__guest_da.read_all_bookings()

    def read_all_av_rooms(self, hotel_id:int, check_out_date:date, check_in_date:date) -> list[model.room]:
        return self.__guest_da.read_all_av_rooms(hotel_id, check_out_date, check_in_date)

    def create_new_booking(self, room_id:int, check_in_date:date, check_out_date:date, guest_id:int):
        room_mo = data_access.RoomDataAccess()
        
        room_dao = room_mo.read_room_by_id(room_id)
        hotel_dao = room_mo.read_hotel_by_roomId(room_id)

        available_rooms = self.read_all_av_rooms(hotel_dao.hotel_id, check_out_date, check_in_date)
        available_room_ids = [room_id for room in available_rooms]
        if room_id not in available_room_ids:
            raise ValueError("Room is not available in the selected period")
        else:
            return self.__guest_da.create_new_booking(room_id, check_in_date, check_out_date, guest_id)
        
    def read_booking_by_id(self, booking_id: int) -> model.Booking:
        if not booking_id:
            raise ValueError("Booking Id is required")
        if not isinstance(booking_id, int):
            raise ValueError("Booking ID has to be an integer")

        return self.__guest_da.read_booking_by_id(booking_id)
    

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