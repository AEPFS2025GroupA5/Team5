from __future__ import annotations
#from room import Room


class Hotel:
    def __init__(self,
                hotel_id:int,
                name:str,
                stars:int,
                adress_id:int
         ):
        
        self._hotel_id = hotel_id
        self._name = name
        self._stars = stars
        self.adress_id = adress_id
    
        # Prüfungen
        if not isinstance (hotel_id, int):
            raise TypeError("hotel_id has to be int")
        if not hotel_id:
            raise ValueError("Hotel Id is required")
        if not isinstance(name, str):
            raise TypeError("Hotel name has to be str")
        if not name:
            raise ValueError("Hotel name is required")
        if not isinstance(stars, int):
            raise TypeError("Stars have to be int")
        
       
       
# @Getter
    @property
    def hotelid(self):
        return self._hotelid

    @property
    def name(self):
        return self._name

    @property
    def stars(self):
        return self._stars
    
    

##Funktionen

    # def show_hotelinfo(self):
    #     return f"Hotel ID: {self.hotelid} \nName: {self.name} \nStars: {self.stars} \nRooms: {self._rooms}:"

    # def update_info(self, name=None, stars=None):
    #     if name is not None:
    #         if not isinstance(name, str):
    #             raise TypeError("name must be a string")
    #         if not name:
    #             raise ValueError("name cannot be empty")
    #         self._name = name

    #     if stars is not None:
    #         if not isinstance(stars, int):
    #             raise TypeError("stars must be an integer")
    #         if not (0 <= stars <= 5):
    #             raise ValueError("stars must be between 0 and 5")
    #         self._stars = stars

    #     ##Adresse wäre auch

    # def add_room(self, room):
    #     if not isinstance(room, Room):
    #         raise TypeError("room must be a Room instance")
    #     self._rooms.append(room)


##Testdaten
# single1 = RoomType(1, "Single Suite", 2, "Schönes Einzelzimmer mit Meerblick")

# raum1 = Room(1, "ER 1.OG", single1, 49.99)

# hotel1 = Hotel(100, "Testhotel", 4, None)
# print(hotel1.show_hotelinfo())

# hotel1.update_info("Saliou", 5)

# print(hotel1.show_hotelinfo())