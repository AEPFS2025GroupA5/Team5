from data_access.base_data_access import BaseDataAccess
import data_access
from datetime import date
import model
from model.booking import Booking
from model.room import Room

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

    def read_all_av_rooms(self, hotel_id:int, check_out_date:date, check_in_date:date) -> list[model.room]:
        sql = """
        SELECT r.room_id, r.hotel_id, r.room_number, r.type_id, r.price_per_night
        FROM Room r
        LEFT JOIN Booking b ON r.room_id = b.room_id
        AND b.check_in_date <= ? AND b.check_out_date >= ?
        WHERE r.hotel_id = ?
        AND b.room_id IS NULL
        """
        params = (check_out_date, check_in_date, hotel_id)
        rows = self.fetchall(sql, params)
        all_av_rooms= []

        for (room_id, hotel_id, room_number, type_id, price_per_night) in rows:
            av_room = model.Room(room_id=room_id, hotel_id=hotel_id, room_number=room_number, room_type=type_id, price_per_night=price_per_night)
            all_av_rooms.append(av_room)
        
        return all_av_rooms

    # def create_new_booking(self, room:model.Room, check_in_date:date, check_out_date:date, total_amount:int, guest:model.Guest) -> model.Booking:
    #     if not guest:
    #         raise ValueError("Guest has to be defined")
    #     if not room:
    #         raise ValueError("Room has to be defined")
    #     if not isinstance(total_amount, (int, float)):
    #         raise TypeError("total amount must be an integer or float")
    #     if total_amount < 0:
    #         raise ValueError("total amount has to be positiv")
    #     if not isinstance(check_in_date, date):
    #         raise ValueError("Check in Date has to be a date")
    #     if not isinstance(check_out_date, date):
    #         raise ValueError("Check out Date has to be a date")
    #     if check_out_date <= check_in_date:
    #         raise ValueError("Check-out date must be after check-in date")
        
    #     available_rooms = self.read_all_av_rooms(room.hotel_id, check_out_date, check_in_date)
    #     available_room_ids = [r.room_id for r in available_rooms]
    #     if room.room_id not in available_room_ids:
    #         raise ValueError("Room is not available in the selected period")

    #     sql = """
    #     INSERT INTO booking (guest_id, room_id, check_in_date, check_out_date, total_amount) VALUES (?, ?, ?, ?, ?)             
    #     """
    #     params = (guest.guest_id, room.room_id, check_in_date, check_out_date, total_amount)
    #     last_row_id, _ = self.execute(sql, params)

    #     guest_mo = data_access.GuestDataAccess.read_guest_by_id(guest)
    #     room_mo = data_access.RoomDataAccess.read_room_by_id(room)


    #     return model.Booking(booking_id=last_row_id, room=room_mo, check_in_date=check_in_date, check_out_date=check_out_date, total_amount=total_amount, guest=guest_mo, is_cancelled=False)
    

