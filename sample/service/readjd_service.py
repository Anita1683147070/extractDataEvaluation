import sys

sys.path.append('..')
import os
import re
from pojo.auction import Auction
from utils.template import get_similar_tag
from utils.selecttables import isBasicTable
from utils.template import add2auction
from utils.template import nonwritable
from utils.template import add2recommendation


class ReadTables:
    def __init__(self, template, doc, similarity=0.97):
        self.auctions = []
        self.template = template
        self.similarity = similarity
        self.doc = doc

    def fillAuction(self, auction, str1, str2):
        if str1 in nonwritable or str2 in nonwritable:  #只有不可写字符串 107787739/
            pass
        else:
            destiKey, keySimilarity = get_similar_tag(self.template, str1)
            if keySimilarity >= self.similarity:
                if destiKey == 'land_situation':    ## 主要解决土地信息三条tag混合在一个cell，可能是两行三行四行
                    mixInfo = str2
                    mixInfo = mixInfo.split('\n')
                    if len(mixInfo) == 2:   #两行：第二条和第三条信息同在第二行
                        subMixInfo = mixInfo.pop().split()
                        mixInfo.extend(subMixInfo)
                    elif len(mixInfo) > 3:  #四行：第三条信息分在第三行和第四行
                        mixInfo[2] += mixInfo.pop()
                    else: # 标准的三行
                        pass
                    for info in mixInfo:
                        info = re.split('[:：]', info)
                        if len(info) == 1:  # 两行：“国有出让” ，上面没法处理这种没标签情况
                            self.fillAuction(auction, '土地性质', info[0])  # 需要信息分离,暂时全部填写到土地性质 @do
                        else:
                            self.fillAuction(auction, info[0], info[1])
                else:   ## 普通表格情况
                    add2auction(auction, destiKey, str2)
            else:   # 相似度太低的信息忽略
                pass

    def readBasicTable(self, auction, tb):
        """

        :param tb: a table from doc.tables
        :return: auction
        """
        #auction = Auction()
        for row in tb.rows:
            cells = row.cells
            if cells[1].text.strip() == cells[2].text.strip():  # 两列
                self.fillAuction(auction, cells[0].text, cells[1].text)
            else:   # 三列
                self.fillAuction(auction, cells[1].text, cells[2].text)
        #return auction

    def list_auctions(self):
        """

        :return: self.auctions 一个文件中所有的拍卖物的所有信息
        """
        auction = Auction()
        for tb in self.doc.tables:
            if isBasicTable(tb):
                self.readBasicTable(auction, tb)
            else:  # @do 带有信息的附属表格
                pass
        self.auctions.append(auction)
        return self.auctions


# temporary method
# to fill several target header information
def get_jdheader(recommendation, template, doc, similarity):
    for paraIndex, para in enumerate(doc.paragraphs):
        paras = re.split('[:：]', para.text.replace('\n', '').replace(' ', ''))
        if len(paras) == 2:  # 可能是目标信息
            if (paras[0] in nonwritable) or (paras[1] in nonwritable):  # 如果是空白信息则跳过
                continue
            else:
                destiKey, Similarity = get_similar_tag(template, paras[0])
            if Similarity >= similarity:
                add2recommendation(recommendation, destiKey, paras[1])
        else:  # 垃圾信息
            pass
        if paraIndex > 15:  # 只读前15行
            break
        else:
            pass
