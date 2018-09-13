from utility import openPickleFile, mappingSet
import pandas as pd
import numpy as np
import operator

imageDesc = openPickleFile('./../descvis/imageDescriptor.pickle')

# print(len(imageDesc['CN'].keys()))
LID, K = input().split()
mapping = mappingSet()
id1 = list(filter(lambda x: x['number'] == LID, mapping['topics']['topic']))[0]
ID = id1['title']
results = []
for modal in imageDesc:
    # print('Processing the modal', modal)
    currentModal = imageDesc[modal]
    queryLocation = currentModal[ID]
    result = []
    for location in currentModal:
        # print('Processing the location', location)
        currentLocation = currentModal[location]
        if(location != ID):
            diff = np.linalg.norm(queryLocation - currentLocation)
            result.append([modal, location ,diff])
    results.append(result)

# overallResultSorted = sorted(overallResult.items(), key=lambda kv: kv[1], reverse=True)

#Normalize all the value in the array
def normalize(x, MIN, MAX):
    a = (x - MIN)/(MAX - MIN)
    # print(a)
    if(a > 1):
        print(MIN, MAX, x)
    return a

#Normalize the results
for each in results:
    MIN = min(each, key=lambda x: x[2])[2]
    MAX = max(each, key=lambda x: x[2])[2]
    for every in each:
        every[2] = normalize(every[2], MIN, MAX)

overallResult = {}
overallTenScore = {}

for key in results:
    for k in key:
        if(k[1] not in overallResult):
            overallResult[k[1]] = k[2]
        else:
            overallResult[k[1]]+=k[2]
        if(k[1] not in overallTenScore):
            overallTenScore[k[1]] = {}
        overallTenScore[k[1]][k[0]] = k[2]

overallResult = sorted(overallResult.items(), key=operator.itemgetter(1), reverse=True)[:int(K)]


for k in overallResult:
    print('Matched Location: ', k[0])
    print('Match score:', k[1])
    print('Individual Contribution: ', overallTenScore[k[0]])
    print()

# print(len(overallTenScore.keys()))
# print(results);
        


# # print(overallResultSorted)
# for index in range(len(results)):
    
#     results[index] = sorted(results[index], key=lambda  x: x[2])[:int(K)]



# print(results)