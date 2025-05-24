import os

import model
import data_access


class RoomManager:
    def __init__(self):
        self.__room_da = data_access.room_data_access.RoomDataAccess()

    def get_room_details_for_hotel(self, hotel_id: int) -> list[model.Room]:
        all_rooms = self.__room_da.read_all_rooms()
        result = []
        for room in all_rooms:
            if room.hotel_id != hotel_id:
                print(f"❗ Room {room.room_id} übersprungen – kein gültiger RoomType")
                continue

            result.append({
                    "room_type": room.room_type.type_id,
                    "max_guests": room.room_type.max_guests,
                    "Description": room.room_type.description,
                    "price_per_night": room.price_per_night,
                   ##Total Price
                })
            return result
        
    def get_room_details_for_hotel2(self, hotel_id: int) -> list[dict]:

        all_rooms = self.__room_da.read_all_rooms()
        result = []

        for room in all_rooms:
            if room.hotel_id != hotel_id:
                continue

            if room.room_type is None:
                print(f"❗ Room {room.room_id} übersprungen – kein gültiger RoomType")
            continue  # wichtig: verhindert .type_id auf None

        result.append({
            "room_type": room.room_type.type_id,  # oder .type_id, wenn du willst
            "max_guests": room.room_type.max_guests,
            "description": room.room_type.description,
            "price_per_night": room.price_per_night
            })

        return result

        

       