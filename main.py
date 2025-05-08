from data_access.facility_data_access import FacilityDataAccess
from data_access.room_type_access import RoomTypeDataAccess
from model.facility import Facility

Verbindung = FacilityDataAccess("database\hotel_reservation_sample.db")  # z. B. hotel_reservation_sample.db

rows = Verbindung.read_all_facilities()
facilities = [Facility(id=row[0], name=row[1]) for row in rows]

print(facilities)



# for f in facilities:
#     print(f"{f.facility_id}: {f.name}")




# new = RoomTypeDataAccess("database\hotel_reservation_sample.db")
# roomtype = new.read_all_room_types()

# for r in roomtype:
#     print(f"ID = {r.type_id}: DESCRIPTION = {r.description}: MAX GUESTS={r.max_guests}")

