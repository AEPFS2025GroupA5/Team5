from data_access.base_data_access import BaseDataAccess
from datetime import datetime
import model

class BookingDataAccess(BaseDataAccess):
    def __init__(self, 
                db_path: str = None               
        ):
        super().__init__(db_path)

        
    def read_all_bookings(self) -> list[model.Booking]:
        sql = """
        SELECT booking_id, room_id, check_in_date, check_out_date, total_amount, guest_id, is_cancelled FROM booking
        """
        rows = self.fetchall(sql)
        all_bookings = []

        for booking_id, room_id, check_in, check_out, total_amount, guest_id, cancelled in rows:
            is_cancelled = bool(cancelled)
            booking= model.Booking(booking_id, room_id, check_in, check_out, total_amount, guest_id, is_cancelled)
            all_bookings.append(booking)

        return all_bookings
    
    

