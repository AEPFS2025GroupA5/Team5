import data_access
import model

import os
os.environ["DB_FILE"] = os.path.abspath("database/hotel_reservation_sample.db")


## // main ist zum Testen gedacht und Kommentieren

### Verbindungen zur DB
# V1 = data_access.FacilityDataAccess()  
# V2 = data_access.RoomTypeDataAccess()
# V3 = data_access.RoomDataAccess()
V4 = data_access.HotelDataAccess()

hotels = V4.read_all_hotels()
for h in hotels:
    print(f"ID: {h._hotel_id} | Name: {h._name} | Stars: {h._stars} | Address ID: {h.adress_id}")