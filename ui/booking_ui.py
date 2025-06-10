import model
import ui
import business_logic
import ui.input_helper
from datetime import date

#Connection to Business Layer
bookingman= business_logic.BookingManager()
hotelman= business_logic.HotelManager()
roomman= business_logic.RoomManager()


#Input from User Functions
def get_booking_id_input() -> int:
    while True:
        try:
            return ui.input_helper.input_valid_int("Enter Booking ID: ", 1, 9999)
        except Exception as e:
            print(f"Invalid input: {e}")

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

def get_guest_firstname() -> str:
    while True:
        try:
            return ui.input_helper.input_valid_string("Enter your firstname", 3, 15)
        except Exception as e:
            print(f"Invalid input: {e}, give at most 15 characters")

def get_guest_lastname() -> str:
    while True:
        try:
            return ui.input_helper.input_valid_string("Enter your lastname", 3, 20)
        except Exception as e:
            print(f"Invalid input: {e}, give at most 20 characters")


#Userfriendly Output
def get_userfriendly_room(room: model.Room) -> str:
    r = roomman.get_room_by_id(room.room_id)
    h = hotelman.read_hotel_by_id(r.hotel.hotel_id)
    return f"Hotel: {h.name},{h.stars}, {h.address.city}, Room number: {r.room_number}, Room description: {r.room_type.description}, Max Guests: {r.room_type.max_guests}, Price per night: CHF {r.price_per_night}"

def get_userfriendly_price(room: model.Room) -> str:
    r = roomman.get_room_by_id(room.room_id)
    h = hotelman.read_hotel_by_id(r.hotel.hotel_id)
    return f"Hotel: {h.name}, {h.stars} stars, City: {h.address.city}, Room number: {r.room_number}, Room description: {r.room_type.description}, Max Guests: {r.room_type.max_guests}"


def get_userfriendly_booking(booking:model.Booking)-> str:

    r= roomman.get_room_by_id(booking.room.room_id)
    h= hotelman.read_hotel_by_id(r.hotel.hotel_id)
    b= bookingman.read_booking_by_id(booking.booking_id)

    return f"Booking ID: {b.booking_id}, Check- In: {b.check_in_date}, Check-Out: {b.check_out_date}, Total Amount: {b.total_amount}, Cancelled: {b.is_cancelled}, Booked in: {h.name} Room: {r.room_number}, Invoice: {b.invoice.booking_id if b.invoice else 'No Invoice'}"

def get_userfriendly_invoice(i:model.Invoice)-> str:
    return f"Invoice ID: {i.invoice_id}, Issue Date: {i.issue_date}, Amount to pay:{i.total_amount}"

def get_userfriendly_guest(guest:model.Guest) -> str:
    return f"Your name: {guest.first_name} {guest.last_name}, Address: {guest.address.street}, {guest.address.city}, {guest.address.zip_code}, E-Mail: {guest.email}"
