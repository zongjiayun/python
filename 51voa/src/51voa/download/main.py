# -*- coding: utf-8 -*-
'''
Created on Feb 12, 2014

@author: xiaos_hui
'''
import util, aword, traceback



def main():
    try:
        for add in util.getContentPages(2, 3):
            for wordURL in  util.getAllWordPageURLOnePaging(add):
                aword.dealOneWord(wordURL)
    except IndexError:
        print traceback.format_exc()


if __name__ == '__main__':
    main()
