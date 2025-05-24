from data_access.base_data_access import BaseDataAccess
from datetime import datetime
import model

class BookingDataAccess(BaseDataAccess):
    def __init__(self, 
                db_path: str = None               
        ):
        super().__init__(db_path)

        
    def read_all_bookings(self) -> list[model.Booking]:
        sql = """
        SELECT 
            a.address_id, a.street, a.city, a.zip_code,
            b.booking_id, b.room_id, r.room_number, r.type_id, r.price_per_night,
            r.hotel_id, h.name, h.stars, 
            b.check_in_date, b.check_out_date, 
            b.total_amount, b.guest_id, g.first_name, g.last_name, g.email, b.is_cancelled
        FROM booking AS b
        JOIN guest AS g ON b.guest_id = g.guest_id
        JOIN room AS r ON b.room_id = r.room_id
        JOIN hotel AS h ON r.hotel_id = h.hotel_id
        JOIN address AS a ON h.address_id = a.address_id
        """
        rows = self.fetchall(sql)
        all_bookings = []

        for (
            address_id, street, city, zip_code,
            booking_id, room_id, room_number, room_type, price_per_night,
            hotel_id, hotel_name, hotel_stars,
            check_in, check_out, total_amount,
            guest_id, guest_first_name, guest_last_name,guest_email,
            cancelled
        ) in rows:
            is_cancelled = bool(cancelled)
            address = model.Address(address_id, street, city, zip_code)
            hotel = model.Hotel(hotel_id, hotel_name, hotel_stars, address)
            room = model.Room(room_id, hotel, room_number, room_type, price_per_night)
            guest = model.Guest(guest_id, guest_first_name, guest_last_name,guest_email, address)
                       
            booking = model.Booking(booking_id=booking_id, room=room, check_in_date=check_in, check_out_date=check_out, total_amount=total_amount, guest=guest, is_cancelled=is_cancelled)
        
            all_bookings.append(booking)

        return all_bookings
        # for bookinge in all_bookings:
        #     booking.print_booking_summary(bookinge)
    

    

