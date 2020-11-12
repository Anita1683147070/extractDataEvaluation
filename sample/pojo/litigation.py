class Litigation:
    def __init__(self):
        self.case_no = []
        self.execution_applicant = []
        self.executed_person = []
        self.judgment_no = []

    def add_case_no(self, caseNo):
        self.case_no.append(caseNo)

    def add_execution_applicant(self, applicant):
        self.execution_applicant.append(applicant)

    def add_executed_person(self, person):
        self.executed_person.append(person)

    def add_judgment_no(self, judgmentNo):
        self.judgment_no.append(judgmentNo)

    def get_case_no(self):
        return self.case_no

    def get_execution_applicant(self):
        return self.execution_applicant

    def get_executed_person(self):
        return self.executed_person

    def get_judgment_no(self):
        return self.judgment_no
