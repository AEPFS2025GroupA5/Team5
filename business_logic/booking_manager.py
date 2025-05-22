import os

import model
import data_access
from datetime import date
from data_access.booking_data_access import BookingDataAccess

class BookingManager:
    def __init__(self):
        self.__booking_da = BookingDataAccess()
    
    def read_all_bookings(self) -> list[model.Booking]:
        return self.__booking_da.read_all_bookings()

    def read_booking_by_id(self, booking_id: int) -> model.Booking | None:
        return self.__booking_da.read_booking_by_id(booking_id)

    def create_new_booking(
        self,
        check_in_date: date,
        check_out_date: date,
        total_amount: float,
        guest_id: int
    ) -> model.Booking:
        return self.__booking_da.create_new_booking(check_in_date, check_out_date, total_amount, guest_id)

    def update_booking(self, booking: model.Booking) -> None:
        return self.__booking_da.update_booking(booking)

    def delete_booking_by_id(self, booking_id: int) -> None:
        return self.__booking_da.delete_booking_by_id(booking_id)

    def _row_to_booking(self, row: tuple) -> model.Booking:
        return self.__booking_da._row_to_booking(row)