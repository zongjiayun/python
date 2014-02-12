# -*- coding: utf-8 -*-
'''
Created on Feb 12, 2014

@author: xiaos_hui

'''

import re, util, traceback


def dealOneWord(wordPageURL):
    """处理一个单词

    :param wordPageURL example: 'http://www.51voa.com/Voa_English_Learning/1949-minority-54577.html'
    """
    try:
        print wordPageURL
        content = util.getPageContent(wordPageURL)

        mp3URL = getMp3URL(content)
        mp3Text = getMp3Text(content)

        util.download(mp3URL)
        title = re.findall(r'[\w-]+.mp3', mp3URL).pop()
        util.insertToFile(title + ':\n' + mp3Text)
    except IndexError:
        print traceback.format_exc()


def getMp3URL(pageContent):
    """提取 mp3 网络地址 mp3URL

    """
    # patternMp3b = r'http.+\.mp3(?=\"\s)'
    patternMp3b = r'http.+\.mp3'
    mp3URLList = re.findall(patternMp3b, pageContent)
    return mp3URLList.pop()

def getMp3Text(pageContent):
    """提取音频文本 mp3Text

    """
    patternText = r'(?<=id="content">)((.|\n)*?)(?=</div>)'
    mp3TextList = re.findall(patternText, pageContent)
#     print type(mp3TextList)  # 'list': [(\xe8\xaf\x8d\xe6\x98\xafcommanding... \r\n', '\n')]
    try:
        txtTuple = mp3TextList.pop()
    except IndexError:
        print 'No mp3Text found from content:\n' + pageContent
        print traceback.format_exc()
        exit()
    print mp3TextList
    return txtTuple[0]





'''

#### -*- TEST -*- ####

'''
# Attention:. 不包括换行
# 文本带换行的页面:
# ur = 'http://www.51voa.com/Voa_English_Learning/Learn_A_Word_21947.html'
ur = 'http://www.51voa.com/Voa_English_Learning/Learn_A_Word_39652.html'
# 文本不带换行的页面
# ur = 'http://www.51voa.com/Voa_English_Learning/1952-motive-54672.html'
# 这个能处理的url 的匹配部分的最后为： 今天我们学习的词是 motive, motive, motive... </div> 注意文本和 </div> 在一行

def localTest():
    """测试获取音频文本

    """
    content = util.getPageContent(ur)
    mp3Text = getMp3Text(content)
    print type(mp3Text)  # 'tuple'
    print mp3Text
    print mp3Text[0]

# localTest()

