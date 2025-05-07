from data_access.base_data_access import BaseDataAccess
from model.facility import Facility

class FacilityDataAccess(BaseDataAccess):
    def read_all_facilities(self) -> list[Facility]:
        sql = """
        SELECT facility_id, facility_name FROM facilities
        """
        rows = self.fetchall(sql)
        return [
            Facility(facility_id, name)
            for facility_id, name in rows
        ]