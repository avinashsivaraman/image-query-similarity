from utility import openPickleFile, getInput, printResultArray,top3SimilarityFeature


feature_set = openPickleFile('./../desctxt/devset_textTermsPerImageFS.pickle')
ID, d, K = getInput('devset_textTermsPerImage')
sortedResult = printResultArray(d, ID, K)
top3SimilarityFeature(sortedResult, d, ID, feature_set )