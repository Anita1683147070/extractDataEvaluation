import os
import sys

sys.path.append('..')
import re
from bert_serving.client import BertClient
from sklearn.metrics.pairwise import cosine_similarity
from pojo.owner import Owner
from utils.strformat import str2date

nonwritable = ['', '\n', '\r', '\t']


def get_template(path):
    """

    :param path: 从targetinfo.txt文件获取要提取信息的标签
    :return: 一个字典列表
    """
    result = []
    with open(path, 'r+', encoding='utf-8') as txtFile:
        for line in txtFile.readlines():
            newDict = {}
            line = line.replace(' ', '').replace('\n', '')
            dictKey, contents = re.split('[:：]', line)
            contents = re.split('[,，]', contents)
            bc = BertClient()
            encodeContents = []
            for content in contents:
                content = bc.encode([content])
                encodeContents.append(content)
            newDict[dictKey] = encodeContents
            result.append(newDict)
    return result


def get_similar_tag(template, cellKey):
    """
        template = [{'doc_id':[[vector1],[vector2],...]}, {'case_no':[[vector],...]},...]
        cellKey = '建筑面积'
        destiKey = 'doc_id'  #一个字典只有一个key,所以是list(template[i].keys())[0]
        for tag in template:
            curKey = doc_id
            for vector in tag[curKey]：
                找这个tag相似度最大的一个vector
            这个tag最大的vector大于destikey的相似度，则更新 destiKey = this tag

    """
    cellKey = cellKey.replace(' ', '').replace('\n', '')
    bc = BertClient()
    encodeCellKey = bc.encode([cellKey])
    destiKeySimilar = 0.0
    destiKey = list(template[0].keys())[0]
    for tag in template:
        curKeySimilar = 0.0
        curKey = list(tag.keys())[0]
        for embedding in tag[curKey]:
            similar_tag_encodeCellKey = cosine_similarity(embedding, encodeCellKey)
            if similar_tag_encodeCellKey > curKeySimilar:
                curKeySimilar = similar_tag_encodeCellKey
            else:
                pass
        if curKeySimilar > destiKeySimilar:
            destiKeySimilar = curKeySimilar
            destiKey = curKey
        else:
            pass
    return destiKey, destiKeySimilar


def add2auction(auction, destiKey, cellContent):
    """
        add the cell text to auction
        return auction
    """
    cellContent = cellContent.replace(' ', '').replace('\n', '')
    if destiKey == 'title':
        auction.set_title(cellContent)
    elif destiKey == 'owner':
        owners = auction.get_owner_info()
        if len(owners) == 0:
            owner = Owner()
        else:
            owner = owners.pop(0)  ## @do 如果是多个权属人还要分离
        owner.set_owner(cellContent)
        auction.add_owner_info(owner)
    elif destiKey == 'certificate_number':
        owners = auction.get_owner_info()
        if len(owners) == 0:
            owner = Owner()
        else:
            owner = owners.pop(0)  ## @do 如果是多个权属人还要...
        owner.set_certificate_number(cellContent)
        auction.add_owner_info(owner)
    elif destiKey == 'housing_estate':
        auction.get_housing_info().set_housing_estate(cellContent)
    elif destiKey == 'developers':
        auction.get_housing_info().set_developers(cellContent)
    elif destiKey == 'realty_management_corp':
        auction.get_housing_info().set_realty_management_corp(cellContent)
    elif destiKey == 'real_estate_use':
        auction.set_real_estate_use(cellContent)
    elif destiKey == 'building_structure':
        auction.set_building_structure(cellContent)
    elif destiKey == 'build_area':
        auction.set_build_area(cellContent)
    elif destiKey == 'elevator':
        auction.set_elevator(cellContent)
    elif destiKey == 'renovation':
        auction.set_renovation(cellContent)
    elif destiKey == 'building_age':
        auction.set_building_age(cellContent)
    elif destiKey == 'arrears':
        auction.set_arrears(cellContent)
    elif destiKey == 'seizure':
        auction.set_seizure(cellContent)
    elif destiKey == 'mortgagee':
        auction.get_mortgage_situation().set_mortgagee(cellContent)
    elif destiKey == 'mortgage_no':
        auction.get_mortgage_situation().set_mortgage_no(cellContent)
    elif destiKey == 'text':
        auction.get_mortgage_situation().set_text(cellContent)
    elif destiKey == 'nature_of_land':
        auction.get_land_situation().set_nature_of_land(cellContent)
    elif destiKey == 'land_use_right':
        auction.get_land_situation().set_land_use_right(cellContent)
    elif destiKey == 'land_use_period':
        auction.get_land_situation().set_land_use_period(cellContent)
    elif destiKey == 'lease':
        auction.set_lease(cellContent)


def add2recommendation(recommendation, destiKey, cellContent):
    if destiKey == 'case_no':
        recommendation.get_litigation_info().add_case_no(cellContent)
    elif destiKey == 'execution_applicant':
        recommendation.get_litigation_info().add_execution_applicant(cellContent)
    elif destiKey == 'executed_person':
        recommendation.get_litigation_info().add_executed_person(cellContent)
    elif destiKey == 'judgment_no':
        recommendation.get_litigation_info().add_judgment_no(cellContent)
    elif destiKey == 'evaluation_agency':
        recommendation.set_evaluation_agency(cellContent)
    elif destiKey == 'evaluation_time':
        cellContent = str2date(cellContent)
        recommendation.set_evaluation_time(cellContent)
