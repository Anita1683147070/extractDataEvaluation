import sys

sys.path.append('..')
import os
import re
from pojo.recommendation import Recommendation
from utils.selecttables import isJDFile
from docx import Document
from service.readjd_service import ReadTables
from service.readjd_service import get_jdheader


class Case:
    def __init__(self, template, root, dirName, similarity=0.97):
        self.recommendation = Recommendation()
        self.similarity = similarity
        self.root = root
        self.dirName = dirName
        self.template = template

    def get_case(self):
        '''
        for root, dirs, files in data/107678832:
            for file in files:
                if '.docx' and 还没有找到目标文件:
                    if 是京东文件:
                        读文件头
                        读表格
                        标记已找到目标文件
                    else 不是京东文件:
                        暂时不处理
                else pdf文件 或者 已经找到目标文件:
                    跳过
        :return: self.recommendation 一个子文件夹(一个案例)的信息
        '''
        self.recommendation.set_doc_id(self.dirName)
        oneFileRead = False
        for root, dirs, files in os.walk(os.path.join(self.root, self.dirName)):
            for file in files:
                if os.path.splitext(file)[-1] == '.docx' and not oneFileRead:
                    doc = Document(os.path.join(root, file))
                    if isJDFile(doc):
                        # 读文件内容(待处理）
                        #print('    read header')
                        get_jdheader(self.recommendation, self.template, doc, self.similarity)  #只读前几段
                        # 读表格
                        #print('    read tables')
                        tables = ReadTables(self.template, doc, self.similarity)
                        self.recommendation.add_to_auction_info(tables.list_auctions())
                        oneFileRead = True
                    else:  # @do 不是京东文件待处理
                        pass
                else:  # pdf文件不读
                    pass
        return self.recommendation
