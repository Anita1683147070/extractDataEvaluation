import json
import collections
import sys

sys.path.append('..')


def litigation2json(litigation_info):
    return collections.OrderedDict({
        'case_no': litigation_info.case_no,
        'execution_applicant': litigation_info.execution_applicant,
        'executed_person': litigation_info.executed_person,
        'judgment_no': litigation_info.judgment_no
    })


def owner2json(owner):
    return collections.OrderedDict({
        'owner': owner.owner,
        'certificate_number': owner.certificate_number
    })


def housing2json(housing):
    return collections.OrderedDict({
        'housing_estate': housing.housing_estate,
        'developers': housing.developers,
        'realty_management_corp': housing.realty_management_corp
    })


def mortgage2json(mortgage):
    return collections.OrderedDict({
        'mortgagee': mortgage.mortgagee,
        'mortgage_no': mortgage.mortgage_no,
        'text': mortgage.text
    })


def land2json(land):
    return collections.OrderedDict({
        'nature_of_land': land.nature_of_land,
        'land_use_right': land.land_use_right,
        'land_use_period': land.land_use_period
    })


def auction2json(auction):
    return collections.OrderedDict({
        'title': auction.title,
        'owner_info': [owner2json(owner) for owner in auction.owner_info],
        'housing_info': housing2json(auction.housing_info),
        'real_estate_use': auction.real_estate_use,
        'building_structure': auction.building_structure,
        'build_area': auction.build_area,
        'elevator': auction.elevator,
        'renovation': auction.renovation,
        'building_age': auction.building_age,
        'arrears': auction.arrears,
        'seizure': auction.seizure,
        'mortgage_situation': mortgage2json(auction.mortgage_situation),
        'land_situation': land2json(auction.land_situation),
        'lease': auction.lease
    })


def recommendation2json(recommendation):
    return collections.OrderedDict({
        'doc_id': recommendation.doc_id,
        'litigation_info': litigation2json(recommendation.litigation_info),
        'evaluation_agency': recommendation.evaluation_agency,
        'evaluation_time': recommendation.evaluation_time,
        'auction_info': [auction2json(auction) for auction in recommendation.auction_info]
    })

