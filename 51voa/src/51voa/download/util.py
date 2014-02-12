# -*- coding: utf-8 -*-
'''
Created on Feb 12, 2014

@author: xiaos_hui
'''
import urllib2, re, urllib

txtFile = 'words.txt'
def insertToFile(text):
    f = open(txtFile, 'a+')
    f.write('\n')
    f.write(text)
    f.close()


def getPageContent(wordPageURL):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib2.Request(wordPageURL, headers=headers)
    return urllib2.urlopen(req).read()


class URLFinder:
    """URLFinder

    """
    def getWordPageURL(self, wordsListURL):
        """
        :param wordsListURL example: http://www.51voa.com/Learn_A_Word_1.html
        """
        content = getPageContent(wordsListURL)
        wordList = re.findall(r'(?<=id="list">).+?(?=<div)', content)
        return wordList


def getAllWordPageURLOnePaging(url):
    """获取一个分页中所有单词URL列表,param

    :param url example:'http://www.51voa.com/Learn_A_Word_1.html'
    :returns ['单词1 html页面url','单词2 html页面url']
    """
    x = URLFinder()
    worList = x.getWordPageURL(url)

    def addBaseURL(item):
        return 'http://www.51voa.com' + item

    wordURLList = re.findall(r'(?<=href=").+?(?=")', worList.pop())
    return map(addBaseURL, wordURLList)


def download(fileUrl):
    """...

    :param fileUrl 资源地址
    """
    def dealFile(matched):
        fileName = matched.group(0);
        print fileName
        urllib.urlretrieve(fileUrl, fileName)

    re.sub(r'[\w-]+\.mp3', dealFile, fileUrl)


def getContentPages(start, end):
    """
    :param start 起始页 ,最小值为1
    :param end 结束页 ,最大值为41
    :returns example:  ['http://www.51voa.com/Learn_A_Word_1.html']
    """
    def getURL(num):
        return 'http://www.51voa.com/Learn_A_Word_' + str(num) + '.html'
    return map(getURL, range(start, end))


