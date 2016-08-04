
dataset = {}

def loadData():
    i = 0
    for line in open('../data/opendata_20w.txt', 'rb'):
        dataset[i] = line
        i = i + 1

    return dataset
