# main.py
import os
from data_access.hotel_data_access import HotelDataAccess

os.environ["DB_FILE"] = "database/hotel_reservation_sample.db"
hotels = HotelDataAccess().read_all_hotels()
for h in hotels:
    print(h)
