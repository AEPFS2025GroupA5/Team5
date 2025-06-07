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


    # def read_all_bookings(self) -> list[model.Booking]:
    #     sql = """
    #     SELECT 
    #         a.address_id, a.street, a.city, a.zip_code,
    #         b.booking_id, b.room_id, r.room_number, r.type_id, r.price_per_night,
    #         r.hotel_id, h.name, h.stars, 
    #         b.check_in_date, b.check_out_date, 
    #         b.total_amount, b.guest_id, g.first_name, g.last_name, g.email, b.is_cancelled
    #     FROM booking AS b
    #     JOIN guest AS g ON b.guest_id = g.guest_id
    #     JOIN room AS r ON b.room_id = r.room_id
    #     JOIN hotel AS h ON r.hotel_id = h.hotel_id
    #     JOIN address AS a ON h.address_id = a.address_id
    #     """
    #     rows = self.fetchall(sql)
    #     all_bookings = []
    #     if rows:
    #         for (
    #             address_id, street, city, zip_code,
    #             booking_id, room_id, room_number, room_type, price_per_night,
    #             hotel_id, hotel_name, hotel_stars,
    #             check_in, check_out, total_amount,
    #             guest_id, guest_first_name, guest_last_name,guest_email,
    #             cancelled
    #         ) in rows:
    #             #objekte aufbauen
    #             is_cancelled = bool(cancelled)
    #             address = model.Address(address_id, street, city, zip_code)
    #             hotel = model.Hotel(hotel_id, hotel_name, hotel_stars, address)
    #             room = model.Room(room_id, hotel, room_number, room_type, price_per_night)
    #             guest = model.Guest(guest_id, guest_first_name, guest_last_name,guest_email, address)
                        
    #             booking = model.Booking(booking_id=booking_id, room=room, check_in_date=check_in, check_out_date=check_out, total_amount=total_amount, guest=guest, is_cancelled=is_cancelled)
    #             #erstelltes Objekt in der leeren Liste appenden
    #             all_bookings.append(booking)

    #         return all_bookings
    #     return None

    def read_all_bookings(self) -> list[model.Booking]:
        sql = """
        SELECT 
            a.address_id, a.street, a.city, a.zip_code,
            b.booking_id, b.room_id, r.room_number, r.type_id, r.price_per_night,
            r.hotel_id, h.name, h.stars, 
            b.check_in_date, b.check_out_date, 
            b.total_amount, b.guest_id, g.first_name, g.last_name, g.email, b.is_cancelled,
            i.invoice_id, i.issue_date, i.total_amount as invoice_amount
        FROM booking AS b
        JOIN guest AS g ON b.guest_id = g.guest_id
        JOIN room AS r ON b.room_id = r.room_id
        JOIN hotel AS h ON r.hotel_id = h.hotel_id
        JOIN address AS a ON h.address_id = a.address_id
        LEFT JOIN invoice AS i ON b.booking_id = i.booking_id
        """
        rows = self.fetchall(sql)
        all_bookings = []
        if rows:
            for (
                address_id, street, city, zip_code,
                booking_id, room_id, room_number, room_type, price_per_night,
                hotel_id, hotel_name, hotel_stars,
                check_in, check_out, total_amount,
                guest_id, guest_first_name, guest_last_name, guest_email,
                cancelled,
                invoice_id, issue_date, invoice_amount
            ) in rows:
                # Objekte aufbauen
                is_cancelled = bool(cancelled)
                address = model.Address(address_id, street, city, zip_code)
                hotel = model.Hotel(hotel_id, hotel_name, hotel_stars, address)
                room = model.Room(room_id, hotel, room_number, room_type, price_per_night)
                guest = model.Guest(guest_id, guest_first_name, guest_last_name, guest_email, address)
                
                booking = model.Booking(
                    booking_id=booking_id, 
                    room=room, 
                    check_in_date=check_in, 
                    check_out_date=check_out, 
                    total_amount=total_amount, 
                    guest=guest, 
                    is_cancelled=is_cancelled
                )
                
                # Invoice zuweisen, falls vorhanden
                if invoice_id:
                    invoice = model.Invoice(
                        invoice_id=invoice_id,
                        booking_id=booking_id,
                        issue_date=issue_date,
                        total_amount=invoice_amount,
                    )
                    booking.invoice = invoice
                
                all_bookings.append(booking)

            return all_bookings
        return None


    def read_bookings_by_guest(self, guest_id: int) -> model.Booking:
        if not guest_id:
            raise ValueError("Booking Id is required")
        if not isinstance(guest_id, int):
            raise ValueError("Booking Id must be an integer")
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
        WHERE g.guest_id = ?
        """
        rows = self.fetchall(sql, (guest_id,))
        bookings= []
        if rows:
            for (
                booking_id, check_in, check_out, total_amount, is_cancelled,
                guest_id, first_name, last_name, email,
                guest_addr_id, guest_street, guest_city, guest_zip,
                room_id, room_number, room_type_id, price_per_night,
                hotel_id, hotel_name, hotel_stars,
                hotel_addr_id, hotel_street, hotel_city, hotel_zip
            ) in rows:

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
                bookings.append(booking)

            return bookings
        return None

    # def read_booking_by_id(self, booking_id: int) -> model.Booking:
    #     if not booking_id:
    #         raise ValueError("Booking Id is required")
    #     if not isinstance(booking_id, int):
    #         raise ValueError("Booking Id must be an integer")
    #     sql = """
    #     SELECT 
    #         b.booking_id, b.check_in_date, b.check_out_date, b.total_amount, b.is_cancelled,
    #         g.guest_id, g.first_name, g.last_name, g.email,
    #         ga.address_id, ga.street, ga.city, ga.zip_code,
    #         r.room_id, r.room_number, r.type_id, r.price_per_night,
    #         h.hotel_id, h.name, h.stars,
    #         ha.address_id, ha.street, ha.city, ha.zip_code
    #     FROM booking b
    #     JOIN guest g ON b.guest_id = g.guest_id
    #     JOIN address ga ON g.address_id = ga.address_id
    #     JOIN room r ON b.room_id = r.room_id
    #     JOIN hotel h ON r.hotel_id = h.hotel_id
    #     JOIN address ha ON h.address_id = ha.address_id
    #     WHERE b.booking_id = ?
    #     """
    #     row = self.fetchone(sql, (booking_id,))
    #     if row:

    #         (
    #             booking_id, check_in, check_out, total_amount, is_cancelled,
    #             guest_id, first_name, last_name, email,
    #             guest_addr_id, guest_street, guest_city, guest_zip,
    #             room_id, room_number, room_type_id, price_per_night,
    #             hotel_id, hotel_name, hotel_stars,
    #             hotel_addr_id, hotel_street, hotel_city, hotel_zip
    #         ) = row

    #         # Objekte aufbauen
    #         guest_address = model.Address(guest_addr_id, guest_street, guest_city, guest_zip)
    #         guest = model.Guest(guest_id, first_name, last_name, email, guest_address)

    #         hotel_address = model.Address(hotel_addr_id, hotel_street, hotel_city, hotel_zip)
    #         hotel = model.Hotel(hotel_id, hotel_name, hotel_stars, hotel_address)

    #         room = model.Room(room_id, hotel, room_number, room_type_id, price_per_night)

    #         #Objekt Booking erstellen
    #         booking = model.Booking(
    #             booking_id=booking_id,
    #             room=room,
    #             check_in_date=check_in,
    #             check_out_date=check_out,
    #             total_amount=total_amount,
    #             guest=guest,
    #             is_cancelled=bool(is_cancelled)
    #         )
    #         return booking
        
    #     return None

    def read_booking_by_id(self, booking_id: int) -> model.Booking:
        if not booking_id:
            raise ValueError("Booking Id is required")
        if not isinstance(booking_id, int):
            raise ValueError("Booking Id must be an integer")
        
        sql = """
        SELECT 
            b.booking_id, b.check_in_date, b.check_out_date, b.total_amount, b.is_cancelled,
            g.guest_id, g.first_name, g.last_name, g.email,
            ga.address_id, ga.street, ga.city, ga.zip_code,
            r.room_id, r.room_number, r.type_id, r.price_per_night,
            h.hotel_id, h.name, h.stars,
            ha.address_id, ha.street, ha.city, ha.zip_code,
            i.invoice_id, i.issue_date, i.total_amount as invoice_amount
        FROM booking b
        JOIN guest g ON b.guest_id = g.guest_id
        JOIN address ga ON g.address_id = ga.address_id
        JOIN room r ON b.room_id = r.room_id
        JOIN hotel h ON r.hotel_id = h.hotel_id
        JOIN address ha ON h.address_id = ha.address_id
        LEFT JOIN invoice i ON b.booking_id = i.booking_id
        WHERE b.booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        if row:
            (
                booking_id, check_in, check_out, total_amount, is_cancelled,
                guest_id, first_name, last_name, email,
                guest_addr_id, guest_street, guest_city, guest_zip,
                room_id, room_number, room_type_id, price_per_night,
                hotel_id, hotel_name, hotel_stars,
                hotel_addr_id, hotel_street, hotel_city, hotel_zip,
                invoice_id, issue_date, invoice_amount
            ) = row

            # Objekte aufbauen
            guest_address = model.Address(guest_addr_id, guest_street, guest_city, guest_zip)
            guest = model.Guest(guest_id, first_name, last_name, email, guest_address)

            hotel_address = model.Address(hotel_addr_id, hotel_street, hotel_city, hotel_zip)
            hotel = model.Hotel(hotel_id, hotel_name, hotel_stars, hotel_address)

            room = model.Room(room_id, hotel, room_number, room_type_id, price_per_night)

            booking = model.Booking(
                booking_id=booking_id,
                room=room,
                check_in_date=check_in,
                check_out_date=check_out,
                total_amount=total_amount,
                guest=guest,
                is_cancelled=bool(is_cancelled)
            )
            
            # Invoice zuweisen, falls vorhanden
            if invoice_id:
                invoice = model.Invoice(
                    invoice_id=invoice_id,
                    booking_id=booking_id,
                    issue_date=issue_date,
                    total_amount=invoice_amount,
                )
                booking.invoice = invoice
            
            return booking
        
        return None

    def read_av_rooms(self, check_out_date: date, check_in_date: date) -> list[model.Room]:
        #Raise Value Errors
        sql = """
        SELECT 
        Room.room_id,
        Room.room_number,
        Room.type_id,
        Room.price_per_night,
        Room.hotel_id,
        Hotel.name,
        Hotel.stars,
        Hotel.address_id,
        Address.street,
        Address.city,
        Address.zip_code
        FROM 
            Room
        JOIN Hotel on Hotel.hotel_id= Room.hotel_id
        JOIN Address on Address.address_id = Hotel.address_id
        LEFT JOIN 
            Booking ON Room.room_id = Booking.room_id
        WHERE not (Booking.check_out_date >= ?
        AND Booking.check_in_date <= ?)
        OR Booking.room_id IS NULL
        """
        rows = self.fetchall(sql, (check_in_date, check_out_date))
        if rows:
            all_av_rooms = []

            for (room_id, room_number, type_id, price_per_night,
                hotel_id, name, stars,
                address_id, street, city, zip_code) in rows:

                #Objekte erstellen, um die verfügbaren Zimmer in der Liste zu appenden
                address = model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
                hotel = model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address=address)
                av_room = model.Room(room_id=room_id, hotel_id=hotel, room_number=room_number, room_type=type_id, price_per_night=price_per_night)
                all_av_rooms.append(av_room)
        
            return all_av_rooms
        
        return None
        

    def read_all_av_rooms_by_hotel(self, hotel_id:int, check_out_date:date, check_in_date:date) -> list[model.Room]:
        if not hotel_id:
            raise ValueError("Hotel Id has to be defined")
        if not isinstance(hotel_id, int):
            raise ValueError("Hotel Id has to be an integer")
        if not isinstance(check_in_date, date):
            raise ValueError("Check in Date has to be a date")
        if not isinstance(check_out_date, date):
            raise ValueError("Check out Date has to be a date")
        # if check_out_date <= check_in_date:
        #     raise ValueError("Check-out date must be after check-in date")
        
        sql = """
        SELECT 
            Room.room_id,
            Room.hotel_id,
            Room.room_number,
            Room.type_id,
            Room.price_per_night
        FROM 
            Room
        LEFT JOIN 
            Booking ON Room.room_id = Booking.room_id
        WHERE 
            Room.hotel_id = ? AND (
                NOT (
                    Booking.check_out_date >= ?
                    AND Booking.check_in_date <= ?
                )
                OR Booking.room_id IS NULL
            )
        """

        params = (hotel_id, check_in_date, check_out_date)
        rows = self.fetchall(sql, params)
        
        if rows:
            all_av_rooms = []

            for (room_id, hotel_id, room_number, type_id, price_per_night) in rows:               
                #Objekt für verfügbare Zimmer erstellen
                av_room = model.Room(room_id=room_id, hotel_id=hotel_id, room_number=room_number, room_type=type_id, price_per_night=price_per_night)
                #verfügbare Zimmer in der leeren Liste appenden
                all_av_rooms.append(av_room)
            
            return all_av_rooms
        
        return None

    def read_av_rooms_city(self, city: str, check_out_date: date, check_in_date: date) -> list[model.Room]:
        if not city:
            raise ValueError("City has to be defined")
        if not isinstance(city, str):
            raise ValueError("City has to be a string")
        if not isinstance(check_in_date, date):
            raise ValueError("Check in Date has to be a date")
        if not isinstance(check_out_date, date):
            raise ValueError("Check out Date has to be a date")
        # if check_out_date <= check_in_date:
        #     raise ValueError("Check-out date must be after check-in date")        

        sql = """
        SELECT 
            Room.room_id,
            Room.room_number,
            Room.type_id,
            Room.price_per_night,
            Room.hotel_id,
            Hotel.name,
            Hotel.stars,
            Address.address_id,
            Address.street,
            Address.city,
            Address.zip_code
        FROM 
            Room
        Join Hotel on hotel.hotel_id = Room.hotel_id
        Join Address on Address.address_id = Hotel.address_id
        LEFT JOIN 
            Booking ON Room.room_id = Booking.room_id
                AND Booking.check_in_date <= ?
                AND Booking.check_out_date >= ?
        WHERE Booking.room_id IS NULL
        AND Address.city Like ?
        """
        like = f"%{city}%"
        rows = self.fetchall(sql, (check_out_date, check_in_date, like))
        if rows:
            all_av_rooms = []

            for (room_id, room_number, type_id, price_per_night,
                hotel_id, name, stars,
                address_id, street, city, zip_code) in rows:

                #Objekte erstellen, um die verfügbaren Zimmer in der Liste zu appenden
                address = model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
                hotel = model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address=address)
                av_room = model.Room(room_id=room_id, hotel_id=hotel, room_number=room_number, room_type=type_id, price_per_night=price_per_night)
                all_av_rooms.append(av_room)
            
            return all_av_rooms
        return None

    def create_new_booking(self, room_id:int, check_in_date:date, check_out_date:date, guest_id:int, total_amount:float) -> model.Booking:
        if not room_id:
            raise ValueError("Room has to be defined")
        if not isinstance(check_in_date, date):
            raise ValueError("Check in Date has to be a date")
        if not isinstance(check_out_date, date):
            raise ValueError("Check out Date has to be a date")
        if check_out_date <= check_in_date:
            raise ValueError("Check-out date must be after check-in date")
        if not guest_id:
            raise ValueError("Guest has to be defined")

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

        params = (guest_id, room_id, check_in_date, check_out_date, total_amount)
        last_row_id, _ = self.execute(sql, params)

        return model.Booking(booking_id=last_row_id, room=room_dao, check_in_date=check_in_date, check_out_date=check_out_date, total_amount=total_amount, guest=guest_dao, is_cancelled=False)
        
    def cancell_booking(self, booking_id:int)-> None:
        if not booking_id:
            raise ValueError("Booking ID is required.")
        #Das Check In Datum soll in nicht in der Vergangenheit liegen
        booking= self.read_booking_by_id(booking_id)
        if booking.check_in_date <= date.today():
            raise ValueError("This Booking cannot be cancelled.")
        #Die Buchung soll nicht nochmals storniert werden
        if booking.is_cancelled:
            raise ValueError("This Booking has already been cancelled")
        #Buchungen, die eine Rechnung haben sollten nicht storniert werden können
        if booking.invoice is not None:
            raise ValueError("This Booking has been billed and cannot be cancelled")

        today = date.today()

        booking= self.read_booking_by_id(booking_id)
        sql = """
        UPDATE booking
        SET is_cancelled = 1
        WHERE booking_id = ?
        """
        self.execute(sql, (booking_id,))
