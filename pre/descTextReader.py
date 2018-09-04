# import pandas as pd
# data = pd.read_csv('../desctxt/devset_textTermsPerPOI.txt', sep='', header=None)
import pickle

def dumpDictToFile(d, fileName):
	formatW = '../desctxt/'+fileName
	pickle_out = open(formatW, "wb")
	pickle.dump(d, pickle_out)
	print(formatW + ' is successfully dumped')

# filepath = 'devset_textTermsPerPOI.txt'
def createDataObject(filepath):
	with open(filepath) as fp:  
		line = fp.readline()
		cnt = 1
		devSetPerPOI = {}
		while line:
			firstItem = line.find("\"")
			description = line[:firstItem].strip()
			lineArray = line[firstItem:].split()
			devSetPerPOI[description] = []
			for i in range(0, len(lineArray), 4):
				item = lineArray[i].replace("\"", "")
				TP = float(lineArray[i+1])
				DP = float(lineArray[i+2])
				TPIDP = float(lineArray[i+3])
				devSetPerPOI[description].append({
					'item': item,
					'TP': TP,
					'DP': DP,
					'TPIDP': TPIDP
				})
			line = fp.readline()
			cnt += 1
	return devSetPerPOI

dumpDictToFile(createDataObject("./../../desctxt/devset_textTermsPerPOI.txt"), "devset_textTermsPerPOI.pickle")
dumpDictToFile(createDataObject("./../../desctxt/devset_textTermsPerImage.txt"), "devset_textTermsPerImage.pickle")
dumpDictToFile(createDataObject("./../../desctxt/devset_textTermsPerUser.txt"), "devset_textTermsPerUser.pickle")
