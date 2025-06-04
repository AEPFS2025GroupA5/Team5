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