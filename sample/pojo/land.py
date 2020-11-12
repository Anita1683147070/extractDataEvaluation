class Land:
    def __init__(self):
        self.nature_of_land = ''
        self.land_use_right = ''
        self.land_use_period = ''

    def set_nature_of_land(self, natureOfLd):
        self.nature_of_land = natureOfLd

    def set_land_use_right(self, LdUseRight):
        self.land_use_right = LdUseRight

    def set_land_use_period(self, LdUsePeriod):
        self.land_use_period = LdUsePeriod

    def get_nature_of_land(self):
        return self.nature_of_land

    def get_land_use_right(self):
        return self.land_use_right

    def get_land_use_period(self):
        return self.land_use_period