import data_access
import model
from model.facility import Facility
from model.room_type import RoomType
from model.room import Room

import os
os.environ["DB_FILE"] = os.path.abspath("database/hotel_reservation_sample.db")


## // main ist zum Testen gedacht und Kommentieren

### Verbindungen zur DB
# V1 = data_access.FacilityDataAccess()  
# V2 = data_access.RoomTypeDataAccess()
V3 = data_access.RoomDataAccess()
# V4 = data_access.HotelDataAccess()
# V5 = data_access.GuestDataAccess()
V6 = data_access.InvoiceDataAccess()

# # # ##Test

test = V3.read_all_rooms()
print(test)

inv = V6.read_all_invoice()
for i in inv:
    print(i)