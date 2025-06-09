import model
import ui
import business_logic
import ui.input_helper

def print_hotel(hotel: model.Hotel) -> None:
    if not isinstance(hotel, model.Hotel):
        raise TypeError("hotel must be a Hotel object")
    print(hotel.name, hotel.stars, hotel.address.city)

def print_hotel_with_address(hotel: model.Hotel) -> None:
    if not isinstance(hotel, model.Hotel):
        raise TypeError("hotel must be a Hotel object")
    print_hotel(hotel)
    print(hotel.address.show_user_friendly())

def get_city_input() -> str:
    while True:
        try:
            return ui.input_helper.input_valid_string("Enter the city you want to search for hotels: ", 3, 10)
        except ui.input_helper.StringLengthError:
            print(f"Invalid input, give at least 3 characters and at most 10 characters.")

def get_stars_input() -> int:
    while True:
        try:
            return ui.input_helper.input_valid_int("Enter the minimum number of stars (1-5): ", 1, 5)
        except ui.input_helper.OutOfRangeError as e:
            print(f"Invalid input: {e}. Please enter a number between 1 and 5.")
        except ui.input_helper.EmptyInputError:
            print("Input cannot be empty. Please enter a valid number.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid integer.")

def get_max_guests_input() -> int:
    while True:
        try:
            return ui.input_helper.input_valid_int("Enter the maximum number of guests: ", 1, 50)
        except ui.input_helper.OutOfRangeError as e:
            print(f"Invalid input: {e}. Please enter a number between 1 and 50.")
        except ui.input_helper.EmptyInputError:
            print("Input cannot be empty. Please enter a valid number.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid integer.")

def get_user_frendly_hotel_info_short(hotel: model.Hotel) -> str:
    return f"Name: {hotel.name}, City: {hotel.address.city}, Stars: {hotel.stars}"

def get_city_no_limit() -> str:
    while True:
        try:
            return ui.input_helper.input_valid_string("Enter the city you want to search for hotels: ", 0, 10)
        except ui.input_helper.StringLengthError:
            print(f"Invalid input, give at most 15 characters.")

def get_address_short(address: model.Address) -> str:
    return f"{address.street}, {address.city}, {address.zip_code}"

def get_room_type_short(room_type: model.RoomType) -> str:
    return f"{room_type.description} (Max Guests: {room_type.max_guests})"

def get_all_facilities_short(facility: model.Facility) -> str:
    if not facility:
        return "No facilities available."
    return f"{facility.name}"

def get_room_info_short(room: model.Room) -> str:
    if not isinstance(room, model.Room):
        raise TypeError("room must be a Room object")
    return f"Room Number: {room.room_number}, Type: {get_room_type_short(room.room_type)}, Price: {room.price_per_night} "
