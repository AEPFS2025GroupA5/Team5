class Facility:

    facility_list: list["Facility"] = []
    facility_ids = {}

    def __init__(self, facility_id:int, name:str):
        
        self.facility_id = facility_id
        self.name = name.strip()


        if not isinstance (facility_id, int):
            raise TypeError("facility_id has to be a int")
        if not facility_id:
            raise ValueError("facility_id is mandatory")
        
        if not isinstance(name, str):
            raise TypeError("facility name has to be a str")
        if not name:
            raise ValueError("facility name is mandatory")
        
        #Speichert sich selber in der Liste
        Facility.facility_list.append(self)
        Facility.facility_ids[facility_id] = self
        

    def list_all() -> list[str]:
        return "\n".join([f"ID: {f.facility_id} | Name: {f.name}" for f in Facility.facility_list])
    
    def get(fid):
        """Facility nach ID holen (KeyError, falls unbekannt)."""
        return Facility.facility_ids[fid]
        

        