import os
import sys
from service.readdoc_service import Case
from utils.template import get_template
import json
from utils.convert2json import recommendation2json


if __name__ == '__main__':
    template = get_template('utils/targetinfo.txt')
    similarity = 0.97
    cases = []
    path = os.path.abspath('../data')
    #print('path', path)
    for root, dirs, files in os.walk(path):
        for dirName in dirs:
            #print('dirname', dirName)
            case = Case(template, root, dirName, similarity)
            cases.append(case.get_case())
    resultFile = os.path.join(os.path.abspath('.'), 'testJson.json')
    with open(resultFile, 'w+', encoding='utf-8') as jsonFile:
        jsonContent = json.dumps(cases, default=recommendation2json, ensure_ascii=False, indent=4)
        jsonFile.write(jsonContent)
