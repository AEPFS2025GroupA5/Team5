from data_access.base_data_access import BaseDataAccess
import data_access
from datetime import date
import model
from model.booking import Booking
from model.room import Room
from model.hotel import Hotel
from data_access import RoomDataAccess
from data_access import GuestDataAccess

class BookingDataAccess(BaseDataAccess):
    def __init__(self, 
                db_path: str = None               
        ):
        super().__init__(db_path)


    def read_all_bookings(self) -> list[model.Booking]:
        sql = """
        SELECT 
            a.address_id, a.street, a.city, a.zip_code,
            b.booking_id, b.room_id, r.room_number, r.type_id, r.price_per_night,
            r.hotel_id, h.name, h.stars, 
            b.check_in_date, b.check_out_date, 
            b.total_amount, b.guest_id, g.first_name, g.last_name, g.email, b.is_cancelled
        FROM booking AS b
        JOIN guest AS g ON b.guest_id = g.guest_id
        JOIN room AS r ON b.room_id = r.room_id
        JOIN hotel AS h ON r.hotel_id = h.hotel_id
        JOIN address AS a ON h.address_id = a.address_id
        """
        rows = self.fetchall(sql)
        all_bookings = []

        for (
            address_id, street, city, zip_code,
            booking_id, room_id, room_number, room_type, price_per_night,
            hotel_id, hotel_name, hotel_stars,
            check_in, check_out, total_amount,
            guest_id, guest_first_name, guest_last_name,guest_email,
            cancelled
        ) in rows:
            #objekte aufbauen
            is_cancelled = bool(cancelled)
            address = model.Address(address_id, street, city, zip_code)
            hotel = model.Hotel(hotel_id, hotel_name, hotel_stars, address)
            room = model.Room(room_id, hotel, room_number, room_type, price_per_night)
            guest = model.Guest(guest_id, guest_first_name, guest_last_name,guest_email, address)
                       
            booking = model.Booking(booking_id=booking_id, room=room, check_in_date=check_in, check_out_date=check_out, total_amount=total_amount, guest=guest, is_cancelled=is_cancelled)
            #erstelltes Objekt in der leeren Liste appenden
            all_bookings.append(booking)

        return all_bookings
        # for bookinge in all_bookings:
        #     booking.print_booking_summary(bookinge)

    def read_booking_by_id(self, booking_id: int) -> model.Booking:
        sql = """
        SELECT 
            b.booking_id, b.check_in_date, b.check_out_date, b.total_amount, b.is_cancelled,
            g.guest_id, g.first_name, g.last_name, g.email,
            ga.address_id, ga.street, ga.city, ga.zip_code,
            r.room_id, r.room_number, r.type_id, r.price_per_night,
            h.hotel_id, h.name, h.stars,
            ha.address_id, ha.street, ha.city, ha.zip_code
        FROM booking b
        JOIN guest g ON b.guest_id = g.guest_id
        JOIN address ga ON g.address_id = ga.address_id
        JOIN room r ON b.room_id = r.room_id
        JOIN hotel h ON r.hotel_id = h.hotel_id
        JOIN address ha ON h.address_id = ha.address_id
        WHERE b.booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        #Prüfen, ob die Buchungs ID existiert
        if not row:
            raise ValueError(f"No booking found with ID {booking_id}")

        (
            booking_id, check_in, check_out, total_amount, is_cancelled,
            guest_id, first_name, last_name, email,
            guest_addr_id, guest_street, guest_city, guest_zip,
            room_id, room_number, room_type_id, price_per_night,
            hotel_id, hotel_name, hotel_stars,
            hotel_addr_id, hotel_street, hotel_city, hotel_zip
        ) = row

        # Objekte aufbauen
        guest_address = model.Address(guest_addr_id, guest_street, guest_city, guest_zip)
        guest = model.Guest(guest_id, first_name, last_name, email, guest_address)

        hotel_address = model.Address(hotel_addr_id, hotel_street, hotel_city, hotel_zip)
        hotel = model.Hotel(hotel_id, hotel_name, hotel_stars, hotel_address)

        room = model.Room(room_id, hotel, room_number, room_type_id, price_per_night)

        #Objekt Booking erstellen
        booking = model.Booking(
            booking_id=booking_id,
            room=room,
            check_in_date=check_in,
            check_out_date=check_out,
            total_amount=total_amount,
            guest=guest,
            is_cancelled=bool(is_cancelled)
        )

        return booking

    def read_av_rooms(self, check_out_date: date, check_in_date: date) -> list[model.Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.type_id, r.price_per_night,
            h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code
        FROM Room r
        JOIN Hotel h ON h.hotel_id = r.hotel_id
        JOIN Address a ON a.address_id = h.address_id
        LEFT JOIN Booking b ON r.room_id = b.room_id
            AND b.check_in_date <= ? AND b.check_out_date >= ?
        AND b.room_id IS NULL
        """
        rows = self.fetchall(sql, (check_out_date, check_in_date))
        if not rows:
            #Wenn man keine Ausgabe erhält, genau weil es keine verfügbaren Zimmer mehr gibt
            raise ValueError(f"There are no rooms available from {check_in_date} to {check_out_date}. Please enter either another city or another check in/check out date")
        all_av_rooms = []

        for (room_id, room_number, type_id, price_per_night,
            hotel_id, name, stars,
            address_id, street, city, zip_code) in rows:

            # Preis dynamisch anpassen:
            room= RoomDataAccess()
            price_season= room.get_price_season(price_per_night)

            #Objekte erstellen, um die verfügbaren Zimmer in der Liste zu appenden
            address = model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
            hotel = model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address=address)
            av_room = model.Room(room_id=room_id, hotel_id=hotel, room_number=room_number, room_type=type_id, price_per_night=price_season)
            all_av_rooms.append(av_room)
        
        return all_av_rooms

    def read_all_av_rooms_by_hotel(self, hotel_id:int, check_out_date:date, check_in_date:date) -> list[model.Room]:
        sql = """
        SELECT r.room_id, r.hotel_id, r.room_number, r.type_id, r.price_per_night
        FROM Room r
        LEFT JOIN Booking b ON r.room_id = b.room_id
        AND b.check_in_date <= ? AND b.check_out_date >= ?
        WHERE r.hotel_id = ?
        AND b.room_id IS NULL
        """
        params = (check_out_date, check_in_date, hotel_id)
        rows = self.fetchall(sql, params)
        
        if not rows:
            #Wenn man keine Ausgabe erhält, genau weil es keine verfügbaren Zimmer mehr gibt
            raise ValueError(f"There are no rooms available from {check_in_date} to {check_out_date}. Please enter either another city or another check in/check out date")
        all_av_rooms = []

        for (room_id, hotel_id, room_number, type_id, price_per_night) in rows:
            # Preis dynamisch anpassen:
            room= RoomDataAccess()
            price_season= room.get_price_season(price_per_night)
            
            #Objekt für verfügbare Zimmer erstellen
            av_room = model.Room(room_id=room_id, hotel_id=hotel_id, room_number=room_number, room_type=type_id, price_per_night=price_season)
            #verfügbare Zimmer in der leeren Liste appenden
            all_av_rooms.append(av_room)
        
        return all_av_rooms

    def read_av_rooms_city(self, city: str, check_out_date: date, check_in_date: date) -> list[model.Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.type_id, r.price_per_night,
            h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code
        FROM Room r
        JOIN Hotel h ON h.hotel_id = r.hotel_id
        JOIN Address a ON a.address_id = h.address_id
        LEFT JOIN Booking b ON r.room_id = b.room_id
            AND b.check_in_date <= ? AND b.check_out_date >= ?
        WHERE a.city LIKE ?
        AND b.room_id IS NULL
        """
        like = f"%{city}%"
        rows = self.fetchall(sql, (check_out_date, check_in_date, like))
        if not rows:
            #Wenn man keine Ausgabe erhält, genau weil es keine verfügbaren Zimmer mehr gibt
            raise ValueError(f"There are no rooms available from {check_in_date} to {check_out_date}. Please enter either another city or another check in/check out date")
        all_av_rooms = []

        for (room_id, room_number, type_id, price_per_night,
            hotel_id, name, stars,
            address_id, street, city, zip_code) in rows:

            # Preis dynamisch anpassen:
            room= RoomDataAccess()
            price_season= room.get_price_season(price_per_night)

            #Objekte erstellen, um die verfügbaren Zimmer in der Liste zu appenden
            address = model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
            hotel = model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address=address)
            av_room = model.Room(room_id=room_id, hotel_id=hotel, room_number=room_number, room_type=type_id, price_per_night=price_season)
            all_av_rooms.append(av_room)
        
        return all_av_rooms

    def create_new_booking(self, room_id:int, check_in_date:date, check_out_date:date, guest_id:int) -> model.Booking:
        if not guest_id:
            raise ValueError("Guest has to be defined")
        if not room_id:
            raise ValueError("Room has to be defined")
        if not isinstance(check_in_date, date):
            raise ValueError("Check in Date has to be a date")
        if not isinstance(check_out_date, date):
            raise ValueError("Check out Date has to be a date")
        if check_out_date <= check_in_date:
            raise ValueError("Check-out date must be after check-in date")

        #Connection with Data Acess Layer
        room_mo = data_access.RoomDataAccess()
        guest_mo = data_access.GuestDataAccess()

        room_dao = room_mo.read_room_by_id(room_id)
        hotel_dao = room_mo.read_hotel_by_roomId(room_id)
        guest_dao = guest_mo.read_guest_by_id(guest_id)

        available_rooms = self.read_all_av_rooms_by_hotel(hotel_dao.hotel_id, check_out_date, check_in_date)
        available_room_ids = [room_id for room in available_rooms]
        if room_id not in available_room_ids:
            raise ValueError("Room is not available in the selected period")

        sql = """
        INSERT INTO booking (guest_id, room_id, check_in_date, check_out_date, total_amount) VALUES (?, ?, ?, ?, ?)             
        """
        # Preis dynamisch anpassen:
        price_season= room_mo.get_price_season(room_dao.price_per_night)

        #Berechnung von MWST und Verwaltungskosten
        num_nights = (check_out_date - check_in_date).days
        price = num_nights * price_season
        
        mwst_satz= 108.1
        verwaltungskosten_satz= 0.1

        verwaltungskosten = price * verwaltungskosten_satz
        base_price = verwaltungskosten + price

        vr_kost= verwaltungskosten/mwst_satz*100

        mwst_betrag= base_price - (base_price/mwst_satz*100)

        total_amount= float(round(base_price, 2))

        sub_total= float(round(total_amount-mwst_betrag, 2))

        #Userfriendly Ausgabe für die erstellte Buchung mit Auszug aller Kosten und MWST Betrag -> Aus simplen Gründen haben wir 8.1% genommen
        print(f"   Thank you for your booking!")
        print(f"   🛏 Base Price ({num_nights:.2f} nights at CHF {price_season:.2f} ): CHF {price:.2f} ")
        print(f"   🛠 Administrative Fee: CHF {vr_kost:.2f} ")
        print(f"-------------------------------------------")
        print(f"   Subtotal: {sub_total:.2f}")
        print(f"   🧾 VAT (8.1%): CHF {mwst_betrag:.2f} ")
        print(f"   💵 Total Amount: CHF {total_amount:.2f} ")

        params = (guest_id, room_id, check_in_date, check_out_date, total_amount)
        last_row_id, _ = self.execute(sql, params)

        return model.Booking(booking_id=last_row_id, room=room_dao, check_in_date=check_in_date, check_out_date=check_out_date, total_amount=total_amount, guest=guest_dao, is_cancelled=False)
        
    def cancell_booking(self, booking_id:int)-> None:
        if not booking_id:
            raise ValueError("Booking ID is required.")
        
        today = date.today()

        booking= self.read_booking_by_id(booking_id)
        #In order to cancell a booking we need to check if the check In Date is in the past
        if booking.check_in_date <= today:
            raise ValueError("This Booking cannot be cancelled.")
        #then we check if the booking has been cancelled before
        if booking.is_cancelled:
            raise ValueError("This Booking has already been cancelled")
        
        else:
            sql = """
            UPDATE booking
            SET is_cancelled = 1
            WHERE booking_id = ?
            """
            self.execute(sql, (booking_id,))
            print(f"❌ Buchung mit ID {booking_id} wurde storniert.")


