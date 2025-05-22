from datetime import date
from data_access.base_data_access import BaseDataAccess
from data_access.guest_data_access import GuestDataAccess
import model


class BookingDataAccess(BaseDataAccess):
    """
    Data Access Object for Booking-related operations in the database.
    """
    def __init__(self, db_path: str = None):
        """
        Initialize with an optional database path; if None, uses environment variable.
        """
        super().__init__(db_path)

    def read_all_bookings(self) -> list[model.Booking]:
        """
        Retrieve all bookings from the database.
        """
        sql = (
            "SELECT booking_id, check_in_date, check_out_date, "
            "total_amount, guest_id, is_cancelled "
            "FROM booking"
        )
        rows = self.fetchall(sql)
        return [self._row_to_booking(row) for row in rows]

    def read_booking_by_id(self, booking_id: int) -> model.Booking | None:
        """
        Retrieve a single booking by its ID; returns None if not found.
        """
        if booking_id is None:
            raise ValueError("booking_id is required")
        sql = (
            "SELECT booking_id, check_in_date, check_out_date, "
            "total_amount, guest_id, is_cancelled "
            "FROM booking WHERE booking_id = ?"
        )
        row = self.fetchone(sql, (booking_id,))
        return self.row_to_booking(row) if row else None

    def create_new_booking(
        self,
        check_in_date: date,
        check_out_date: date,
        total_amount: float,
        guest_id: int
    ) -> model.Booking:
        """
        Insert a new booking and return the created Booking object.
        """
        # Validate inputs
        if not isinstance(check_in_date, date) or not isinstance(check_out_date, date):
            raise TypeError("check_in_date and check_out_date must be date objects")
        if check_out_date <= check_in_date:
            raise ValueError("check_out_date must be after check_in_date")
        if not isinstance(total_amount, (int, float)) or total_amount < 0:
            raise ValueError("total_amount must be a non-negative number")
        if not isinstance(guest_id, int):
            raise TypeError("guest_id must be an integer")

        sql = (
            "INSERT INTO booking (check_in_date, check_out_date, total_amount, guest_id) "
            "VALUES (?, ?, ?, ?)"
        )
        params = (check_in_date, check_out_date, float(total_amount), guest_id)
        booking_id, _ = self.execute(sql, params)

        guest = GuestDataAccess(self._db_connection_str if hasattr(self, '_BaseDataAccess__db_connection_str') else None).read_guest_by_id(guest_id)
        return model.Booking(
            booking_id=booking_id,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            total_amount=float(total_amount),
            guest=guest
        )

    def update_booking(self, booking: model.Booking) -> None:
        """
        Update an existing booking record in the database.
        """
        if booking is None:
            raise ValueError("booking is required")
        sql = (
            "UPDATE booking SET check_in_date = ?, check_out_date = ?, "
            "total_amount = ?, is_cancelled = ?, guest_id = ? "
            "WHERE booking_id = ?"
        )
        params = (
            booking.check_in_date,
            booking.check_out_date,
            booking.total_amount,
            booking.is_cancelled,
            booking.guest.guest_id,
            booking.booking_id
        )
        self.execute(sql, params)

    def delete_booking_by_id(self, booking_id: int) -> None:
        """
        Delete a booking by its ID.
        """
        if booking_id is None:
            raise ValueError("booking_id is required")
        sql = "DELETE FROM booking WHERE booking_id = ?"
        self.execute(sql, (booking_id,))

    def row_to_booking(self, row: tuple) -> model.Booking:
        """
        Map a SQL row tuple to a Booking model instance.
        """
        booking_id, check_in, check_out, amount, guest_id, is_cancelled = row
        # ensure types
        amount = float(amount)
        is_cancelled = bool(is_cancelled)
        guest = GuestDataAccess(self._db_connection_str if hasattr(self, '_BaseDataAccess__db_connection_str') else None).read_guest_by_id(guest_id)
        return model.Booking(
            booking_id=booking_id,
            check_in_date=check_in,
            check_out_date=check_out,
            total_amount=amount,
            guest=guest,
            is_cancelled=is_cancelled
        )
