class Mortgage:
    def __init__(self):
        self.mortgagee = ''
        self.mortgage_no = ''
        self.text = ''

    def set_mortgagee(self, mort):
        self.mortgagee = mort

    def set_mortgage_no(self, mortNo):
        self.mortgage_no = mortNo

    def set_text(self, text):
        self.text = text

    def get_mortgagee(self):
        return self.mortgagee

    def get_mortgagee_no(self):
        return self.mortgage_no

    def get_text(self):
        return self.text