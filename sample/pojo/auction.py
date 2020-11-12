import sys
sys.path.append('..')
from pojo.housing import Housing
from pojo.mortgage import Mortgage
from pojo.land import Land


class Auction:
    def __init__(self):
        self.title = ''
        self.owner_info = []
        self.housing_info = Housing()
        self.real_estate_use = ''
        self.building_structure = ''
        self.build_area = ''
        self.elevator = ''
        self.renovation = ''
        self.building_age = ''
        self.arrears = ''
        self.seizure = '不详'
        self.mortgage_situation = Mortgage()
        self.land_situation = Land()
        self.lease = ''

    def get_title(self):
        return self.title

    def get_owner_info(self):
        return self.owner_info

    def get_housing_info(self):
        return self.housing_info

    def get_real_estate_use(self):
        return self.real_estate_use

    def get_building_structure(self):
        return self.building_structure

    def get_build_area(self):
        return self.build_area

    def get_elevator(self):
        return self.elevator

    def get_renovation(self):
        return self.renovation

    def get_building_age(self):
        return self.building_age

    def get_arrears(self):
        return self.arrears

    def get_seizure(self):
        return self.seizure

    def get_mortgage_situation(self):
        return self.mortgage_situation

    def get_land_situation(self):
        return self.land_situation

    def get_lease(self):
        return self.lease

    def set_title(self, title):
        self.title = title

    def add_owner_info(self, owner):
        self.owner_info.append(owner)

    def set_housing_info(self):
        pass

    def set_real_estate_use(self, realUse):
        self.real_estate_use = realUse

    def set_building_structure(self, structure):
        self.building_structure = structure

    def set_build_area(self, area):
        self.build_area = area

    def set_elevator(self, elevator):
        self.elevator = elevator

    def set_renovation(self, renovation):
        self.renovation = renovation

    def set_building_age(self, age):
        self.building_age = age

    def set_arrears(self, arrears):
        self.arrears = arrears

    def set_seizure(self, seizure):
        self.seizure = seizure

    def set_mortgage_situation(self):
        pass

    def set_land_situation(self):
        pass

    def set_lease(self, lease):
        self.lease = lease
