import pickle

pickle_in = open('./../desctxt/devset_textTermsPerPOI.pickle', 'rb')
textTermsPerPOI = pickle.load(pickle_in)

print(len(textTermsPerPOI.keys()))

pickle_in = open('./../desctxt/devset_textTermsPerImage.pickle', 'rb')
textTermsPerImage = pickle.load(pickle_in)

print(textTermsPerImage.keys())

pickle_in = open('./../desctxt/devset_textTermsPerUser.pickle', 'rb')
textTermsPerUser = pickle.load(pickle_in)

print(len(textTermsPerUser.keys()))