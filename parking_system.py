class ParkingSystem(object):

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.occupied_place = {"big": 0, "medium": 0, "small": 0}

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if not self.check_type(carType, self.big, "big"):
                return False

        if carType == 2:
            if not self.check_type(carType, self.medium, "medium"):
                return False

        if carType == 3:
            if not self.check_type(carType, self.small, "small"):
                return False

        return True

    def check_type(self, carType: int, type: int, type_in_str: str) -> bool:
        if not type:
            return False

        if self.occupied_place.get(type_in_str) >= type:
            return False

        self.occupied_place[type_in_str] += 1
        return True
