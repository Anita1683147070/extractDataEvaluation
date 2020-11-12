class Owner:
    def __init__(self):
        self.owner = ''
        self.certificate_number = ''

    def set_owner(self, ownerName):
        self.owner = ownerName

    def set_certificate_number(self, certiNumber):
        self.certificate_number = certiNumber

    def get_owner(self):
        return self.owner

    def get_certificate_number(self):
        return self.certificate_number