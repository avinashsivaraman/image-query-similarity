import pandas as pd
import pickle
from os import listdir, makedirs
from os.path import isfile, join, exists

mypath = './../../descvis/img/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
result = {}


for k in onlyfiles:
    # print('Reading the'+mypath+'and the file'+k)
    d = pd.read_csv( mypath + k, header=None)
    location, modelWithExtension = k.split(' ')
    model = modelWithExtension.split('.')[0]
    # print('Location'+location)
    # print('Processing',model)
    col_mean = d.mean(axis=0)[1:]
    if (model not in result):
        result[model] = {}
    result[model][location] = col_mean
    # print(result, end='\n\n')
    print(model +'    ', result[model].keys(), end='\n')
    # print('Added the col_mean', col_mean)

directory = './../descvis'

if not exists(directory):
    makedirs(directory)

pickle_out_tf = open(directory+'/imageDescriptor.pickle', "wb")
pickle.dump(result,pickle_out_tf)
print('Dumped the file')

