from model.facility import Facility

class RoomType:
    def __init__(
        self,
        type_id: int,
        name: str,
        max_guests: int,
        amenities: list = None,
        description: str = None,
        facility_ids:Facility = None

    ):
         self.type_id = type_id
         self.name = name
         self.max_guests = max_guests
         self.amenities = amenities
         self.description = description


#Prüfungen // Type_id müssen wir klären wie das vergeben wird.
         if not isinstance(type_id, int):
               raise TypeError("type_id must be a int")
         if not type_id:
               raise ValueError("type_id must be assigned")
         
         if not isinstance(name, str): 
               raise TypeError("name must be a string")
         if not name:
               raise ValueError("name must be assigned")
         
         if not isinstance(max_guests, int):
               raise TypeError("max_guests must be an int")
         if max_guests <= 0:
               raise ValueError("max_guests must be greater than 0")     
            

         #if not isinstance(description, str):
               #raise TypeError("description must be a string")
        

        # // Facility Verknüpfung //None → leere Liste 
         facility_ids = facility_ids or []
         if not all(isinstance(fid, int) for fid in facility_ids):
            raise TypeError("facility_ids must be ints") 
         
         self.facilities = []
         missing = []
         for fid in facility_ids:
            try:
                self.facilities.append(Facility.get(fid))
            except KeyError:               # ID nicht bekannt
                missing.append(fid)

         if missing:
            raise ValueError(f"Unknown Facility IDs: {missing}")


#Funktionen // get für User story 2-2.1 // update info User Story 10
    def get_details(self):
            return f"Name: {self.name}\n" \
                   f"Max Guests: {self.max_guests}\n" \
                   f"Facilities: {', '.join(facility.name for facility in self.facilities)}\n" \
                   f"Description: {self.description}\n"
    
    def update_info(
        self,
        name: str = None,
        max_guests: int = None,
        description: str = None,
        amenities: list = None,
    ):
        if name is not None:
            if not isinstance(name, str):
                raise TypeError("name must be a string")
            if not name.strip():
                raise ValueError("name cannot be empty")
            self.name = name

        if max_guests is not None:
            if not isinstance(max_guests, int):
                raise TypeError("max_guests must be an integer")
            if max_guests < 1:
                raise ValueError("max_guests must be at least 1")
            self.max_guests = max_guests

        if description is not None:
            if not isinstance(description, str):
                raise TypeError("description must be a string")
            if not description.strip():
                raise ValueError("description cannot be empty")
            self.description = description