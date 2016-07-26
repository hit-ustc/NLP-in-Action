# -*- coding:utf-8 -*-

import math
import sys

"""
 采用 TF-IDF算法对特征进行计算权重
"""

label = ['C000007', 'C000008', 'C000010', 'C000013', 'C000014', 'C000016', 'C000020', 'C000022', 'C000023', 'C000024']

TrainSetsDocCount = 200
TestSetsDocCount = 50

def loadClassDoc(path, label, TrainSetsDocCount, TestSetsDocCount):
    classWords = dict()
    for eachclass in label:
        classPath = path + eachclass + "/"
        eachClassWords = []
        for i in range(TrainSetsDocCount, TrainSetsDocCount + TestSetsDocCount):
            eachfile = open(classPath + str(i) + ".txt")
            eachDocContent = eachfile.read()
            eachDocWords = eachDocContent.split(" ")
            eachClassWords.append(eachDocWords)
        classWords[eachclass] = eachClassWords
    return classWords


def loadFeature(featureName):
    featureFile = open(featureName, 'r')
    featureContent = featureFile.read().split('\n')
    featureFile.close()
    features = []
    for eachfeature in featureContent:
        eachfeature = eachfeature.split(" ")
        if (len(eachfeature) == 2):
            features.append(eachfeature[1])
    return features


def featureIDF(classWords, features, dffilename):
    dffile = open(dffilename, "w")
    dffile.close()
    dffile = open(dffilename, "a")
    idffeature = dict()
    dffeature = dict()
    for feature in features:
        docFeature = 0
        docCount = 0
        for key in classWords:
            docCount = docCount + len(classWords[key])
            classfiles = classWords[key]
            for eachfile in classfiles:
                if feature in eachfile:
                    docFeature = docFeature + 1

        featureValue = math.log(float(docCount) / (docFeature+1))
        dffeature[feature] = docFeature
        dffile.write(feature + " " + str(docFeature) + "\n")
        idffeature[feature] = featureValue
    dffile.close()
    return idffeature


def TFIDFCal(features, classWords, idf_features, filename):
    file = open(filename, 'w')
    file.close()
    file = open(filename, 'a')
    for key in classWords:
        classFiles = classWords[key]
        classid = label.index(key)
        for eachfile in classFiles:
            file.write(str(classid) + " ")
            for i in range(len(features)):
                if features[i] in eachfile:
                    feature = features[i]
                    featureCount = eachfile.count(feature)
                    tf = float(featureCount) / (len(eachfile))
                    featureValue = idf_features[feature] * tf
                    file.write(str(i+1) + ":" + str(featureValue) + " ")
            file.write("\n")


classWords = loadClassDoc("../data/sougouC/", label, TrainSetsDocCount, TestSetsDocCount)
features = loadFeature("../feature/SVMFeature.txt")
idf_features = featureIDF(classWords, features, "../feature/test-df-feature.txt")
TFIDFCal(features, classWords, idf_features, "../test.svm")


