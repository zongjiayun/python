# -*- coding: utf-8 -*-
'''
Created on Feb 12, 2014

@author: xiaos_hui
'''

import util, aword


test = True

wordURLList = util.getAllWordPageURLOnePaging('http://www.51voa.com/Learn_A_Word_1.html')
# ['http://www.51voa.com/Voa_English_Learning/1955-binge-watch-54675.html', 'http://www.51voa.com/Voa_English_Learning/1954-discard-54674.html']


# URL = "http://down.51voa.com/201401/1955-binge-watch.mp3";
# down.download(URL);


# aword.dealOneWord('http://www.51voa.com/Voa_English_Learning/1955-binge-watch-54675.html')

def deal():
    for wordURL in wordURLList:
        if test:
            print wordURL
        else:
            aword.dealOneWord(wordURL)





pageContent = '<a id="mp3" href="http://down.51voa.com/learning/lw05.mp3" title="鼠标右键点击下载"></a><a id="help" href="/intro/help.html" target=_blank></a><BR></div><div id="content"><BR><BR><P>今天要学的一个词组是：<STRONG>opt for</STRONG>。 Opt for就是选择。比如，美国国务卿赖斯在紧张处理中东事务后： "...opted ...for a piano recital featuring classical pieces for her performance...," 意思是她选择举行钢琴独奏会，为大家演奏古典乐曲。 </P><P>你是要一辆很贵的豪华轿车呢，还是一辆既便宜但又实用的车？ Would you opt for an expensive luxurious car or a reasonable but practical car? 要是有机会出国留学，或有一份高工资的工作等着你，你会选择什么呢？ Would you opt for further study abroad or a well-paid job? 我什么都要，行吗？ No, you can opt for only one。今天学的词组是opt for...<BR></P></div><div id="Bottom_VOA">'
aword.getMp3Text(pageContent);




