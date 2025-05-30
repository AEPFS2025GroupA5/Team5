from data_access.base_data_access import BaseDataAccess
import model
import data_access.room_type_access
import model.facility 


class RoomFacilityDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def add_facility_to_room(self, room_id: int, facility_id: int):
        sql = "INSERT INTO Room_Facilities (room_id, facility_id) VALUES (?, ?)"
        self.execute(sql, (room_id, facility_id))

    def get_facilities_for_room(self, room_id: int) -> list[model.Facility]:
        sql = """
        SELECT f.facility_id, f.facility_name 
        FROM facilities f
        JOIN Room_Facilities rf ON f.facility_id = rf.facility_id
        WHERE rf.room_id = ?
        """
        result = self.fetchall(sql, (room_id,))
        return [model.Facility(facility_id, name) for facility_id, name in result]
    