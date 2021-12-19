import pickle

def predi(params):
    pickle_in = open('rfc_banknoteauth.pkl', 'rb')
    clf = pickle.load(pickle_in)
    pred = clf.predict([params])

    return pred