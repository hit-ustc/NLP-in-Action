# -*- coding:utf-8 -*-
import csv
import sys

stopwords = {}
label = ['C000007', 'C000008', 'C000010', 'C000013', 'C000014', 'C000016', 'C000020', 'C000022', 'C000023', 'C000024']

def stopword():
    f = open('../data/stopword.csv')
    rows = csv.reader(f)
    for row in rows:
        stopwords[str(row)] = True


def eachClass200docs(docments):
    termDic = dict()
    termClassDic = dict()
    for eachclass in label:
        currClassPath = "../data/sougouC/" + eachclass+"/"
        eachClassWords = set()
        eachClassDocWords = list()
        for i in range(docments):
            eachDocName = currClassPath+str(i)+".txt"
            eachDocPath = open(eachDocName, 'r')
            eachDocContent = eachDocPath.read()
            eachFileWords = eachDocContent.split(" ")
            eachDocWords = set()
            for eachword in eachFileWords:
                if eachword not in stopwords and len(eachword.strip(" ")) > 0 and eachword.strip(" ") != " ":
                    eachDocWords.add(eachword)
                    eachClassWords.add(eachword)
            eachClassDocWords.append(eachDocWords)

        termDic[eachclass] = eachClassWords
        termClassDic[eachclass] = eachClassDocWords
    return termDic, termClassDic


# 卡方计算公式
# 对卡方检验所需的 a b c d 进行计算
# a：在这个分类下包含这个词的文档数量
# b：不在该分类下包含这个词的文档数量
# c：在这个分类下不包含这个词的文档数量
# d：不在该分类下，且不包含这个词的文档数量
def ChiCalc(a, b, c, d):
    result = float(pow((a*d - b*c), 2)) /float((a+c) * (a+b) * (b+d) * (c+d))
    return result


# K 每个类别选取的特征个数
def featureSelection(termDic, termClassDic, K):
    termCountDic = dict()
    for key in termDic:
        classWords = termDic[key]
        classTermCountDic = dict()
        for eachword in classWords:
            a = 0
            b = 0
            c = 0
            d = 0
            for eachclass in termClassDic:
                if eachclass == key:
                    for eachdoc in termClassDic[eachclass]:
                        if eachword in eachdoc:
                            a = a + 1
                        else:
                            c = c + 1
                else:
                    for eachdoc in termClassDic[eachclass]:
                        if eachword in eachdoc:
                            b = b + 1
                        else:
                            d = d + 1

            eachwordcount = ChiCalc(a, b, c, d)
            classTermCountDic[eachword] = eachwordcount

        sortedClassTermCountDic = sorted(classTermCountDic.items(), key=lambda d:d[1], reverse=True)
        count = 0
        subDic = dict()
        for i in range(K):
            subDic[sortedClassTermCountDic[i][0]] = sortedClassTermCountDic[i][1]
        termCountDic[key] = subDic
    return termCountDic


def writeFeatureToFile(termCountDic, fileName):
    features = set()
    for key in termCountDic:
        for eachkey in termCountDic[key]:
            features.add(eachkey)
    count = 1
    file = open("../feature/" + fileName, 'w')
    for feature in features:
        if len(feature.strip(" ")) > 0 and feature.strip(" ") != " " :
            file.write(str(count)+" " +feature+"\n")
            count = count + 1
    print "特征个数共有 %d个" %count
    file.close()


# 生成停用词词典
stopword()

# 每个类别下取前200个文件
termDic, termClassDic = eachClass200docs(200)

# 特征选择，每个类别选择前1000个特征
termCountDic = featureSelection(termDic, termClassDic, 1000)

# 保存特征
writeFeatureToFile(termCountDic, "SVMFeature.txt")
