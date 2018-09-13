from utility import openPickleFile, mappingSet
import pandas as pd
import numpy as np

imageDesc = openPickleFile('./../descvis/imageDescriptor.pickle')

# print(len(imageDesc['CN'].keys()))
LID, M, K = input().split()

mapping = mappingSet()
id1 = list(filter(lambda x: x['number'] == LID, mapping['topics']['topic']))[0]
ID = id1['title']

modalVector = imageDesc[M]
query = imageDesc[M][ID]
result = []

for i in modalVector:
    if(i != ID):
        diff = np.linalg.norm(query - modalVector[i])
        result.append([i, diff])

sortedResult = sorted(result, key=lambda x: x[1])[:int(K)]

print(sortedResult)

# print('Finding the Match Pair which contributed the most')

# mypath = './../../descvis/img/'
# queryFileName = "{} {}.csv".format(ID, M)
# queryd = pd.read_csv( mypath + queryFileName, header=None)
# print(queryd.columns[1:])
# for k in sortedResult:
#     name, matchingscore = k
#     fileName = "{} {}.csv".format(name, M)
#     d = pd.read_csv( mypath + fileName, header=None)
#     for key, rows in queryd.iterrows():
#         for key2, rows2  in d.iterrows():
                
#             break
#         break

    # print(fileName)
