import model

def print_hotel(hotel: model.Hotel) -> None:
    if not isinstance(hotel, model.Hotel):
        raise TypeError("hotel must be a Hotel object")
    print(hotel.name, hotel.stars)

def print_hotel_with_address(hotel: model.Hotel) -> None:
    if not isinstance(hotel, model.Hotel):
        raise TypeError("hotel must be a Hotel object")
    print_hotel(hotel)
    print(hotel.address.show_user_friendly())