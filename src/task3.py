from utility import mappingSet, openPickleFile, getInput, printResultArray, top3SimilarityFeature

mapping = mappingSet()
feature_set = openPickleFile('./../desctxt/devset_textTermsPerPOIFS.pickle')
locationID, d, K = getInput('devset_textTermsPerPOI')
id1 = list(filter(lambda x: x['number'] == locationID, mapping['topics']['topic']))[0]
ID = id1['title'].replace('_', ' ')
sortedResult = printResultArray(d, ID, K)
top3SimilarityFeature(sortedResult, d, ID, feature_set )