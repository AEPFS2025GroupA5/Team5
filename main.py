from data_access.base_data_access import test_hello

test_hello()


from data_access.facility_data_access import FacilityDataAccess

fac_dao = FacilityDataAccess("C:/Users/Salio/Documents/FH/Github/Supreme/Coding/SQL/DB/hotel_reservation_sample.db")  # z. B. hotel_reservation_sample.db
facilities = fac_dao.read_all_facilities()

for f in facilities:
    print(f"{f.facility_id}: {f.name}")



