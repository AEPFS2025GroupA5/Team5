class Address:
    def __repr__(self):
        return (
            f"Address(\n"
            f"  ID: {self.addressid}\n"
            f"  Street: {self.street}\n"
            f"  City: {self.city}\n"
            f"  Zipcode: {self.zipcode}\n"
            f")"
        )

    def __init__(self, addressid:int, street:str, city:str, zipcode:str):
        self.__address_id = addressid
        self._street = street
        self._city = city
        self._zipcode = zipcode

        if addressid is None:
            raise ValueError("Address Id is required")
        if not isinstance(addressid, int):
            raise ValueError("Address Id has to be an integer")
        
        if street is None:
            raise ValueError("Street is required")
        if not isinstance(street, str):
            raise ValueError("Street has to be a string")

        if city is None:
            raise ValueError("City is required")
        if not isinstance(city, str):
            raise ValueError("City has to be a string")
        
        if zipcode is None:
            raise ValueError("Zipcode is required")
        if not isinstance(zipcode, str):
            raise ValueError("Zipcode has to be a string")

    @property
    def addressid(self):
        return self.__address_id

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, new_street:str):
        if not isinstance(new_street, str):
            raise ValueError("The new street name has to be a string")
        if not new_street:
            raise ValueError("New Street is required")
        else:
            self._street = new_street
            print(f"You have changed the street into {new_street}")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city:str):
        if not isinstance(new_city, str):
            raise ValueError("The new city name has to be a string")
        if not new_city:
            raise ValueError("New city is required")
        else:
            self._city = new_city
            print("You have changed the city into {new_city}")

    @property
    def zipcode(self):
        return self._zipcode

    @zipcode.setter
    def zipcode(self, new_zipcode:str):
        if not len(new_zipcode) >= 4:
            raise ValueError("A Zipcode has to be longer than 4 characters")
        if not new_zipcode:
            raise ValueError("A new zipcode is required")
        if not isinstance(new_zipcode, str):
            raise ValueError("A new zipcode has to be a string") 
        else: 
            self._zipcode = new_zipcode
            print("You have changed the zipcode into {new_zipcode}")

    def show_user_friendly(self):
        return (
            f"Street: {self._street}\n"
            f"City: {self._city}\n"
        )