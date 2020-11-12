import sys
sys.path.append('..')
from pojo.auction import Auction
from pojo.litigation import Litigation


class Recommendation:
    def __init__(self):
        self.doc_id = ''
        self.litigation_info = Litigation()
        self.evaluation_agency = ''
        self.evaluation_time = ''
        self.auction_info = []

    def set_doc_id(self, docId):
        self.doc_id = docId

    def set_evaluation_agency(self, agency):
        self.evaluation_agency = agency

    def set_evaluation_time(self, evaTime):
        self.evaluation_time = evaTime

    def add_to_auction_info(self, auctions):
        self.auction_info.extend(auctions)

    def get_litigation_info(self):
        return self.litigation_info

    def get_doc_id(self):
        return self.doc_id

    def get_evaluation_agency(self):
        return self.evaluation_agency

    def get_evaluation_time(self):
        return self.evaluation_time

    def get_auction_info(self):
        return self.auction_info