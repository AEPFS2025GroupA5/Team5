from data_access import BaseDataAccess
import os

data_access = BaseDataAccess(r"C:\Users\Salio\Documents\FH\Github\Supreme\Coding\SQL\DB\hotel_reservation_sample.db")
result = data_access.fetchall("SELECT * FROM Hotel")
print(result)