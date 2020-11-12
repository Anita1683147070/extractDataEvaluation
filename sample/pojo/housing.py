class Housing:
    def __init__(self):
        self.housing_estate = ''
        self.developers = ''
        self.realty_management_corp = ''

    def set_housing_estate(self, housingEstate):
        self.housing_estate = housingEstate

    def set_developers(self, developers):
        self.developers = developers

    def set_realty_management_corp(self, realMana):
        self.realty_management_corp = realMana

    def get_housing_estate(self):
        return self.housing_estate

    def get_developers(self):
        return self.developers

    def get_realty_management_corp(self):
        return self.realty_management_corp
