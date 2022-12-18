import pickle

file = open("writeData.txt", "rb")
LIST = pickle.load(file)
print(LIST)
