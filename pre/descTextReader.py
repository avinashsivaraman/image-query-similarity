# import pandas as pd
# data = pd.read_csv('../desctxt/devset_textTermsPerPOI.txt', sep='', header=None)
import pickle
from collections import Counter
import numpy as np


def dumpDictToFile(d, fileName):
    print('Started Dumping')
    TF, DF, TFIDF, feature_set, frequency_item = d

    formatWTF = '../desctxt/' + fileName + 'TF.pickle'
    formatWDF = '../desctxt/' + fileName + 'DF.pickle'
    formatTFIDF = '../desctxt/' + fileName + 'TFIDF.pickle'
    formatWFQS = '../desctxt/' + fileName + 'FQS.pickle'
    formatWFS = '../desctxt/' + fileName + 'FS.pickle'
    pickle_out_tf = open(formatWTF, "wb")
    pickle_out_df = open(formatWDF, "wb")
    pickle_out_tfidf = open(formatTFIDF, "wb")
    pickle_out_fqs = open(formatWFQS, "wb")
    pickle_out_fs = open(formatWFS, "wb")
    pickle.dump(TF, pickle_out_tf)
    pickle.dump(DF, pickle_out_df)
    pickle.dump(TFIDF, pickle_out_tfidf)
    pickle.dump(feature_set, pickle_out_fs)
    pickle.dump(frequency_item, pickle_out_fqs)
    
    print(fileName + ' is successfully dumped')


def noOfUniqueKeys(d):
    print('NUK')
    feature_keys = []
    for k in d:
        feature_keys = feature_keys + list(d[k])
    feature_counter = Counter(feature_keys)
    frequency_item = dict(feature_counter)
    feature_set = list(feature_counter.keys())
    return [frequency_item, feature_set]


# filepath = 'devset_textTermsPerPOI.txt'
def createDataObject(filepath):
    print('CBO')
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        devSetPerPOI = {}
        while line:
            firstItem = line.find("\"")
            description = line[:firstItem].strip()
            lineArray = line[firstItem:].split()
            devSetPerPOI[description] = {}
            for i in range(0, len(lineArray), 4):
                item = lineArray[i].replace("\"", "")
                TF = float(lineArray[i + 1])
                DF = float(lineArray[i + 2])
                TFIDF = float(lineArray[i + 3])
                devSetPerPOI[description][item] = {
                    'TF': TF,
                    'DF': DF,
                    'TFIDF': TFIDF
                }
            line = fp.readline()
            cnt += 1
    return devSetPerPOI


def constructFeatureVector(d, feature_set, l):
    print('CFV')
    TF= {}
    DF = {}
    TFIDF = {}
    for k in d:
        current = d[k]
        featureVectorTF = np.zeros(shape=(1, l))
        featureVectorDF = np.zeros(shape=(1, l))
        featureVectorTFIDF = np.zeros(shape=(1, l))
        for item in current:
            currentIndex = feature_set.index(item)
            featureVectorTF[0][currentIndex] = current[item]['TF']
            featureVectorDF[0][currentIndex] = current[item]['DF']
            featureVectorTFIDF[0][currentIndex] = current[item]['TFIDF']
        TF[k] = featureVectorTF
        DF[k] = featureVectorDF
        TFIDF[k] = featureVectorTFIDF
    return TF, DF, TFIDF


def main(inputFile, outputFile):
    d = createDataObject(inputFile)
    frequency_item, feature_set = noOfUniqueKeys(d)
    setLength = len(feature_set)
    TF, DF, TFIDF = constructFeatureVector(d, feature_set, setLength)
    # print(featureVectorArray)
    dumpDictToFile([TF, DF, TFIDF, feature_set, frequency_item], outputFile)

main("./../../desctxt/devset_textTermsPerPOI.txt", "devset_textTermsPerPOI")
# main("./../../desctxt/devset_textTermsPerImage.txt", "devset_textTermsPerImage")
main("./../../desctxt/devset_textTermsPerUser.txt", "devset_textTermsPerUser")
