from data_access.base_data_access import BaseDataAccess
import model

class FacilityDataAccess(BaseDataAccess):
    def __init__(self, 
                 db_path: str = None
        ):
        super().__init__(db_path)

    def read_all_facilities(self) -> list[model.Facility]:
        sql = """
        SELECT facility_id, facility_name FROM facilities
        """
        facilities = self.fetchall(sql)
        return [model.Facility(facility_id, name) for facility_id, name in facilities]
    
    def read_facility_by_id(self, 
                            facility_id: int
        ) -> model.Facility:
     if facility_id is None:
        raise ValueError("facility_id is required")

     sql = "SELECT facility_id, facility_name FROM facilities WHERE facility_id = ?"
     params = (facility_id,)
     result = self.fetchone(sql, params)

     if result:
        return model.Facility(facility_id=result[0], name=result[1])
     return None
    
    def read_facility_by_name(self,
                                name: str
        ) -> model.Facility:
     if not name:
        raise ValueError("Facility name is required")

     sql = "SELECT facility_id, facility_name FROM facilities WHERE facility_name = ?"
     params = (name,)
     result = self.fetchone(sql, params)

     if result:
        return model.Facility(facility_id=result[0], name=result[1])
     return None

    def create_new_facility(self, 
                            name: str
        ) -> model.Facility:
     if not isinstance(name, str):
            raise TypeError("facility name has to be a str")
     if not name:
            raise ValueError("facility name is mandatory")
    
     sql = "INSERT INTO facilities (facility_name) VALUES (?)"
     params = tuple([name])
     last_row_id, _ = self.execute(sql, params)
     return model.Facility(facility_id=last_row_id, name=name)
    
    def delete_facility_by_id(self, 
                              facility_id: int
        ) -> None:
     sql = "DELETE FROM facilities WHERE facility_id = ?"
     self.execute(sql, (facility_id,))


    
    def update_facility(self, 
                        facility: model.Facility
        ) -> None:
     sql = "UPDATE facilities SET facility_name = ? WHERE facility_id = ?"
     params = tuple([facility.name, facility.facility_id])
     last_row_id, row_count = self.execute(sql, params)

