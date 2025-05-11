import data_access
import model
from model.facility import Facility
from model.room_type import RoomType

import os
os.environ["DB_FILE"] = os.path.abspath("database/hotel_reservation_sample.db")


## // main ist zum Testen gedacht und Kommentieren

### Verbindungen zur DB
V1 = data_access.FacilityDataAccess()  
V2 = data_access.RoomTypeDataAccess()
# # V3 = data_access.RoomDataAccess()
# # V4 = data_access.HotelDataAccess()

# ##Test

f1 = Facility(100, "WLAN")
f2 = Facility(200, "Klimaanlage")
f3 = Facility(3300, "Fernseher")

fac = V1.read_all_facilities()


# Hole z. B. die IDs von "WLAN" und "Klimaanlage""
ids = [f.facility_id for f in fac if f.name in ["WLAN", "Klimaanlage"]]


room = RoomType(
    type_id=7,
    description="Minir Bar, TV TESTSSTSS",
    max_guests=2,
    facility_ids=[100,200]
)
print(room)
#print(Facility._facility_list)

V2.update_room_type(room)
roomtypes= V2.read_all_room_types()
print(roomtypes)

