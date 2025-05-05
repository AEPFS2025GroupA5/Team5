import os
from data_access.roomtype_access import RoomTypeAccess

if __name__ == "__main__":
    # Absoluter Pfad zur Datenbank
    db_path = os.path.join(os.path.dirname(__file__), "hotel_reservation_sample.db")
    roomtype_access = RoomTypeAccess(db_path)

    print("Verfügbare Zimmertypen:\n")
    roomtypes = roomtype_access.get_all()
    for rt in roomtypes:
        print(f"ID: {rt[0]}, Beschreibung: {rt[1]}, Max Gäste: {rt[2]}")