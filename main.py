import data_access
import model
from model.guest import Guest

import os
os.environ["DB_FILE"] = os.path.abspath("database/hotel_reservation_sample.db")


### /// Test

##Facility
# Verbindung = data_access.FacilityDataAccess()  
# V2 = data_access.RoomTypeDataAccess()

## /// RoomType

# rooms = V2.read_all_room_types()
# for r in rooms:
#     print(f"ID: {r.type_id} max guests: {r.max_guests} description: {r.description}")

# byid = V2.read_room_type_by_id(5)
# if byid:
#     print(f"Gefunden wurde ID: {byid.type_id} max: {byid.max_guests} description: {byid.description}")
# else:
#     print(f"Nüt")

###Read all
# facilities = Verbindung.read_all_facilities()
# for f in facilities:
#     print(f"{f.facility_id}: {f.name}")

###Read by ID
# fac = Verbindung.read_facility_by_id(6)
# if fac:
#     print(f"Gefundene Facility: ID: {fac.facility_id} - Name: {fac.name}")
# else:
#     print("Keine Facility mit dieser ID gefunden.")

###Read by name
# t2 = Verbindung.read_facility_by_name("Saliou")
# if t2:
#     print(f" Gefunden: {t2.name} mit der ID: {t2.facility_id}")
           
# else:
#     print("Keine Facility mit diesem Namen gefunden")

### Create new
# 'Beispiel_1 = Verbindung.create_new_facility("Beispiel 3")
# facilities = Verbindung.read_all_facilities()
# for f in facilities:
#      print(f"{f.facility_id}: {f.name}")'

### Delete by ID
# Verbindung.delete_facility_by_id(7)
# print("Gelöscht.")


###Update
# fac = Verbindung.read_facility_by_id(8)
# fac.name = "BEISPIEL"
# Verbindung.update_facility(fac)

# facilities = Verbindung.read_all_facilities()
# for f in facilities:
#     print(f"{f.facility_id}: {f.name}")

#====================================================================
## Guest
VG = data_access.guest_data_access
guests = VG.read_all_guest()
