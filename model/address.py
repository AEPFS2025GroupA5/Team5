class Address:
    def __repr__(self):
        return (
            f"Address(\n"
            f"  ID: {self.__addressid}\n"
            f"  Street: {self._street}\n"
            f"  City: {self._city}\n"
            f"  Zipcode: {self._zipcode}\n"
            f")"
        )

    def __init__(self, addressid:int, street:str, city:str, zipcode:str):
        self.__addressid = addressid
        self._street = street
        self._city = city
        self._zipcode = zipcode

    @property
    def addressid(self):
        return self.__addressid

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, new_street:str):
        self._street = new_street
        print("Success")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city:str):
        self._city = new_city
        print("Success")

    @property
    def zipcode(self):
        return self._zipcode

    @zipcode.setter
    def zipcode(self, new_zipcode:str):
        if len(new_zipcode) >= 4:
            self._zipcode = new_zipcode
            print("Success")
        else:
            print("Invalid zipcode")