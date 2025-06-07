class Address:
    def __repr__(self):
        return (
            f"Address(\n"
            f"  ID: {self.address_id}\n"
            f"  Street: {self.street}\n"
            f"  City: {self.city}\n"
            f"  Zipcode: {self.zip_code}\n"
            f")"
        )

    def __init__(self, address_id:int, street:str, city:str, zip_code:str):
        self.__address_id = address_id
        self._street = street
        self._city = city
        self._zip_code = zip_code

        if address_id is None:
            raise ValueError("Address Id is required")
        if not isinstance(address_id, int):
            raise ValueError("Address Id has to be an integer")
        
        if street is None:
            raise ValueError("Street is required")
        if not isinstance(street, str):
            raise ValueError("Street has to be a string")

        if city is None:
            raise ValueError("City is required")
        if not isinstance(city, str):
            raise ValueError("City has to be a string")
        
        if zip_code is None:
            raise ValueError("Zipcode is required")
        if not isinstance(zip_code, str):
            raise ValueError("Zipcode has to be a string")

    @property
    def address_id(self):
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
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, new_zip_code:str):
        if not len(new_zip_code) >= 4:
            raise ValueError("A Zipcode has to be longer than 4 characters")
        if not new_zip_code:
            raise ValueError("A new zipcode is required")
        if not isinstance(new_zip_code, str):
            raise ValueError("A new zipcode has to be a string") 
        else: 
            self._zip_code = new_zip_code
            print("You have changed the zipcode into {new_zip_code}")

    def show_user_friendly(self):
        return (
            f"Street: {self._street}\n"
            f"City: {self._city}\n"
        )