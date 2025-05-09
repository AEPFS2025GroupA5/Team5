import data_access
import model
from model.guest import Guest
from data_access.guest_data_access import GuestDataAccess

import os
os.environ["DB_FILE"] = os.path.abspath("database/hotel_reservation_sample.db")


### /// Test

##Facility
# Verbindung = data_access.FacilityDataAccess()  
# V2 = data_access.RoomTypeDataAccess()

## /// RoomType

## Read all
# rooms = V2.read_all_room_types()
# for r in rooms:
#     print(f"ID: {r.type_id} max guests: {r.max_guests} description: {r.description}")

## Read by id
# byid = V2.read_room_type_by_id(5)
# if byid:
#     print(f"Gefunden wurde ID: {byid.type_id} max: {byid.max_guests} description: {byid.description}")
# else:
#     print(f"Nüt")

## Create new
# new_type = V2.create_new_room_type("Groß", 10)
# rooms = V2.read_all_room_types()
# for r in rooms:
#     print(f"ID: {r.type_id} max guests: {r.max_guests} description: {r.description}")

## Update Roomtype
# update = V2.read_room_type_by_id(6)
# update.description = "Doch nicht groß"
# update.max_guests = 8
# V2.update_room_type(update)
# rooms = V2.read_all_room_types()
# for r in rooms:
#     print(f"ID: {r.type_id} max guests: {r.max_guests} description: {r.description}")

## Delete Roomtyp

# delete = V2.read_room_type_by_id(5)
# V2.delete_room_type_by_id(delete)
# rooms = V2.read_all_room_types()
# for r in rooms:
#     print(f"ID: {r.type_id} | max guests: {r.max_guests} | description: {r.description}")
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
#     print(f"{f.facility_id}: {f.name}")

#====================================================================
## Guest Verbindung
# VG = GuestDataAccess()

# # Read all guests
# guests = VG.read_all_guest()
# for guest in guests:
#     print(f"Guest Id: {guest.guest_id} First Name: {guest.first_name} Last Name: {guest.last_name} email: {guest.email} address id: {guest.address_id}")

# # Read guest by id
# guests = VG.read_guest_by_id(2)
# print(guests)

# #Read guest by lastname
# guests = VG.read_guest_by_name("Müller")
# for guest in guests:
#     print(f"Guest Id: {guest.guest_id} First Name: {guest.first_name} Last Name: {guest.last_name} email: {guest.email} address id: {guest.address_id}")

# #Create new guest
# new_guest=VG.create_new_guest("Arthur", "Evlanov", "ev.arth@gmail.com", 1)
# guests= VG.read_all_guest()
# for guest in guests:
#     print(f"Guest Id: {guest.guest_id} First Name: {guest.first_name} Last Name: {guest.last_name} email: {guest.email} address id: {guest.address_id}")

# # Update guest
# update_guest= VG.update_guest_by_last_name(6, "Evlanovo")
# guests= VG.read_all_guest()
# for guest in guests:
#     print(f"Guest Id: {guest.guest_id} First Name: {guest.first_name} Last Name: {guest.last_name} email: {guest.email} address id: {guest.address_id}")

# #Delete guest by id
# delete_guest = VG.delete_guest_by_id(6)
# guests= VG.read_all_guest()
# for guest in guests:
#     print(f"Guest Id: {guest.guest_id} First Name: {guest.first_name} Last Name: {guest.last_name} email: {guest.email} address id: {guest.address_id}")
