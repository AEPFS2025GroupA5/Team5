import model
import ui
import business_logic
import ui.input_helper
from datetime import date


def get_booking_id_input() -> int:
    while True:
        try:
            return ui.input_helper.input_valid_int("Enter Booking ID: ", 1, 9999)
        except Exception as e:
            print(f"Invalid input: {e}")

# def get_guest_id_input() -> int:
#     while True:
#         try:
#             return ui.input_helper.input_valid_int("Enter Guest ID: ", 1, 9999)
#         except Exception as e:
#             print(f"Invalid input: {e}")

# def get_total_amount_input() -> float:
#     while True:
#         try:
#             return float(ui.input_helper.input_valid_int("Enter total amount (CHF): ", 1, 100000))
#         except Exception as e:
#             print(f"Invalid input: {e}")

def get_checkin_date_input() -> date:
    while True:
        try:
            return ui.input_helper.input_valid_date("Enter check-in date (YYYY-MM-DD): ")
        except Exception as e:
            print(f"Invalid input: {e}")

def get_checkout_date_input() -> date:
    while True:
        try:
            return ui.input_helper.input_valid_date("Enter check-out date (YYYY-MM-DD): ")
        except Exception as e:
            print(f"Invalid input: {e}")

def get_userfriendly_room(room: model.Room) -> str:
    roomman= business_logic.RoomManager()
    hotelman= business_logic.HotelManager()

    r = roomman.get_room_by_id(room.room_id)
    h = hotelman.read_hotel_by_id(r.hotel_id)
    return f"Hotel: {h.name},{h.stars}, {h.address.city}, Room number: {r.room_number}, Room description: {r.room_type.description}, Max Guests: {r.room_type.max_guests}, Price per night: CHF {r.price_per_night}"

