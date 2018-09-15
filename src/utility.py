import pickle
import numpy
from scipy import spatial
import xmltodict

def mappingSet():
    # This is only used in Task 3 to get the mapping between the location and locationID
    devset_topics = open('./../../devset_topics.xml', 'rb')
    return xmltodict.parse(devset_topics)

def openPickleFile(fileName):
    #Opening the feature_set which contains the unique terms from our dataset
    feature_set_pickel = open(fileName, 'rb')
    feature_set = pickle.load(feature_set_pickel)
    return feature_set

def getInput(inputFile):
    ID, M, K = input().split()    
    #Fetching the file based on the Model
    dfile = open('./../desctxt/'+inputFile+M+'.pickle', 'rb')
    #Loading the dict of feature vectors of all IDs into 'd'
    d = pickle.load(dfile)
    return ID, d, K

def printResultArray(d, ID, K):
    # Fetching the Feature vector for the given id
    given = d[ID]
    result = []
    # Finding the euclidean distance between the given and other vector available
    # print(given)
    givenNonZero = numpy.nonzero(given)[1]
    for k in d:
        if(k != ID):
            # Using numpy to find the distance
            # diff = 1 - spatial.distance.cosine(given, d[k])
            diff = numpy.linalg.norm(given-d[k])
            # print('a', givenNonZero, end='\n')
            # print(len(givenNonZero))
            currentNonZero = numpy.nonzero(d[k])[1]
            # print('b', currentNonZero, end='\n')
            # print(len(currentNonZero))
            unionD = len(numpy.unique(numpy.append(givenNonZero, currentNonZero)))
            # print('u', unionD, end='\n')
            interD = len(givenNonZero) + len(currentNonZero) - unionD

            if(interD < 3):
                # We are not considering the user with less than 3 similarities
                result1 = 0
            else:
                # Jacaad Similarity index
                J = interD / unionD
                # Dividing the 'J' index with euclidean distance
                result1 = J / (1 + diff)
        result.append([k, result1])
    
    # Sorting the euclidean distance vector in increasing order such that we can pick the first 'K' Similarities easily
    sortedResult = sorted(result, key=lambda x: x[1], reverse=True)
    return sortedResult[:int(K)]

def top3SimilarityFeature(sortedResult, d, ID, feature_set):
    given = d[ID][0]
    givenListIndex = numpy.nonzero(given)[0].tolist()
    for i in range(len(sortedResult)):
        currentID = sortedResult[i][0]
        # print(currentID)
        current = d[currentID][0]
        currentListIndex = numpy.nonzero(current)
        unionListIndex = numpy.unique(numpy.append(givenListIndex, currentListIndex))
        # Stores (index, distance)
        Listdifferences = []
        for index in unionListIndex:
            # print(index)
            Listdifferences.append((index, numpy.abs(given[index] - current[index])))
        
        # Sort based on distances
        Listdifferences.sort(key=lambda x: x[1])
        
        # print(Listdifferences)
        # Finding 2 most similar terms in this example
        similarTerms = Listdifferences[:3]
        # print(similarTerms, end='\n')
        
        # Replace indexes with actual words (features) using the reversed dictionary
        similarTerms = list(map((lambda x : (feature_set[x[0]], x[1])), similarTerms))
        print(currentID, sortedResult[i][1], similarTerms)          

