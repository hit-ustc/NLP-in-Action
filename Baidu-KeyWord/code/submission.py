#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import jieba
import jieba.posseg
import jieba.analyse
import re
from loadDataSet import loadData

import sys

reload(sys)

sys.setdefaultencoding('utf8')


print('='*40)
print('关键词提取')
print('-'*40)
print(' TF-IDF')
print('-'*40)

tf_idf_result = open('../data/writedata_20w_TF-IDF_result', 'wb')
textrank_result = open('../data/writedata_20w_textrank_result', 'wb')

dataset = loadData()

for data in dataset:
    content =  dataset[data]
    sentences = content.strip("\n").split("。")

    result = "["

    for sentence in sentences:
        if len(sentence) <= 0:
            continue
        index = 0
        score = 0
        for key, value in jieba.analyse.extract_tags(sentence, withWeight=True):
            if index == 0:
                entity = key
                score = value
                break;

        # print ('%d %s %s' % (data, x, w))
        result = result + "{\"content\": \"%s。\", \"core_entity\": [\"%s\"]}" % (sentence, entity) + ","
        # print result
    result = result[:-1]
    result = result + "]" + "\n"
    # print result
    tf_idf_result.write(result)

# s = "程序员(英文Programmer)是从事程序开发、维护的专业人员。一般将程序员分为程序设计人员和程序编码人员，但两者的界限并不非常清楚，特别是在中国。软件从业人员分为初级程序员、高级程序员、系统分析员和项目经理四大类。"
# for x, w in jieba.analyse.extract_tags(s, withWeight=True):
#     print('%s %s' % (x, w))
print "TF-IDF is over"

print('-'*40)
print(' TextRank')
print('-'*40)

# for x, w in jieba.analyse.textrank(s, withWeight=True):
#     print('%s %s' % (x, w))

# for data in dataset:
#     content =  dataset[data]
#     x, w = jieba.analyse.textrank(content, withWeight=True)[0]
#     print ('%s %s' % (x, w))

for data in dataset:
    content =  dataset[data]
    # print data, content
    sentences = content.strip("\n").split("。")

    result = "["

    for sentence in sentences:
        if len(sentence) <= 0:
            continue
        index = 0
        score = 0
        for key, value in jieba.analyse.textrank(sentence, withWeight=True):
            if index == 0:
                entity = key
                score = value
                break;

        result = result + "{\"content\": \"%s。\", \"core_entity\": [\"%s\"]}" % (sentence, entity) + ","
        # print result
    result = result[:-1]
    result = result + "]" + "\n"
    textrank_result.write(result)

print "TextRank is over"