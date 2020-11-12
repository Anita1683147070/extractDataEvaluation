import re
from docx import Document


def isBasicTable(tb):
    """

    :param tb:京东文件中的一个word表格
    :return: 1 | 0 是不是一个总体基本表格
    """
    #rowOk = (len(tb.rows) > 14) & (len(tb.rows) < 33)
    rowOk = 1
    colOk = (len(tb.columns) == 3)
    return rowOk & colOk


def isJDFile(doc):
    isJD = False
    isCompleteJDFile = False
    for para in doc.paragraphs:
        JD = re.search('京东', para.text)
        docHead = re.search('执行案号', para.text)  #可能有多个京东文件，但是只有一份有用
        if JD is not None:
            isJD = True
        if docHead is not None:
            isCompleteJDFile = True
        if isJD and isCompleteJDFile:
            return True
    return False
